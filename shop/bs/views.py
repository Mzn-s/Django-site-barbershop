from django.shortcuts import render



def views1(request):
  return render(request, 'bs/index.html')
