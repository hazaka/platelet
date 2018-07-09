from rest_framework import generics

from utils.models import Language
from utils.serializers import LanguageSerializer


class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
