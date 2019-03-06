from django.http import HttpResponse


# HttpResponse.__init__(content='', content_type=None, status=200, reason=None, charset=None)[source]¶


def simple_route(request, something=None):
    if request.method == 'GET' and something == None:
        return HttpResponse(content='', status=200)
    elif request.method in ['POST', 'PUT']:
        return HttpResponse(status=405)
    else:
        return HttpResponse(status=404)


def slug_route(request, something=None):
    if request.method == 'GET' and something == None:

    return HttpResponse('ok')


def sum_route(request):
    return HttpResponse('ok')


def sum_get_method(request):
    return HttpResponse('ok')


def sum_post_method(request):
    return HttpResponse('ok')

#     id = request.GET.get('id')  // /blog/blog_post/?id=123
#     https://www.youtube.com/watch?v=w_qfivxRra8
#     from routing.views import simple_route, slug_route, sum_route, sum_get_method, sum_post_method


# 4-я задача
# Добрый день! Вы усложняете себе задачу, сделайте вызов функции sum_get_method по шаблону
# url - r'^sum_get_method/$', а получение параметров и логику реализуйте внутри sum_get_method.
