from django.shortcuts import render

# Create your views here.
def bussiness_user(request):
    return render(request, 'bussiness_user/bussiness_user.html', {})
