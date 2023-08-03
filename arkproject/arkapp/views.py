from django.shortcuts import render,redirect
from .models import Product
from math import ceil
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'index.html')



def purchase(request):
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n // 4 + ceil((n /4 ) - (n // 4))
        allProds.append([prod,range(1, nSlides), nSlides])

    params={'allProds':allProds}
    return render(request,"purchase.html",params)

def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Login & try Again')
        return redirect('/arkauth/login')
    return render(request,'checkout.html')
    