from django.shortcuts import render
from django.http import HttpResponse

import time
# Create your views here.

def homePageView(request):
    '''respond to an HTTP request with a single web page.'''

    response_html = '''
    <html>
    <h1>Hello, world!</h1>
    <p>
    This is our first Django web application!
    </p>
    <hr>
    This page was generated at %s.
    </html>
    ''' % time.ctime()
    return HttpResponse(response_html)
