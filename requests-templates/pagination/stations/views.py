# from pagination.settings import BUS_STATION_CSV  УПОРНО ВЫДАЕТ ОШИБКУ ModuleNotFoundError: No module named 'pagination' НЕИЗВЕСТНО С ЧЕМ СВЯЗАНО
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv


import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent                                    #костыльное решение из-за ошибки выше
BUS_STATION_CSV = os.path.join(BASE_DIR, 'data-398-2018-08-30.csv')



def index(request):
    return redirect(reverse('bus_stations'))

def read_cvv():
    with open (BUS_STATION_CSV, 'r', encoding='utf-8') as f:
        top = csv.DictReader(f)
        show = list(top)
    Stations = [i for i in show]
    return Stations

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    paginator = Paginator(read_cvv(), 10)
    page_num = int(request.GET.get("page", 1))
    page = paginator.get_page(page_num)
    
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
