from django.db import models
from django.urls import reverse

class Catlog(models.Model):
    title=models.CharField(max_length=100)
    category=models.SlugField(max_length=200,unique=True)


    def __str__(self):
        return "title: "+self.title+" Catlog: "+self.category

class Product(models.Model):
    cat_id=models.ForeignKey(Catlog,on_delete=models.CASCADE)
    ptitle=models.CharField(max_length=100)
    discrip=models.TextField(max_length=1000)
    price=models.DecimalField(default=0,max_digits=12,decimal_places=4)
    act_price=models.DecimalField(default=0,max_digits=12,decimal_places=4)
    color=models.CharField(max_length=50)
    size=models.CharField(max_length=50)
    image=models.FileField(upload_to="static/image")
    brand=models.CharField(max_length=100)
    rating=models.DecimalField(decimal_places=1,max_digits=2,default=0)
    review=models.TextField(max_length=400)
    def get_absolute_url(self):
        return reverse("Store:detail",kwargs={"menu":self.cat_id.category})

    def __str__(self):
        return "Product: "+self.ptitle +" Brand: "+self.brand