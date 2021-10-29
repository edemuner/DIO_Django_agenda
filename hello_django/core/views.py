from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome}!</h1> a idade informada é {idade}')

def soma(request, num1, num2):
    return HttpResponse(num1 + num2)

def subtracao(request, num1, num2):
    return HttpResponse(num1 - num2)

def multiplicacao(request, num1, num2):
    return HttpResponse(num1 * num2)

def divisao(request, num1, num2):
    if num2 != 0:
        return HttpResponse(num1 / num2)
    else:
        return HttpResponse('Impossível dividir por zero!')
