from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from django.db.models import Q
from rest_framework import generics
from .serializers import GameSerializer

# Start Controller Game
# Class GameList untuk menambah dan menampilkan seluruh data
class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all().order_by('id')
    serializer_class = GameSerializer

# Class GameDetail untuk mengubah, menghapus dan menampilkan data
# berdasarkan id
class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all().order_by('id')
    serializer_class = GameSerializer

# Class GameListAPIView untuk mencari data berdasarkan name
class GameListAPIView(generics.ListAPIView):
    serializer_class = GameSerializer

    def get_queryset(self, *args, **kwargs):
        query_list = Game.objects.all().order_by('id')
        query = self.request.GET.get('q')
        if query:
            query_list = query_list.filter(
                Q(name__icontains = query)
            ).distinct()
        return query_list
# End Controller Game

