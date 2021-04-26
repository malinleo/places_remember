from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from places_remember_app.models import Memory
from .forms import MemoryForm
from social_django.models import UserSocialAuth


# Create your views here.


def render_main(request):
    if request.method == 'GET':
        try:
            user_social_auth = UserSocialAuth.objects.get(user_id=request.user.pk)
        except UserSocialAuth.DoesNotExist:
            user_social_auth = None
        if user_social_auth is not None:
            context = {
                'user': request.user,
                'picture_url': user_social_auth.extra_data['picture']['data']['url']
                if user_social_auth.provider == 'facebook' else user_social_auth.extra_data['photo_big']
            }
            return render(request, 'index.html', context)
        return render(request, 'index.html', {'user': request.user})


@login_required(login_url='/user/social-auth/login/facebook/')
def render_memories(request):
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
        return render(request, 'memories/memories.html', context)


@login_required(login_url='/user/social-auth/login/facebook/')
def add_memory(request):
    if request.method == 'POST':
        memory_form = MemoryForm(request.POST, request.FILES)
        if memory_form.is_valid():
            memory_form.cleaned_data['user'] = request.user
            Memory.objects.create(**memory_form.cleaned_data)
        return redirect('memories')
    else:
        memory_form = MemoryForm()
        user_social_auth = UserSocialAuth.objects.get(user_id=request.user.pk)
        context = {
            'form': memory_form,
            'picture_url': user_social_auth.extra_data['picture']['data']['url']
            if user_social_auth.provider == 'facebook' else user_social_auth.extra_data['photo_big']
        }
        return render(request, 'memories/add_memory.html', context)


@login_required(login_url='/user/social-auth/login/facebook/')
def change_memory(request, pk):
    memory = get_object_or_404(Memory, pk=pk)
    if request.method == 'POST':
        memory_form = MemoryForm(request.POST, request.FILES)
        if memory_form.is_valid():
            print(memory_form.cleaned_data)
            for key, value in memory_form.cleaned_data.items():
                setattr(memory, key, value)
            memory.save()
        return redirect('memories')
    else:
        user_social_auth = UserSocialAuth.objects.get(user_id=request.user.pk)
        # memory_form_initial = {field.__str__().split('.')[-1]: field.value_from_object(memory)
        #                        for field in memory._meta.fields}
        memory_form = MemoryForm(instance=memory)
        context = {
            'memory_id': memory.pk,
            'form': memory_form,
            'picture_url': user_social_auth.extra_data['picture']['data']['url']
            if user_social_auth.provider == 'facebook' else user_social_auth.extra_data['photo_big']
        }
        return render(request, 'memories/change_memory.html', context)


def delete_memory(request, pk):
    if request.method == 'POST':
        Memory.objects.get(pk=pk).delete()
    return redirect('memories')

