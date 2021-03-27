from django.urls import include, path
from sectionone.views import PostList
urlpatterns =[
    path('create/', views.PostList.asview())
]