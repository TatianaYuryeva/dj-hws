from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open("data-398-2018-08-30.csv") as f:
        content = list(csv.DictReader(f))
    current_page = int(request.GET.get("page", 1))
    paginator = Paginator(content, 10)
    page = paginator.get_page(current_page)
    context = {
        'page': page,
        'bus_stations': page,
        'current_page': current_page,
    }
    return render(request, 'index.html', context)
