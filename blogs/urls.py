from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    re_path(r'^blog/(?P<slug>[-\w]+)/', views.BlogDetailView.as_view(), name='blog_detail'),
]

