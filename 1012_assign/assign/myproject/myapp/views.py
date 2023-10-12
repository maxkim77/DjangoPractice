from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html')

@login_required
def notice(request):
    return render(request, 'notice.html')

@login_required
def blog(request):
    if request.method == 'POST':
        pass
    return render(request, 'blog.html')

@login_required
def blog_create(request):
    return render(request, 'blog_create.html')

@login_required
def blog_update(request, pk):
    return render(request, 'blog_update.html')

@login_required
def blog_delete(request, pk):
    return render(request, 'blog_delete.html')

@login_required
def profile(request, pk):
    return render(request, 'profile.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/blog/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # 로그인 페이지로 리디렉션
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
