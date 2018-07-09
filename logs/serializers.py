from collections import OrderedDict
from typing import List

from rest_framework import serializers

from logs.models import Piece, Log, Watch
from utils.models import Name
from utils.serializers import NameSerializer


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'


class WatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        fields = '__all__'


class PieceSerializer(serializers.ModelSerializer):
    titles = NameSerializer(many=True)

    class Meta:
        model = Piece
        fields = '__all__'

    def validate_titles(self, titles: List[OrderedDict]):
        if not titles:
            raise serializers.ValidationError('There should be at least one title.')

        return titles

    def create(self, validated_data: OrderedDict):
        titles_data = validated_data.pop('titles')
        piece = Piece.objects.create(**validated_data)
        for title_data in titles_data:
            piece.titles.add(Name.objects.create(**title_data))
        return piece
