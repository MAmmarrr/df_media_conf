from django.shortcuts import render, redirect
from .models import NewProduct
# Create your views here.
def index(request):
    dc = {'data':"I AM FROM INDEX FUNCTION"}
    return render(request,'index.html',dc)

def save_item(request):
    dc ={}
    if request.method=='POST':
        item = NewProduct(name=request.POST['name'],price=request.POST['price'],description=request.POST['description'],image = request.FILES.get('item_image'))
        item.save()
        dc['Success'] = 'Item has been added'
    return redirect('/')
