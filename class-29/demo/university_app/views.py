from django.shortcuts import render
import requests
from django.http import JsonResponse
from .models import University

# Create your views here.

data = requests.get('http://universities.hipolabs.com/search?name=middle')

def home_view(request):
    global data
    api_data = data.json()

    # insert API data in DB
    for uni in api_data:

        if not University.objects.filter(alpha_two_code=uni['alpha_two_code'], web_pages=uni['web_pages'][0], country=uni['country'], name=uni["name"], state_province=uni["state-province"]).exists():

            University.objects.create(alpha_two_code=uni['alpha_two_code'], web_pages=uni['web_pages'][0], country=uni['country'], name=uni["name"], state_province=uni["state-province"])
        
    universities = University.objects.all()
    return render(request, 'index.html', {"universities":universities})

    # return JsonResponse({'uni_arr': api_data})

def uni_details_view(request,pk):
    uni = University.objects.filter(id=pk).values()
    uni_list = list(uni)
    return JsonResponse({"uni_details":uni_list})

