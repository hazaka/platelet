from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from logs import views

urlpatterns = [
    path('pieces/', views.PieceList.as_view()),
    path('pieces/<int:pk>/', views.PieceDetail.as_view()),
]

urlpatterns += format_suffix_patterns(urlpatterns)
