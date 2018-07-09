from rest_framework import serializers

from utils.models import Language, Name


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class NameSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(read_only=True)
    language_id = serializers.PrimaryKeyRelatedField(write_only=True, source='language', queryset=Language.objects.all())

    class Meta:
        model = Name
        fields = '__all__'
