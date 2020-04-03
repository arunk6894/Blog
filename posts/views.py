from django.shortcuts import render, get_object_or_404
from .models import posts

# Create your views here.


def allposts(request):
    post = posts.objects.all
    return render(request, 'posts/allposts.html', {'posts': post})

def detail(request, post_id):
    po = get_object_or_404(posts, pk = post_id)
    return render(request,'posts/detail.html', {'post':po})