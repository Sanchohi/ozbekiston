from django.db import models

# Create your models here.

class Viloyat(models.Model):
	name = models.CharField(max_length=355)
	slug = models.SlugField(max_length=355)
	
	

	def __str__(self):
		return self.name

class Rayon(models.Model):
	name = models.CharField(max_length=355)
	slug = models.SlugField(max_length=355)
	aholi = models.BigIntegerField(default=0)
	content = models.TextField(blank=True)
	cat = models.ForeignKey(Viloyat,on_delete=models.PROTECT,null=True)

	def __str__(self):
		return self.name

class Umumiy(models.Model):
	name = models.CharField(max_length=355)
	content = models.TextField(blank=True)
	slug = models.SlugField(max_length=355)
	img = models.ImageField(upload_to='photos/%Y/%m/%d/')
	aholi = models.BigIntegerField(default=0)
	cat = models.ForeignKey(Viloyat,on_delete=models.PROTECT,null=True)
	def __str__(self):
		return self.name