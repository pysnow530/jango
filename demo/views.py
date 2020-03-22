from jango.http import HttpResponse


def welcome(request, nickname):
    content = f'Hello {nickname}, welcome to jango.'
    response = HttpResponse(content=content)
    return response


def foobar(request):
    content = 'This is a sub urlpattern demo.'
    response = HttpResponse(content=content)
    return response
