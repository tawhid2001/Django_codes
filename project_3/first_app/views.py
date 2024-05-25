from django.shortcuts import render

# Create your views here.

def home(request):
    d = {'author':'Rahim','age':20,'lst':[1,2,3],'courses':[
        {
            'id':1,
            'name':'python',
            'fee':1000
        },
        {
            'id':2,
            'name':'django',
            'fee':10000
        },
        {
            'id':3,
            'name':'c',
            'fee':1500
        },
    ]}
    return render(request,'first_app/home.html',d)