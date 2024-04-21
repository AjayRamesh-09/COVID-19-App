from django.shortcuts import render

def home(request):
    return render(request,'arogya/home.html')
def vaccine(request):
    return render(request,'arogya/vaccine.html')
