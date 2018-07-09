from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from utils import views

urlpatterns = [
    path('languages/', views.LanguageList.as_view()),
]

urlpatterns += format_suffix_patterns(urlpatterns)
