from django.shortcuts import render
from django.http import JsonResponse
import threading
import time

# Variável de controle global (apenas para simulação)
nivel = 0
enchendo = False


def interface(request):
    return render(request, 'tanque/ihm.html', {'nivel': nivel})


def estado_nivel(request):
    return JsonResponse({'nivel': nivel})


def ligar(request):
    global enchendo
    enchendo = True
    threading.Thread(target=encher).start()
    return JsonResponse({'status': 'ligado'})


def desligar(request):
    global enchendo
    enchendo = False
    return JsonResponse({'status': 'desligado'})


def encher():
    global nivel, enchendo
    inicio = time.time()
    while enchendo and (time.time() - inicio < 10) and nivel < 100:
        nivel += 1
        time.sleep(0.1)  # velocidade de enchimento
    enchendo = False