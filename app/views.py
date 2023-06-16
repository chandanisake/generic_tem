from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'bhavi','age':1}
    return render(request,'wish.html',context=d)

