from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('nblog/', views.NBlogListView.as_view(), name='nblog_list'),
    re_path(r'^nblog/(?P<slug>[-\w]+)/', views.NBlogDetailView.as_view(), name='nblog_detail'),
]

