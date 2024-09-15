from django.http import HttpResponse
from django.shortcuts import render ,redirect
from .models import product
from .models import Catagory
from .forms import ProductForm

def home(request):
    return render(request,'shop/index.html')

def homepage(request ,id=None):
    catagories = Catagory.objects.order_by('name')
    filter = request.GET.get('Search','')
    if filter !="":
        Poduct = product.objects.filter(name__icontains=filter).order_by('name')
        return render(request,'shop/homepage.html' ,{'Poduct':Poduct ,'catagories':catagories ,'filters':filter})
    
    if id is None:
        Poduct = product.objects.all()
        return render(request,'shop/homepage.html' ,{'Poduct':Poduct ,'catagories':catagories})
    else:
        Poduct = product.objects.filter(catagory_id=id)
        return render(request,'shop/homepage.html' ,{'Poduct':Poduct ,'catagories':catagories})
    # Poduct = product.objects.order_by('name')
    # return render(request,'shop/homepage.html' ,{'Poduct':Poduct ,'catagories':catagories})

def product_detail(request,id):
    catagories = Catagory.objects.order_by('name')
    products = product.objects.get(id=id)
    return render(request,'shop/product_detail.html' ,{'product':products ,'catagories':catagories})




def update(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    catagory = Catagory.objects.all()
    return render(request, 'shop/product_update.html', {'form': form ,'catagories': catagory})
