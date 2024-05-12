from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('blog/', views.BlogList.as_view(), name='blog_list'),
    re_path(r'^blog/(?P<slug>[-\w]+)/', views.BlogDetail.as_view(), name='blog_detail'),
]

