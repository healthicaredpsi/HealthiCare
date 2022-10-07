from django.urls import path
from. import views
urlpatterns=[
    path('contact',views.contact,name='contactus'),
    path('/about_before_login',views.about_before_login,name='about_before_login'),
    path('/about_after_login',views.about_after_login,name='about_after_login')
]