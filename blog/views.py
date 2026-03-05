from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post
from .filters import PostFilter

# Create your views here.


def blog(request):
    posts = Post.objects.all()
    
    #Filter
    myfilter = PostFilter(request.GET, queryset=posts)
    posts = myfilter.qs
    paginator = Paginator(posts,2 ) # Show 3 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    return render(request, 'blog/blog.html', {'page_obj': page_obj, 'posts': page_obj, 'myfilter': myfilter})