from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from places_remember_app.models import Memory
from social_django.models import UserSocialAuth
# Create your views here.


def main(request):
    return render(request, 'index.html', {'user': request.user})


@login_required(login_url='/user/social-auth/login/facebook/')
def memories(request):
    memories = Memory.objects.filter(user=request.user.pk)
    user_social_auth = UserSocialAuth.objects.get(user_id=request.user.pk)
    context = {
        'user': request.user,
        'memories': memories,
        'picture_url': user_social_auth.extra_data['picture']['data']['url'],
    }
    return render(request, 'impressions/memories.html', context)
