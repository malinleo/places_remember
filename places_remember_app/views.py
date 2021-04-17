from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from places_remember_app.models import Memory
# Create your views here.


def main(request):
    return render(request, 'index.html', {'user': request.user})


@login_required(login_url='/user/social-auth/login/facebook/')
def memories(request):
    memories = Memory.objects.filter(user=request.user)
    context = {
        'user': request.user,
        'memories': memories
    }
    return render(request, 'impressions/memories.html', context)
