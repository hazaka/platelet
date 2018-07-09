from rest_framework import serializers

from utils.models import Language, Name


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = '__all__'
