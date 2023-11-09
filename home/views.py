
from django.shortcuts import render

def home(request):
    print('HOME')
    
    contexto = {
        'text': 'Olá, estou na Home por uma variavel "contexto"',
        'title': 'HOME | '
    }
    
    return render(
        request,
        template_name='home/index.html',
        context = contexto,
    )
