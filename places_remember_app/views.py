from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from places_remember_app.models import Memory
from social_django.models import UserSocialAuth


# Create your views here.


def main(request):
    if request.method == 'GET':
        try:
            user_social_auth = UserSocialAuth.objects.get(user_id=request.user.pk)
        except UserSocialAuth.DoesNotExist:
            user_social_auth = None
        print(user_social_auth)
        if user_social_auth is not None:
            context = {
                'user': request.user,
                'picture_url': user_social_auth.extra_data['picture']['data']['url']
                if user_social_auth.provider == 'facebook' else user_social_auth.extra_data['photo_big']
            }
            return render(request, 'index.html', context)
        return render(request, 'index.html', {'user': request.user})


@login_required(login_url='/user/social-auth/login/facebook/')
def memories(request):
    if request.method == 'POST':
        pass
    else:
        memories = Memory.objects.filter(user=request.user.pk)
        user_social_auth = UserSocialAuth.objects.get(user_id=request.user.pk)
        context = {
            'user': request.user,
            'memories': memories,
            'picture_url': user_social_auth.extra_data['picture']['data']['url']
            if user_social_auth.provider == 'facebook' else user_social_auth.extra_data['photo_big']
        }
        return render(request, 'impressions/memories.html', context)
