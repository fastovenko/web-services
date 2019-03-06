from django.conf.urls import url

from coursera_assignment_tmp1.routing.views import simple_route, slug_route, sum_route, sum_get_method, sum_post_method

urlpatterns = [
    url(r'^routing/simple_route/$', simple_route),
    url(r'^routing/simple_route/(w+)/$', simple_route),
    url(r'^routing/slug_route/([0-9]w)+{16}/$', slug_route),
    url(r'^routing/slug_route/([0-9]w)+/$', slug_route),
    url(r'^routing/slug_route/(*)+/$', slug_route),
]
