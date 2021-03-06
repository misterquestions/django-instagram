from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from posts.forms import CreatePostForm

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

@login_required
def list_posts(request):
    """List existing posts"""
    return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def create_post(request):
    """Creates a new post"""
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('feed')

    else:
        form = CreatePostForm()

    return render(
        request,
        'posts/create.html',
        {
            'form': form,
            'user': request.user,
            'profile': request.user.profile,
        }
    )
