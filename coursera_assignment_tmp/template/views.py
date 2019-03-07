from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# get с: 2
# get b: 3
# statement is empty

"""
@register.filter(name='inc')
def inc(value, arg):
    return int(value) + int(arg)


@register.simple_tag
def division(a, b, to_int=False):
    return int(a)//int(b) if to_int is True else int(a)/int(b)
    
    
Немного странно: если поставить декоратор @register.tag то тест не проходится, а с декоратором 
@register.simple_tag тест проходит. Почему, какие между ними отличия ?    

Вопрос решен. Не хватало проверки на ноль.

Подскажите, пожалуйста, какие именно заголовки запроса нужны? 
вернуть нужно параметры и значение HTTP_X-PRINT-STATEMENT, если оно передано.

Попробовал простейшие варианты:
первый
{% extends "base.html" %}
{% block title %}new_block{% endblock %}
{% block content %}
{{block_a}}
{{block_b}}
{% endblock %}

или второй, если убрать все теги нового блока
{% extends "base.html" %}
{{block_a}}
{{block_b}}
У меня отображается родительская страница целиком. Вопрос: как отобразить один блок из родительской страницы ?

Нашел. Вызвать содержимое родительского блока: {{block.super}}

Обнулить содержимое родительского блока: 
{% block block_a %}{{a}}{% endblock %} просто не указать ничего в теле. 
А если в тело вставить super то и как раз получится часть требуемого задания.




def echo(request):
return render(request, 'echo.html', context={
    'get_letter': request.META['QUERY_STRING'][0],
    'get_value': request.GET.get(request.META['QUERY_STRING'][0]),
    'get_tag': request.META.get('HTTP_X_PRINT_STATEMENT'),
    'request_method': request.META['REQUEST_METHOD']
})


<!--DOCTYPE html -->
<html>
<body>
{% if 'QUERY_STRING' in request.META %}
    <h1> {{ request_method }} {{ get_letter }}: {{ get_value }} statement is empty </h1>
{% elif 'HTTP_X_PRINT_STATEMENT' in request.META %}
    <h2> statement is {{get_tag}} </h2>
{% endif %}
</body>
</html>

"""

def echo(request):
    return HttpResponse(status=200)


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
