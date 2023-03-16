from django.shortcuts import render

# Create your views here.
def brook(request):
    return render(request,'brook.html')