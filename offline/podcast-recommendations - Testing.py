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

import urllib2, urllib,re
from contextlib import closing

import htmlentitydefs
import os

import recommends_testing

http_list = {'Ferriss':'http://fourhourworkweek.com/podcast/'}

html_docs = {'Home': 'Podcast list.html',
            'Podcasts': ['Jamie Foxx.html', 'Derek Sivers Reloaded.html',
                        'Edward Norton.html', 'Luis von Ahn.html','Naval Ravikant.html']}

def offline_http():
    html = 'Derek Sivers Reloaded.html'
    cwd = os.path.dirname(__file__)
    file_path = os.path.join(cwd, 'html', html)
    #Only use path.join to join locations and file name as structure is different on different OS \ or /
    with open(file_path) as f:
        print f
        page = f.read()
    page = page[page.find('<article'):page.find('<\/article')]
    return page


podcast_find_pattern = '''<p\s #search through html for <p with trailing whitespace
        id="post-       #whitespace is followed by a post ids
        ([0-9]{5})"     #Match the 5 number post id and store that
        .*?<a\shref=    #Skip any extra characters including newlines until a link is found
        "(.*?)"         #Match the http link inside the ""
        .*?>            #Skip any other characters in the <a> tag. ie. target="_blank"
        (.*?)<\/a>      #Match the text before the </a> as the title
        .*?<\/p>        #move to end of the post paragraph
        '''

book_find_pattern = '''
        a\shref="  #looks for list item with link
        (http:\/\/.*?) #gets all books, post, audiobooks
                #adds the above selection to tuple
        ".*?>   #
        (.*?)       #selects the name of the book inside the link
        <\/a>       #searches for end of link followed by
        \sby\s      # _by_ which points to a book and not a movie or other
        (\w+\W\w+)  #selects the authors names word_space_ word
        <\/li>      #followed by end of line
        '''

second_book_patern = '''
        <a\shref="
        (.*?")
        .*?>
        (.*?)$
        '''

db_parent_pattern = 'http\:\/\/w*\.?(.*?)\.com' #matches with or without www

all_books = {}
#structure
# KEY = name of book : href, author, counter, [referrer]

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


def get_page(url):
    parent_db = get_re(db_parent_pattern, url, '', 'search')
    with closing(urllib2.urlopen(url)) as page:
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
        main_page = main_page.replace(u'\xa0',u' ') #remove bytecode space to space
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

def strip_tag(book):
    #print book
    book_href, book_title, book_author = book
    tag_start = book_href.find(u'?tag')
    #print tag_start
    if tag_start != -1:
        book_href = book_href[:tag_start]
        #print book_href
    return (book_href, book_title, book_author)


def look_for_multi_books(list_of_books):
    for book in list_of_books:
        if '<a href' in book[1]:
            book_index = list_of_books.index(book)
            href, title, author = list_of_books.pop(book_index)
            try:
                second = get_re(second_book_patern, title, '(?x)', 'findall')[0]
                new_book = (second[0],second[1],author)
                first_book = (href, title[:title.find('</a>')], author)
            except TypeError:
                new_book = None
            else:
                if new_book:
                    list_of_books.insert(book_index, new_book) # this places the new book after the first which means
                    #if there is more than two it's keep reducing until all books are extracted.
                    list_of_books.insert(book_index, first_book)
    return [strip_tag(book) for book in list_of_books]

def get_books_from_page(podcast_html_page):
    '''given a podcast show notes page, extract the parent db and the list of books.
    Assuming that books come in the format of a list, amazon link, title, ' by ' author
    Books are returned as list of tuples (href, title, author)
    '''
    pod_page, parent_db = get_page(podcast_html_page)
    #print pod_page
    books = get_re(book_find_pattern, pod_page, '(?x)', 'findall')
    if books: books = look_for_multi_books(books)
    return books, parent_db

def add_books_to_dict(list_of_books, referrer_podcast_id):
    '''go through list, check if in dict, if so increase counter by 1 and add referrer id to list
    else add book to dict
    '''
    for href, title, author in list_of_books:
        if title in all_books:
            all_books[title]['counter'] +=1
            all_books[title]['referrer'].append(referrer_podcast_id)
        else: all_books[title] = {'href': href, 'author': author, 'counter': 1, 'referrer':[referrer_podcast_id]}


def main(http):
    #offline main_page = html #get_page(http)
    #main_page, parent_db = get_page(http)


    #podcasts = get_re(podcast_find_pattern, main_page, '(?xs)','findall')
    #print podcasts[0]
    '''
    for referrer, href, title in podcasts:
        books, parent_db = get_books_from_page(href)
        if books: add_books_to_dict(books,referrer)
    '''
    books, parent_db = get_books_from_page('http://fourhourworkweek.com/2015/07/05/stanley-mcchrystal/')
    if books: add_books_to_dict(books,u'15554')
    print all_books



#main(html_docs['Home']) #offline
main(http_list['Ferriss']) #online

#print recommends_testing.offline_html_doc(html_docs['Podcasts'][1])


