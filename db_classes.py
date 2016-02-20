from google.appengine.api import users  #import google user features to log users in and out
from google.appengine.ext import ndb  #import datastore library

"""
class Person(ndb.Model):
    '''Sub-class model for Podcast interviewee'''
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty(default='')
    twitter_handle = ndb.StringProperty(default='')
    website = ndb.StringProperty(default='')
"""
class Reference(ndb.Model):
    '''Model for books and other recommended references.
    Auto generated ID used as the key'''
    title = StringProperty()
    author = StructureProperty(Person)
    href = ndb.StringProperty()

class Podcast(ndb.Model):
    '''Datastore Model for published podcasts. Postcast ids striped from the
    html page are to be used as key names'''
    title = ndb.StringProperty()
    href = ndb.StringProperty()
    #image_href = ndb.StringProperty()
    #interviewee = ndb.StructureProperty(Person)
    #posted_date = ndb.DateTimeProperty()
    #references =  ndb.StringProperty(repeated=True) #list of link_ids
