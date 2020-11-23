from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import student

def home(request):
    return render(request,"Pages/home.html")

@csrf_exempt
def form(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        if student.objects.filter(phone__iexact=phone):
            messages.error(request,"Your record already stored.")
        else:
            student(fname = fname,lname = lname,address = address,email = email,phone = phone).save()
            messages.success(request,"Your record has successfully saved!")
        return redirect("/")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")