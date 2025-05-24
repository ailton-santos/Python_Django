from django.shortcuts import render
from django.http import JsonResponse
import time, threading

tanque_nivel = 0
tanque_ligado = False

def painel(request):
    return render(request, 'scada/painel.html')

def iniciar(request):
    global tanque_ligado
    tanque_ligado = True
    threading.Thread(target=encher).start()
    return JsonResponse({'status': 'ok'})

def parar(request):
    global tanque_ligado
    tanque_ligado = False
    return JsonResponse({'status': 'parado'})

def nivel(request):
    return JsonResponse({'nivel': tanque_nivel})

def encher():
    global tanque_nivel, tanque_ligado
    inicio = time.time()
    while tanque_ligado and (time.time() - inicio < 10) and tanque_nivel < 100:
        tanque_nivel += 1
        time.sleep(0.1)
    tanque_ligado = False
