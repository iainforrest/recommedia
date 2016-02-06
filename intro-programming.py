import urllib #used in several places for working with URL's
import urllib2
import json
import logging

from google.appengine.api import users  #import google user features to log users in and out
from google.appengine.ext import ndb  #import datastore library

import os  #to find and join the file path

import jinja2   #used for HTML templates
import webapp2  #used to work with websites.

"""create a variable with the path to the template files stored.
create a second jinja Environment loading the files from that directory."""
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

admin_emails = ['redefine.everything.ltd@gmail.com','review-support@udacity.com', 'introprogramming-support@udacity.com']

DEFAULT_COMMENTBOOK_NAME = 'default_CommentBook'

class Handler(webapp2.RequestHandler):
    """The write, render_str and render functions create and easy way for us to render html
    templates in python using the jinja2 Environment.
    We can simply call self.render('name-of-template.html', kwargs) in our class and it will
    automatically create get the template and render it using the kwargs and then wrap that up
    in response.out.write so that it outputs to the screen"""
    def write(self, *a, **kw):
       self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
       t = jinja_env.get_template(template)
       return t.render(params)

    def render(self, template, **kw):
       self.write(self.render_str(template, **kw))


def commentbook_key(commentbook_name=DEFAULT_COMMENTBOOK_NAME):
    """Constructs a Datastore key for a commentbook entity.
    We use commentbook_name as the key."""
    return ndb.Key('CommentBook', commentbook_name)

class Location(ndb.Model):
    """Sub Model for user's location at time of comment"""
    ip = ndb.StringProperty(indexed=False)
    country_name = ndb.StringProperty(default='CLASSIFIED')
    city = ndb.StringProperty(default='CLASSIFIED', indexed=False)
    country_code = ndb.StringProperty(default='XX', indexed=False)
    lat = ndb.StringProperty(default = '9.232', indexed=False)
    lng = ndb.StringProperty(default = '-150.996', indexed=False)
    map_center  = ndb.StringProperty(indexed=False)


class Author(ndb.Model):
    """Sub model for representing an author."""
    identity = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)


class Comment(ndb.Model):
    """A main model for representing an individual commentbook entry."""
    author = ndb.StructuredProperty(Author)
    content = ndb.StringProperty(indexed=False)
    location = ndb.StructuredProperty(Location)
    date = ndb.DateTimeProperty(auto_now_add=True)

def get_user(page_request):
    '''Used to find out if there is a user logged in. If so it returns the user details plus a logout link.
    if there is no user a login link is returned.
    This is used primarily for comments.'''
    user = users.get_current_user()  #this is a special function from google app engine
    if user:
        url = users.create_logout_url(page_request.uri)
        url_linktext = 'Logout'
    else:
        url = users.create_login_url(page_request.uri)
        url_linktext = 'Login'
    return user, url, url_linktext

def get_user_location(ip_address):
    '''we get the users location details using the API from http://www.hostip.info/
    We have chosen to receive this in JSON format, which is then easily converted to a dictionary.
    We have a default set of location information in case the service doesn't work or is unable
    to determine an accurate location.
    We then do a couple of variable checks on the outcome to ensure the static map works well
    Finally we return a dictionary with the same key words as the NDB datastore class Location'''
    default_user_location = {
        'ip': ip_address,
        'country_name': 'CLASSIFIED',
        'city': 'CLASSIFIED',
        'country_code': 'XX',
        'lat': '9.232',
        'lng': '-150.996',
        'map_center' : '9.232,-150.996' }
    try:
        api_return = urllib2.urlopen('http://api.hostip.info/get_json.php?ip=' + ip_address +'&position=true').read()
    except:
        return default_user_location  #use default is retrieve fails
    else:
        location_dict = json.loads(api_return)
        if any(x in location_dict['country_name'] for x in ['Unknown','Private']):
            location_dict = default_user_location
        elif any(x in location_dict['city'] for x in ['Unknown','Private']):
            location_dict['city'] = 'CLASSIFIED'
            location_dict['map_center'] = location_dict['country_name']
        else:
            location_dict['map_center'] = location_dict['lat'] + ',' + location_dict['lng']
        return location_dict


class MainHandler(Handler):
    """Creates the main pages for the stages displayed on the website.
    The error message is for incorrect input in comments
    Temp path is used to define the separate comment books for each page as well as to load the correct html file"""
    def get(self):
        logging.info('I think we may have a winner')
        error_message = self.request.get('error_message')
        temp_path = "default_" if self.request.path == '/' else self.request.path.strip('/')
        commentbook_name = temp_path
        comments_query = Comment.query(ancestor=commentbook_key(commentbook_name)).order(-Comment.date)
        comments = comments_query.fetch()


        user, url, url_linktext = get_user(self.request)
        user_location = get_user_location(self.request.remote_addr)  #'84.158.65.221')   #  207.202.6.127')  #

        self.render(temp_path+'.html', user=user, comments=comments, commentbook_name=urllib.quote_plus(commentbook_name),
            url=url, url_linktext=url_linktext, temp_path=temp_path, error_message=error_message, **user_location)


class CommentBook(webapp2.RequestHandler):
    '''This is for collecting comments posted by the form, it gets the name of the ancestor book from the path,
    Checks to see if there is a current suer logged in and if so assigns that person as the author, otherwise
    author is anon. Then it checks that some content was actually submitted, if no content then redirect
    back to the comment section with the error message.
    If everything checks out then commit the object to the datastore and reload the page with the new comments.
    '''
    def post(self):

        temp_path = "/" if self.request.get('temp_path') == 'default_' else '/'+self.request.get('temp_path') +'/'

        commentbook_name = self.request.get('commentbook_name', DEFAULT_COMMENTBOOK_NAME)
        comment = Comment(parent=commentbook_key(commentbook_name))

        if users.get_current_user():
            comment.author = Author(
                    identity=users.get_current_user().user_id(),
                    email=users.get_current_user().email())

        comment.content = self.request.get('content')
        user_location = get_user_location(self.request.remote_addr)  #'84.158.65.221')   #  207.202.6.127')   #  self.request.remote_addr)  #
        comment.location = Location(**user_location)

        if comment.content.strip():
            comment.put()
            error_message = ""
        else:
            error_message = "Sorry, You need to enter a comment if you want to submit it."

        query_params = {'commentbook_name': commentbook_name,'error_message':error_message}
        self.redirect(temp_path+'?' + urllib.urlencode(query_params) + '#comments')

class AdminHandler(Handler):
    '''This is the admin page where an admin can view comments from all pages and delete ones if required.
    It loads up all the comments and then prints them by page.
    In the html it adds the key for each comment to an anchored button which if clicked, reloads this class
    and activated the if delete_key section.
    '''
    def get(self, delete_message=None):
        delete_key = self.request.get('delete')
        if delete_key:
            ndb.Key(urlsafe=delete_key).delete()
            delete_message = "The Comment Was Successfully Deleted."

        allcomments = []

        all_keys = Comment.query().fetch(keys_only=True)  #list of all keys
        #sorted() orders set() which removes duplicates but doesn't keep order
        #.parent() gets the ancestors keys and .id() gets the string ID in tuple Kind1,Id1
        stages = sorted(list(set([key.parent().id() for key in all_keys])))

        for stage in stages:
            comments = Comment.query(ancestor=commentbook_key(stage)).order(-Comment.date).fetch(20)
            allcomments.append([stage,comments])

        user, url, url_linktext = get_user(self.request)
        admin = True if user and user.email() in admin_emails else False

        self.render('adminUI.html', allcomments=allcomments, temp_path="admin ",
            delete_message=delete_message, user=user, admin=admin, url=url, url_linktext=url_linktext)

class RedirectHandler(webapp2.RequestHandler):
    #because of the nature of the website I have removed the base landing page at this time and redirected to stage1
    def get(self):
        self.redirect('/stage1/')


app = webapp2.WSGIApplication([('/', RedirectHandler),
    ('/stage1/', MainHandler),
    ('/stage2/', MainHandler),
    ('/stage3/', MainHandler),
    ('/stage4/', MainHandler),
    ('/stage5/', MainHandler),
    ('/adminUI/', AdminHandler),
    ('/sign', CommentBook)], debug=True)


