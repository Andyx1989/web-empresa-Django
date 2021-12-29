from django.shortcuts import get_object_or_404, render
from .models import Category, Post
# Create your views here.
def Posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

def category(request, category_id):
    category = get_object_or_404(Category, id = category_id)
    return render(request, 'blog/category.html', {'category': category})
    
