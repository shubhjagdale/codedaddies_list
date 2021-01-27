from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus

BASE_CRAIGSLIST_URL = 'https://pune.craigslist.org/search/bbb?s=120'
# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    final_url = BASE_CRAIGSLIST_URL
    response = requests.get('https://pune.craigslist.org/search/bbb?query=cafe')
    data = response.text
    print(data)
    stuff_for_frontend = {
        'search': search,
    }

    return render(request,'my_app/new_search.html',stuff_for_frontend)