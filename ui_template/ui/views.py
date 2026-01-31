from django.shortcuts import render

from django.shortcuts import render

def dashboard(request):
    return render(request, "ui/pages/dashboard.html", {"active_nav": "dashboard"})

def tables(request):
    return render(request, "ui/pages/tables.html", {"active_nav": "tables"})

def forms(request):
    return render(request, "ui/pages/forms.html", {"active_nav": "forms"})

