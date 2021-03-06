from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from utils import views

urlpatterns = [
    path('languages/', views.LanguageList.as_view()),
    path('languages/<int:pk>/', views.LanguageDetail.as_view()),

    path('names/', views.NameList.as_view()),
    path('names/<int:pk>/', views.NameDetail.as_view()),
]

urlpatterns += format_suffix_patterns(urlpatterns)
