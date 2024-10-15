from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from accounts.models import User


@csrf_exempt
def about_us(request):
    if request.method == 'GET':
        if User.objects.all():
            users = User.objects.all()
            context = {
                'users': users
            }
            return render(request, 'about_us.html', context=context)
        return render(request, 'about_us.html', context=None)


