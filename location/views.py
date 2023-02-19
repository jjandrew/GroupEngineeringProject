from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

   x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

   if x_forwarded_for:

       ip = x_forwarded_for.split(',')[0]

   else:

       ip = request.META.get('REMOTE_ADDR')

  

   return HttpResponse("Welcome to the home page. \
   IP address: {}".format(ip))