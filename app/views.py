from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')

def usd_to_egp(request):
    context = {
        'usd_to_egp': 30,
    }
    return render(request, 'app/usd-to-egp.html', context=context)
