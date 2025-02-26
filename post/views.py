from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all() # .order_by('-created_at')[:5]
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'postDetail.html', {'post': post})