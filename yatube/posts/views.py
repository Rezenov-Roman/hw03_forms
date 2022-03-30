from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


NUMBER10 = 10


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, NUMBER10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'post_list': post_list,
               'page_obj': page_obj,
               }
    template = 'posts/index.html'
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, NUMBER10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'group': group,
               'page_obj': page_obj,
               }
    template = 'posts/group_list.html'
    return render(request, template, context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author__username=username)
    paginator = Paginator(posts, NUMBER10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/profile.html'
    context = {
        'page_obj': page_obj,
        'posts': posts,
        'author': author,
}
    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    template = 'posts/post_detail.html'
    context = {
        'post': post,
    }
    return render(request, template, context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            author = request.user
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:profile', username=author)
        return render(request, 'posts/create_post.html', {'form': form})

    form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author != request.user:
        return redirect(f'/posts/{post_id}/')
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect(f'/posts/{post_id}/')
    context = {
        'post': post,
        'form': form,
        'is_edit': True,
    }
    return render(request, 'posts/create_post.html', context)