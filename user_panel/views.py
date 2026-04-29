from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm, SettingsForm
from .models import Profile

@login_required
def home_view(request):
    return render(request, 'user_panel/home.html')

@login_required
def profile_view(request):
    form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('user_profile')
    return render(request, 'user_panel/profile.html', {'form': form})

@login_required
def settings_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    form = SettingsForm(request.POST or None, instance=profile)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Settings saved!')
        return redirect('user_settings')
    return render(request, 'user_panel/settings.html', {'form': form})
