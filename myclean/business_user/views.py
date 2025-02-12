from django.shortcuts import render

# Create your views here.
def business_user(request):
    return render(request, 'business_user/business_user.html', {})
