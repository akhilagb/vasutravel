from . import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    # path('add/',views.addition,name='addition')
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
    # path('detail/',views.detail,name='detail'),
    # path('thanks/',views.thanks,name='thanks')
]