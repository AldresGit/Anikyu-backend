from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from anikyu_api.models import Anime, User
from django.contrib.auth.hashers import make_password

class AnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anime
        fields = ('id', 'title', 'slug', 'description', 'poster_image', 'background_image', 'categories', 'rating', 'start_date')

    def create(self, validated_data):
        return Anime.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.description = validated_data.get('description', instance.description)
        instance.poster_image = validated_data.get('poster_image', instance.poster_image)
        instance.background_image = validated_data.get('background_image', instance.background_image)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.start_date = validated_data.get('start_date', instance.start_date)

        instance.save()

        return instance


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    watched_animes = AnimeSerializer(many=True)
    wanted_animes = AnimeSerializer(many=True)
    unwanted_animes = AnimeSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'anime_count', 'watched_animes', 'wanted_animes', 'unwanted_animes']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', make_password(instance.password))
        instance.anime_count = validated_data.get('anime_count', instance.anime_count)

        watched_animes = validated_data.get('watched_animes', instance.watched_animes)
        wanted_animes = validated_data.get('wanted_animes', instance.wanted_animes)
        unwanted_animes = validated_data.get('unwanted_animes', instance.unwanted_animes)

        instance.save()

        return instance

    def addAnimeToList(self, instance, data):
        selected_anime = searchAnimeInLocalDB(data.pop('selected_anime'))
        selected_list = data.pop('selected_list')
        instance.anime_count = (instance.anime_count + 1)
        if selected_list == 'watched':
            instance.watched_animes = instance.watched_animes.add(selected_anime)
        if selected_list == 'wanted':
            instance.wanted_animes = instance.wanted_animes.add(selected_anime)
        if selected_list == 'unwanted':
            instance.unwanted_animes = instance.unwanted_animes.add(selected_anime)

        instance.save()

        return instance

    def removeAnimeFromList(self, instance, data):
        selected_anime = data.pop('selected_anime')
        selected_list = data.pop('discarted_list')
        instance.anime_count = (instance.anime_count - 1)
        if selected_list == 'watched':
            instance.watched_animes = instance.watched_animes.remove(selected_anime)
        if selected_list == 'wanted':
            instance.wanted_animes = instance.wanted_animes.remove(selected_anime)
        if selected_list == 'unwanted':
            instance.unwanted_animes = instance.unwanted_animes.remove(selected_anime)

        instance.save()

        return instance

    def moveAnimeToList(self, instance, add_data, remove_data):
        self.removeAnimeFromList(self, instance, remove_data)
        self.addAnimeToList(self, instance, add_data)

    def searchAnimeInLocalDB(self, selected_anime):
        if Anime.objects.filter(**selected_anime).exists():
            return selected_anime

        return Anime.objects.create(**selected_anime)
