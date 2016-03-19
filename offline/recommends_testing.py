#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Iain Forrest
#
# Created:     03/02/2016
# Copyright:   (c) Iain Forrest 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os



def offline_html_doc(html):
    cwd = os.path.dirname(__file__)
    file_path = os.path.join(cwd, 'html', html)
    #Only use path.join to join locations and file name as structure is different on different OS \ or /
    with open(file_path) as f:
        page = f.read()
    try:
        start = page.index('<article')
        finish = page.index('</article')
    except ValueError:
        try:
            start = page.index('<body')
            finish = page.find('</body')
        except ValueError:
            start, finish = 0,len(page)
    else:
        page = page[start:finish]
    return page

#print offline_html_doc('Luis von Ahn.html')