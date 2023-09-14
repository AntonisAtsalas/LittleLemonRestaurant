from django.http import HttpResponse

def handler404(request, exception):
    response = HttpResponse('<h1>404: Page not found!</h1>\n'
                            '<p>Sorry, the page you are looking for does not exist.</p>\n'
                            '<a href="/">Go to homepage</a>')
    response.status_code = 404  # Set the HTTP status code to 404
    return response