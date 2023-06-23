def app(environ, start_response):
    with open("allcats.html", 'r') as f:
        data = f.read().encode()
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/html'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])