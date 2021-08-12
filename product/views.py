from django.shortcuts import render, redirect
from .models import Product
# Create your views here.
def index(request):
    dc = {'data':"I AM FROM INDEX FUNCTION"}
    return render(request,'index.html',dc)

def save_item(request):
    dc ={}
    item = Product(name=request.POST['name'],price=request.POST['price'],description=request.POST['description'],image = request.FILES.get('item_image'))
    dc['Success'] = 'Item has been added'
    return redirect('/')
