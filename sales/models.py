from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
#from addons.log_fetch import recentPcode




# Create your models here.

class Product (models.Model) : 
    id = models.AutoField(primary_key = True)
    pcode = models.CharField(max_length = 10, unique = True, null = True)
    pname = models.TextField()
    jang = models.TextField()
    ptime = models.IntegerField(default = 0)
    unitprice = models.IntegerField(default = 0)
    discountrate = models.DecimalField(max_digits = 11, decimal_places = 2, default = 0)
    img_file = models.ImageField(null = True, blank = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    create_date = models.DateTimeField(null = True, blank = True)
    
    class Meta :
        unique_together = (("id", "pcode"),)
    
    #def publish(self) : 
    #    self.published_date = datetime.now()
    #    self.save()
    
    def __str__(self) :
        return self.pcode + " | " + self.pname + " | " + self.jang + " | "+str(self.ptime) + " | " + str(self.unitprice) + " | " + str(self.discountrate)
    
class Sales (models.Model) : 
    #scode = models.ForeignKey(Product, on_delete = models.SET(Product.objects.get()), to_field = "pcode")
    scode = models.CharField(max_length = 10, null = True)
    sdate = models.DateTimeField(null = True, blank = True)
    qty = models.IntegerField(default = 0)
    amt = models.IntegerField(default = 0)
    