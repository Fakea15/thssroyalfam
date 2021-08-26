from django.urls import path
from . import views
from .views import CommentView

urlpatterns = [
    path('', views.homeView, name='home'),
    path('contact_puipate/', views.contact, name='contact'),
    path('about_royal_family/', views.about_page, name='about'),
    path('thlalak_of_royal_families/', views.thlalak, name='thlalak-page'),
    path('comments/', CommentView.as_view(), name='comment'),
    path('i_comment_ta/', views.successful, name='success')
]


