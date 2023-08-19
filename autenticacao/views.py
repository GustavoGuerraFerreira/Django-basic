from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
        nome = 'Gustavo'
        idade = 20
        profissao = 'Engenheiro'
        dic ={'nome': nome, 'idade' : idade, "profissao" : profissao}
        return render(request, 'cadastro/index.html', {'nome': nome, 'idade' : idade, "profissao" : profissao})
