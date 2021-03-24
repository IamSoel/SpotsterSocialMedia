from django.shortcuts import render
from home.models import registration
# Create your views here.

def hottopic(request):
    email = request.session['email']
    user = registration.objects.filter(email=email)
    return render(request, 'hottopic.html',{'email':email, 'user':user})