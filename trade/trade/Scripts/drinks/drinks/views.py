from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import Drinkserializer
from .serializers import Partyserializer,Partyserializer,Collectionserializer
from .models import Drink
from .models import Party,Payment,Collection
from rest_framework.response import Response
from rest_framework import status

# create a viewset

@api_view (['GET', 'POST'])
def drink_list(request):
	# define queryset
	
	# specify serializer to be used
	if request.method== 'GET':

		drinks= Drink.objects.all()


		serializer = Drinkserializer(drinks, many= True);
		return JsonResponse({"drinks": serializer.data,"coun":4},safe=False)

	if request.method == 'POST':
		serializer= Drinkserializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

@api_view (['GET','PUT','DELETE'])
def drink_detail(request, id):
	drink = Drink.objects.get(pk=id)
	# try: 
	# 	drink = Drinks.object.all(pk=id)
	# except Drinks.DoesNotExit:
	# 	return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer= Drinkserializer(drink)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer= Drinkserializer(drink, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		drink.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# for filter start
@api_view (['GET', 'POST'])
def filter_product(request,data):
	if request.method == 'GET':
		drinks= Drink.objects.all()
		drinks=drinks.filter(open_stock=data)
		serializer = Drinkserializer(drinks, many= True);
		return JsonResponse({"drinks": serializer.data,"coun":4},safe=False)
# for filter end




@api_view (['GET', 'POST'])
def party_list(request):
	# define queryset
	
	# specify serializer to be used
	if request.method== 'GET':

		party= Party.objects.all()

		serializer = Partyserializer(party, many= True);
		return JsonResponse({"party": serializer.data,"coun":4},safe=False)

	if request.method == 'POST':
		serializer= Partyserializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)


@api_view (['GET', 'POST'])
def payment_list(request):
	# define queryset
	
	# specify serializer to be used
	if request.method== 'GET':

		payment= Payment.objects.all()

		serializer = Paymentserializer(payment, many= True);
		return JsonResponse({"payment": serializer.data,"coun":4},safe=False)

	if request.method == 'POST':
		serializer= Paymentserializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)


@api_view (['GET', 'POST'])
def collection_list(request):
	# define queryset
	
	# specify serializer to be used
	if request.method== 'GET':

		collection= Collection.objects.all()

		serializer = Collectionserializer(payment, many= True);
		return JsonResponse({"collection": serializer.data,"coun":4},safe=False)

	if request.method == 'POST':
		serializer= Collectionserializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)




