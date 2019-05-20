from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('lotto/',views.lotto),
    path('halo/',views.halo),
    path('dinner/', views.dinner),
    path('midnight/', views.midnight),
    path('hello/<name>/', views.hello),
    path('cube/<int:num>/', views.cube),
    path('introduce/<name>/<int:age>/', views.introduce),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('area/<int:r>/', views.area),
    path('isbirth/', views.isbirth),
    path('template_example/', views.template_example),
    path('ping/', views.ping),
    path('pong/', views.pong),
    path('static_example/', views.static_example),
]