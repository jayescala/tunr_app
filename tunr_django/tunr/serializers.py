from rest_framework import serializers
from .models import Artist, Song

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'nationality', 'photo_url', 'songs')

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'artist', 'title', 'album', 'preview_url')
