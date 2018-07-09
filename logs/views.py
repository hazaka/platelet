from rest_framework import generics

from logs.models import Piece
from logs.serializers import PieceSerializer


class PieceList(generics.ListCreateAPIView):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer


class PieceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer
