from django.shortcuts import render

from django.http import HttpResponse

from .models import Destination

# Create your views here.

def index(request):
   dests= Destination.objects.all()


#     # return HttpResponse('helllo world')

    
#     # Creating first destination's object 

#     dest1= Destination()
#     dest1.name= 'Pan Pacific Sonargaon'
#     dest1.desc= 'It is one of the oldest 5 star hotel in Bangladesh'
#     dest1.price= 50000
#     dest1.img='destination_2.jpg'

#     dest1.offer= False

#     # Creating second destination's object 

#     dest2= Destination()
#     dest2.name= 'Hydrabad'
#     dest2.desc= 'This is one of the oldest city in the India'
#     dest2.price= 30000
#     dest2.img='destination_3.jpg'

#     dest2.offer= True 

#  # Creating third destination's object 

#     dest3= Destination()
#     dest3.name= 'Mumbai'
#     dest3.desc= 'The city I love most'
#     dest3.price= 7800
#     dest3.img='destination_1.jpg'
#     dest3.offer= False

#     # Passing the objects as a list 

#     dests= [dest1, dest2, dest3]





   return render(request, 'index.html', {'dests': dests})
