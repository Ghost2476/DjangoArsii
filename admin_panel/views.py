from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from accounts.models import CustomUser
from accounts.decorators import admin_required

@admin_required
def dashboard_view(request):
    stats = {
        'total_users':  CustomUser.objects.filter(role='user').count(),
        'total_admins': CustomUser.objects.filter(role='admin').count(),
        'total':        CustomUser.objects.count(),
    }
    return render(request, 'admin_panel/dashboard.html', {'stats': stats})

@admin_required
def users_list_view(request):
    q     = request.GET.get('q', '')
    users = CustomUser.objects.filter(username__icontains=q) if q else CustomUser.objects.all()
    return render(request, 'admin_panel/users_list.html', {'users': users, 'q': q})

@admin_required
def user_detail_view(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'toggle_role':
            user.role = 'admin' if user.role == 'user' else 'user'
            user.save()
            messages.success(request, f"{user.username}'s role updated.")
        elif action == 'delete':
            user.delete()
            messages.warning(request, 'User deleted.')
            return redirect('admin_users')
        return redirect('admin_user_detail', pk=pk)
    return render(request, 'admin_panel/user_detail.html', {'u': user})
