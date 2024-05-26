from django.shortcuts import render

def blank(request):
    return render(request,'blank.html')