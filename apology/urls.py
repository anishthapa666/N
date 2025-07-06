from django.urls import path
from . import views

urlpatterns = [
    path('', views.letter_view, name='letter'),
    path('home/', views.home, name='home'),
    path('memories/', views.memories, name='memories'),
    path('reasons/', views.reasons, name='reasons'),
    path('forgive/', views.forgive, name='forgive'),
    path('yes/', views.YES, name='yes_page'),
    path('no/', views.NO, name='no_page'),

    path('music_upload/', views.music_upload, name='music_upload'),
]



