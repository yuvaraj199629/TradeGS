from django.db import models

# Create your models here.

class Drink(models.Model):
	name= models.CharField(max_length=200)
	code= models.CharField(max_length=200)
	item_group= models.CharField(max_length=200)
	acc = models.CharField(max_length=200)
	mrp= models.CharField(max_length=200)
	open_stock = models.CharField(max_length=200)
	unit= models.CharField(max_length=200)
	tax=models.CharField(max_length=200)
	hSN= models.CharField(max_length=200)
	purchase_rate=models.CharField(max_length=200)
	retail_rate= models.CharField(max_length=200)
	ws_rate= models.CharField(max_length=200)
	qty_rate= models.CharField(max_length=200)
	bluk_unit= models.CharField(max_length=200)
	Cess=models.CharField(max_length=200)
	bulk_qty=models.CharField(max_length=200)
	cess_price=models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Party(models.Model):
    name= models.CharField(max_length=200)
    code= models.CharField(max_length=200)
    phone_no= models.CharField(max_length=200)
    acc = models.CharField(max_length=200)
    gst_in= models.CharField(max_length=200)
    price_type = models.CharField(max_length=200)
    gst_type= models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Payment(models.Model):
    payment_id= models.CharField(max_length=200)
    date= models.CharField(max_length=200)
    supplier= models.CharField(max_length=200)
    amount= models.CharField(max_length=200)
    adj = models.CharField(max_length=200)
    remark= models.CharField(max_length=200)
    

    def __str__(self):
        return self.payment_id

class Collection(models.Model):
    collection_id= models.CharField(max_length=200)
    date= models.CharField(max_length=200)
    customer= models.CharField(max_length=200)
    amount= models.CharField(max_length=200)
    adj = models.CharField(max_length=200)
    remark= models.CharField(max_length=200)
    

    def __str__(self):
        return self.collection_id






