from django.shortcuts import render

def lista_nacionalidades(request):
    nacionalidades = [

        "Portuguesa",
        "Alemã",
        "Espanhola",
        "Brasileira",
        "Moldava",
        "Francesa",
        "Italiana",
    ]

    return render(request, "nacionalidades/lista.html", {
        "nacionalidades": nacionalidades
    })


