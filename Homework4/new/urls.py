from django.urls import path
from .views import mainpage,coments,author

urlpatterns = [
    path('',mainpage, name='home'),
    path('coments/',coments,name='comment'),
    path('authors/',author, name='authors'),
]