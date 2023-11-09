from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import HttpRequest, Http404

def blog(request):
    print('blog')
    
    contexto = {
        'text': 'Olá, estou no BLOG',
        'title': 'Pagina BLOG | ',
        'posts': posts
    }
    
    return render(
        request=request,
        template_name='blog/index.html',
        context = contexto,
    )

def exemplo(request):
    print('exemplo')
    
    contexto = {
        'text': 'Olá, estou no EXEMPLO',
        'title': 'Pagina EXEMPLO | '
    }
    
    return render(
        request=request,
        template_name='blog/exemplo.html',
        context = contexto
    )
    

def post(request: HttpRequest , post_id: int):
    print('post', post_id)
    
    found_post: dict[str, Any] | None = None
    
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
        
    if found_post is None:
        raise Http404('Post não existe')
    
    contexto = {
        'text': 'Olá, estou no BLOG',
        'title': found_post['title'] + ' - ',
        'post': found_post
    }
    
    return render(
        request=request,
        template_name='blog/post.html',
        context = contexto,
    )