from django.urls import path
from . import views

urlpatterns = [
    path('vote/<int:review_id>/', views.vote_review, name='vote_review'),
]
