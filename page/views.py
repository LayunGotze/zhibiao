from django.shortcuts import render

# Create your views here.
def world_map(request):
    return render(request,'geo.html')

def time_line(request):
    return render(request,'time.html')