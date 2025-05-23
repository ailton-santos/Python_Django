from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django_otp.plugins.otp_totp.models import TOTPDevice

def login_mfa(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        token = request.POST['token']

        user = authenticate(request, username=username, password=password)
        if user:
            device = TOTPDevice.objects.filter(user=user, confirmed=True).first()
            if device and device.verify_token(token):
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'erro': 'Token inválido.'})
        else:
            return render(request, 'login.html', {'erro': 'Credenciais inválidas.'})

    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')