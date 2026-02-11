from django.shortcuts import render, get_object_or_404
from .models import Post

def post_details(request, pk):
    # Retrieve the specific post by its primary key (pk)
    # or return a 404 error if it's not found
    post = get_object_or_404(Post, pk=pk)
    
    context = {
        'post': post,
    }
    
    return render(request, 'blog_app/post_details.html', context)