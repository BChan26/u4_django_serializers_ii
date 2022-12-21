from rest_framework import serializers
from .models import User, Book, Review
class UserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name = 'review_detail',
        many = True,
        read_only = True
    )
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'reviews')

        
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(
        view_name = 'user_detail',
        read_only = True
    )
    books = serializers.HyperlinkedRelatedField(
        view_name = 'book_detail',
        read_only = True
    )
    class Meta:
        model = Review
        fields = ('id', 'name', 'title', 'body', 'books', 'users', "rating")
class BookSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(
        many = True,
        read_only = True
    )
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'summary', 'price', 'reviews', 'photo_url')