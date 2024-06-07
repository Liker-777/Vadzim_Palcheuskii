from django.urls import path
from . import views


urlpatterns = [
    path('', views.main,),
    path('Cars/', views.show_cars),
    path('About/', views.about),
    path('Contacts/', views.contacts),
    path('Reviews/', views.feedbackView.as_view()),
    path('Reviews/Thanks/', views.ThanksFeedback),
    path('Car/<slug:slug_car>/', views.show_car, name ='name_site_car'),
]