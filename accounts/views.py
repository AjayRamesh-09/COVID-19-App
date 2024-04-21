from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import http.client
import requests
import json
from . import views
import joblib

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'USERNAME HAS ALREADY BEEN TAKEN'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('covid')
        else:
            return render(request, 'accounts/signup.html', {'error':'PASSWORDS MUST MATCH'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('covid')
        else:
            return render(request, 'accounts/login.html',{'error':'USERNAME OR PASSWORD IS INCORRECT'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def statistics(request):
    return render(request,'accounts/statistics.html')

def vaccine(request):
    return render(request,'accounts/vaccine.html')

def covid(request):
    return render(request,'accounts/covid.html')

def result(request):

    cls=joblib.load('finalized_model.sav')
    lis=[]
    cough=request.GET['cough']
    fever=request.GET['fever']
    sore=request.GET['sore']
    short=request.GET['short']
    head=request.GET['head']
    
    if cough=="YES":
        lis.append(1)
    elif cough=="NO":
        lis.append(0)
    
    if fever=="YES":
        lis.append(1)
    elif fever=="NO":
        lis.append(0)
    
    if sore=="YES":
        lis.append(1)
    elif sore=="NO":
        lis.append(0)
    
    if short=="YES":
        lis.append(1)
    elif short=="NO":
        lis.append(0)
    
    if head=="YES":
        lis.append(1)
    elif head=="NO":
        lis.append(0)
    
    data=request.GET['number']
    ans=cls.predict([lis])
    string=""
    if(ans[0]==0):

        string="THE PROBABILITY THAT YOU HAVE CONTRACTED THE VIRUS IS LOW.PLEASE MAINTAIN SOCIAL DISTANCING AND FOLLOW OTHER covid-19 PROTOCOLS.GET VACCINATED AS SOON AS POSSIBLE!!"
        color="color:green"
    
    else:
        
        string="PLEASE VISIT THE NEARBY HOSPITAL AND TAKE A covid-19 TEST IMMEDIATELY.STAY SAFE !!"
        color="color:red"
    
  

    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization":"Your ID","sender_id":"Sender ID","message":string,"route":"v3","numbers":data}

    headers = {
    'cache-control': "no-cache"
    }   

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    return render(request,'accounts/result.html',{"ans":string,"color":color})

