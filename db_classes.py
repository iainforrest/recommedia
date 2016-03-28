from google.appengine.api import users  #import google user features to log users in and out
from google.appengine.ext import ndb  #import datastore library

"""
class Person(ndb.Model):
    '''Sub-class model for Podcast interviewee'''
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty(default='')
    twitter_handle = ndb.StringProperty(default='')
    website = ndb.StringProperty(default='')
    podcast_page = ndb.KeyPropety(kind='Podcast')
    recommended_books = ndb.KeyProperty(kind='Reference', repeated=True)
"""

class Reference(ndb.Model):
    '''Model for books and other recommended references.
    title of book used as the key'''
    title = ndb.StringProperty()
    author = ndb.StringProperty()
    href = ndb.StringProperty()
    referrer = ndb.StringProperty(repeated=True)
    counter = ndb.IntegerProperty(default=1)

class Podcast(ndb.Model):
    '''Datastore Model for published podcasts. Postcast ids striped from the
    html page are to be used as key names'''
    title = ndb.StringProperty()
    href = ndb.StringProperty()
    #image_href = ndb.StringProperty()
    #interviewee = ndb.StructureProperty(Person)
    #posted_date = ndb.DateTimeProperty()
    #references =  ndb.StringProperty(repeated=True) #list of link_ids

def podcast_dict():
    pod_dict = {}
    podcasts = Podcast.query().fetch()
    for pod in podcasts:
        pod_dict[pod.key.id()] = [pod.title, pod.href]
    return pod_dict
