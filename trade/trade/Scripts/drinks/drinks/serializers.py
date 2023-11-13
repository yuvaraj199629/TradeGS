# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import Drink
from .models import Party,Payment,Collection

# Create a model serializer
class Drinkserializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = Drink
		fields = ('name','code','item_group','acc','mrp','open_stock','unit','tax','hSN','purchase_rate','retail_rate','ws_rate','qty_rate','bluk_unit','Cess','bulk_qty','cess_price')

class Partyserializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = Party
		fields = ('name','code','phone_no','acc','gst_in','price_type','gst_type')


class Paymentserializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = Payment
		fields = ('payment_id','date','supplier','amount','adj','remark')

class Collectionserializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = Collection
		fields = ('payment_id','date','customer','amount','adj','remark')



