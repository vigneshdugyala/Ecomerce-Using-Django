from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from .models import Cart
from django.contrib.auth.models import auth,User
from django.http import HttpResponse


# Create your views here.
def index(request):
    dests= Product.objects.all()
    return render(request,"index.html",{'dests':dests})
def image(request, image_id):
    if request.method=="POST":
        dest = get_object_or_404(Product,pk= image_id)
        y=request.user
        k=Cart.objects.all()
        if Cart.objects.filter(users=y.id,products=image_id).exists() :
             return render(request,"image.html",{'dest':dest})
        else:
            z=Cart(users=y.id , products=image_id)
            z.save()
            return render(request,"image.html",{'dest':dest})
           
    else:
        dest = get_object_or_404(Product,pk= image_id)
        return render(request,"image.html",{'dest':dest})
def cartt(request):
    if request.method=="POST":
        w=request.user
        k=int(request.POST['keyy'])
        zzz=get_object_or_404(Cart,users=w.id , products=k)
        zzz.delete()
        return redirect("cartt")
    else:
        if Cart.objects.filter(users=request.user.id).exists():
            c= Cart.objects.filter(users=request.user.id)
            l=[]
            for i in c:
                az=i.products
                dest = get_object_or_404(Product,pk= az)
                l.append(dest)
            return render(request,"cart.html",{'l':l})
        else:
            return render(request,"nocart.html")
def book(request):
    if request.method=="POST":
        return render(request,"ordered.html")
    return render(request,"book.html")
    
   
