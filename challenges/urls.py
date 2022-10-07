from django.urls import path,include
from. import views
urlpatterns=[
    path('',views.challenges,name='challenges'),
    path('colorista',views.colorista,name='colorista')
]
