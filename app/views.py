from django.shortcuts import render

# Create your views here.

def condition(request):
    d={'a':66123,'b':225,'c':2388}
    return render(request,'condition.html',d)