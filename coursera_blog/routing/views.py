from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_http_methods, require_POST


# HttpResponse.__init__(content='', content_type=None, status=200, reason=None, charset=None)[source]¶

@require_http_methods(['GET', 'PUT', 'POST'])
def simple_route(request, something=None):
    if request.method == 'GET' and something == None:
        return HttpResponse(content='', status=200)
    elif request.method in ['POST', 'PUT']:
        return HttpResponse(status=405)
    else:
        return HttpResponse(status=404)


# @require_GET()
@require_http_methods(['GET'])
def slug_route(request, first=None, second=None):
    if second is None:
        return HttpResponse(content=first, status=200)
    else:
        return HttpResponse(status=404)


# @require_GET()
@require_http_methods(['GET'])
def sum_route(request, first, second):
    if check_int(first) and check_int(second):
        return HttpResponse(content=str(int(first) + int(second)), status=200)
    else:
        return HttpResponse(status=404)


# @require_GET()
@require_http_methods(['GET'])
def sum_get_method(request):
    first = request.GET.get('a')
    second = request.GET.get('b')

    if check_int(first) and check_int(second):
        return HttpResponse(content=str(int(first) + int(second)), status=200)
    else:
        return HttpResponse(status=400)


# @require_POST()
@require_http_methods(['POST'])
def sum_post_method(request):
    first = request.POST.get('a')
    second = request.POST.get('b')

    if check_int(first) and check_int(second):
        return HttpResponse(content=str(int(first) + int(second)), status=200)
    else:
        return HttpResponse(status=400)


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

#     id = request.GET.get('id')  // /blog/blog_post/?id=123
#     https://www.youtube.com/watch?v=w_qfivxRra8
#     from routing.views import simple_route, slug_route, sum_route, sum_get_method, sum_post_method


# 4-я задача
# Добрый день! Вы усложняете себе задачу, сделайте вызов функции sum_get_method по шаблону
# url - r'^sum_get_method/$', а получение параметров и логику реализуйте внутри sum_get_method.
