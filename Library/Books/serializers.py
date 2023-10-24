from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    rarity_level = serializers.SerializerMethodField()

    book_info = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
     )
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'book_info', 'authors', 'publication_house', 'publication_date', 'rarity_level']
        #read_only_fields = ['title']
        #This is an example of read_only_fields.
        #It stops 'title' from appearing when sending the serialized book as a response
        #Therefore, I'm leaving it as a comment
    
    def get_rarity_level(self, obj):
        if obj.publication_date.year > 2010:
            return "Common"
        elif obj.publication_date.year > 2000:
            return "Uncommon"
        else:
            return "Rare"
    

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

    