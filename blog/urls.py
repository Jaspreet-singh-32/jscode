from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.bloghome,name="bloghome"),
    path('PostComment/',views.PostComment,name="PostComment"),
    path("<str:slug>",views.blodpost,name="post")
]
