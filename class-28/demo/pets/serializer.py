from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pet
        fields = ('name', 'owner', 'des', 'breed', 'birth_date')