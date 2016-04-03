#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.api import users  #import google user features to log users in and out
from google.appengine.ext import ndb  #import datastore library

import os  #to find and join the file path

import jinja2   #used for HTML templates
import webapp2  #used to work with websites.

from db_classes import *  #import all the classes defined in db_classes

"""create a variable with the path to the template files stored.
create a second jinja Environment loading the files from that directory."""
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)



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



class MainHandler(Handler):
  def get(self):
    podcasts = Podcast.query().fetch()
    self.render('home.html', podcasts=podcasts)

# def add_image():
#   refs = Reference.query().fetch(keys_only=True)
#   for ref in refs:
#     refer = Reference.get_by_id(ref.id())
#     refer.image = "/images/4hourworkweek.jpg"
#     refer.put()


class RefHandler(Handler):
  def get(self):
    fetch_no = 10
    references = Reference.query().order(-Reference.counter).fetch(fetch_no)
    #add_image()
    podcasts = podcast_dict()
    self.render('references.html', references=references, podcasts=podcasts)



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/references/', RefHandler)
], debug=True)
