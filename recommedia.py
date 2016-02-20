#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Iain Forrest
#
# Created:     17/01/2016
# Copyright:   (c) Iain Forrest 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import webapp2
import urllib2, re
import htmlentitydefs

from db_classes import *  #import all the classes defined in db_classes

http_list = ['http://fourhourworkweek.com/podcast/']

podcast_find_pattern = '''
        <p\s            #search through html for <p with trailing whitespace
        id="post-       #whitespace is followed by a post ids
        ([0-9]{5})"     #Match the 5 number post id and store that
        .*?<a\shref=    #Skip any extra characters including newlines until a link is found
        "(.*?)"         #Match the http link inside the ""
        .*?>            #Skip any other characters in the <a> tag. ie. target="_blank"
        (.*?)<\/a>      #Match the text before the </a> as the title
        .*?<\/p>        #move to end of the post paragraph
        '''

book_find_pattern = '''
        <li><a\shref=" #search for <li> item followed by a link
        (.*?)		         #capture the href (amazon) inside the quotes
        \?tag.*?>      #but skip the affiliate link
        (.*?)          #capture the title of the book inside the <a> tags
        <\/a>
        \sby\s         #make sure link is followed by " by " this ensures a book link
        (\w+\W\w+)     #capture the following author name (word,whitespace,word)
        <\/li>         #searched for text finished with </li>
        '''

db_parent_pattern = 'http\:\/\/w*\.?(.*?)\.com' #matches with or without www


def podcastdb_key(podcastDB_name = 'fourhourworkweek'):
    '''Constructs a Datastore key for the DB entry'''
    return ndb.Key('PodcastDB', podcastDB_name)


def unescape(text):
    '''Copied from http://effbot.org/zone/re-sub.htm#unescape-html
    uses re to search through the string and use the internal function fixup
    to substitute the unicode elements for there character equivilents'''
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)


def get_database_id(parent_db):
    db_query = Podcast.query(ancestor=podcastdb_key(parent_db)).order


def get_page(url):
    '''returns unescaped html text from url and
    domain name for the ancestor ndb name'''
    parent_db = get_re(db_parent_pattern, url, '', 'search')
    with closing(urllib.urlopen(url)) as page:
        main_page = unescape(page.read().decode('utf-8'))
    try:
        start = main_page.index('<article')
        finish = main_page.index('</article')
    except ValueError:
        try:
            start = main_page.index('<body')
            finish = main_page.find('</body')
        except ValueError:
            start, finish = 0,len(main_page)
    else:
        main_page = main_page[start:finish]
    return main_page, parent_db

def get_re(pattern, text, flags='', re_type='findall'):
    '''An abstracted regex function for multi-types
    Flags are added in the form (?sx) and concat with pattern before compile
    Currently only set for re_type=='search' and 'findall'(default)
    Function returns a string if search and a list of strings in findall or None'''
    pattern = pattern + flags
    expression = re.compile(pattern)
    if re_type == 'search':
        result = expression.search(text)
        return result.group(1) if result else None #checks for result and returns string if found and none if not
    elif re_type =='findall':
        result = expression.findall(text)
    else: result = None
    return result if result else None

def process_podcast_page(http):
    #some code goes in here
    books = get_re(book_find_pattern, pod_page, '(?x)', 'findall')


def process_matches(matched_podcasts, parent_db):
    '''Query the datastore for all podcast keys,
    then loop through the podcasts found from get_page(url) and check to see if the
    key is in the datastore. If not then assign the details collected from the home page
    then follow the link, extract the other info and also create recommended books
    before moving onto the next podcast in the list
    '''
    all_podcast_keys = Podcast.query().fetch(keys_only=True) #get all podcast keys

    for pod in matched_podcasts:
        if pod[0] not in all_podcast_keys: #if not then process now
            podcast = Podcast(parent= podcastdb_key(parent_db),
            id=pod[0], #podcast id from post
            href = pod[1],   #http:// link from post
            title = pod[2])  #title from between <a>*</a> tags
            '''
            imghref, person, reflist = process_podcast_page(podcast.href)
#need to create process_podcast_page
            podcast.image_href = imghref
            podcast.interviewee = person
            podcast.references = reflist
            '''
            podcast.put()




class MainHandler(webapp2.RequestHandler):
    def get(self):
        for http in http_list:
            main_page, parent = get_page(http)
            podcasts = get_re(podcast_find_pattern, main_page, '(?xs)','findall')
            #above returns list of podcasts in tuple [(id,href,title),...]
            if podcasts: process_matches(podcasts, parent)

app = webapp2.WSGIApplication([
    ('/podcast-check/check',MainHandler)
], debug=True)


