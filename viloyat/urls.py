from django.urls import path
from .views import *

urlpatterns = [
	path('',home,name='home'),
	path('viloyat/',region,name='viloyat'),
	path('rayon/<int:pk>/',rayon,name='rayon'),
	path('korinish/',korinish,name='kor'),
	path('oqish/<int:pk>/',oqish,name='oqish'),
	path('saytmuallifi/',yarat,name='yarat')
	


]