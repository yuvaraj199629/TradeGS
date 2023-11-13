# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import Drink

# Create a model serializer
class Drinkserializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = Drink
		fields = ('name','description')
