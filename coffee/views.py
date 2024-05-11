from django.shortcuts import render
from .models import Coffee
from rest_framework.views import APIView

from .serializers import CoffeeSerializer

from rest_framework.response import Response
# Create your views here.

def home(request):
    coffee = Coffee.objects.all()
    return render(request, 'coffee/home.html', {'coffee':coffee})

def about(request):
    return render(request, 'coffee/about.html')

def connect(request):
    return render(request, 'coffee/connect.html')

def team(request):
    return render(request, 'coffee/team.html')

def service(request):
    return render(request, 'coffee/service.html')


# class Index(APIView):
#
#     def get(self, request):
#         coffee = Coffee.objects.all()
#         serializer = CoffeeSerializer(coffee, many=True, context={})
#         return Response(serializer.data)
