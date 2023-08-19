from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
        pessoa = [{'nome':  'Gustavo', 'idade' : 20, "profissao" : 'Engenheiro'},
                  {'nome':  'João', 'idade' : 22, "profissao" : 'Médico'}]
       
        return render(request, 'cadastro/index.html', {'pessoas': pessoa, "x" : 1})
