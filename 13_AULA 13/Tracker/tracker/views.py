from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CalorieEntryForm
from .models import CalorieEntry
from datetime import timedelta, date

@login_required
def dashboard(request):
    today = date.today()
    week_ago = today - timedelta(days=7)
    entries = CalorieEntry.objects.filter(user=request.user, date__gte=week_ago).order_by('-date')
    total = sum(e.calories for e in entries)
    return render(request, 'tracker/dashboard.html', {'entries': entries, 'total': total})

@login_required
def add_entry(request):
    if request.method == 'POST':
        form = CalorieEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('dashboard')
    else:
        form = CalorieEntryForm()
    return render(request, 'tracker/add_entry.html', {'form': form})