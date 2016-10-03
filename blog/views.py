from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def show_post(request,post_id):
    posts = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post.html',{'posts':posts})