from django.shortcuts import render


# Create your views here.

def index(request):
    #passa o codigo html por aqui
    return render(request, "galeria/index.html")

def imagem(request):
    return render(request, "galeria/imagem.html")
