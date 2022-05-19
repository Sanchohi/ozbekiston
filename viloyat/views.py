from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
	return render(request,'viloyat/index.html')

def region(request):
	viloyat = Viloyat.objects.all()
	
		
	return render(request,'viloyat/viloyat.html',{'viloyat':viloyat})

def rayon(request,pk):
	rayon = Rayon.objects.filter(cat_id=pk)
	malum = Umumiy.objects.filter(cat_id=pk)
	viloyat = Viloyat.objects.all()
	return render(request,'viloyat/rayon.html',{'viloyat':viloyat,'rayon':rayon,'malum':malum,'r':1})

def korinish(request):
	return render(request,'viloyat/korinish.html')


def oqish(request,pk):
	rayon = Rayon.objects.filter(pk=pk)
	viloyat = Viloyat.objects.all()
	if pk>14:
		pk = 1

	
	return render(request,'viloyat/oqi.html',{'viloyat':viloyat,'rayon':rayon,'a':pk})

def yarat(request):
	return render(request,'viloyat/umidjon.html')

