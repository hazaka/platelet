from rest_framework import generics

from utils.models import Language, Name
from utils.serializers import LanguageSerializer, NameSerializer


class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class NameList(generics.ListCreateAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer


class NameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer
