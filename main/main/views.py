from django.shortcuts import render 
from . core import pumk 
class Containeer:
     movie : str
     poster : str 
     type1  : str 
def result(request):
    if(request.method =='POST'):
        x = request.POST["movie"]
        movies  = pumk(x)
    return render(request ,'result.html',movies)

def main(request):
    return render(request ,'index.html' )

def base(request):
    return render(request , 'base.html')
def blog(request):
        return render(request , 'blog.html') 
def cofee(request): 
    return render(request , 'coffees.html' )