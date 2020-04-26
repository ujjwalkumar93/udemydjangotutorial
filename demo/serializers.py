from rest_framework import serializers
from .models import Book, BookNumber, Charecter, Auther
class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id','isbn_13','isbn_10']
class CharecterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charecter
        fields = ['id','name']

class AutherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auther
        fields = ['id','name']


class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many = False)
    char = CharecterSerializer(many = True)
    authname = AutherSerializer(many = True)
    class Meta:
        model = Book
        fields = ['id','title','discription','char','number','authname']
