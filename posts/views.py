from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})    # renders the index.html file

def post(request, pk):
    posts = Post.objects.get(id=pk)  # assigns pk = post object id
    return render(request, 'posts.html', {'posts': posts})
