
from django.shortcuts import render,redirect
# from django.contrib.auth.models import user
# from .models import Contact
from .models import Food_details
def index(request):

    return render(request,"fd.html")
   

def fdnw(request):
     return render(request,"fdnw.html")

def view(request):
     data=Food_details.objects.all()
     return render(request,"view.html",{'data':data})



def Adddata(request):
    if request.method=="POST":
        item=request.POST['item']
        price=request.POST['price']
        contact=request.POST['Contact']
        address=request.POST['address']
        hotelname=request.POST['hotelname']
        rating=request.POST['rating']
        add=Food_details(Item=item,Price=price,Contact=contact,Address=address,Hotelname=hotelname,Rating=rating)
        add.save()
        return redirect('view')
    return render(request,"fdnw.html")

# 

def formupdate(request,id):
    if request.method=="POST":
        add=Food_details.objects.get(id=id)
        add.Hotelname=request.POST['hotelname']
        add.Rating=request.POST['rating']
        add.Item=request.POST['item']
        add.Price=request.POST['price']
        add.Contact=request.POST['Contact']
        add.Address=request.POST['address']
        add.save()
        return redirect("view")

def edit(request,id):
    Data=Food_details.objects.get(id=id)
    return render(request,'edit.html',{'Data':Data})

def delete(request,id):
    add=Food_details.objects.get(id=id)
    add.delete()
    return redirect('view')