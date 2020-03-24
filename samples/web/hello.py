
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello %s!</h1>' % environ['PATH_INFO'][1:] or 'Web'
    # return [b'<h1>Hello Web!</h1>']
    return [body.encode('utf-8')]