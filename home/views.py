from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, VastuMaps, Design,  Search
from .forms import searchForm
import folium
import geocoder
# Create your views here.


def home(request):
    design = Design.objects.all()
    return render(request, 'home/home.html', {'design':design})

def design(request):
    design = Design.objects.all()
    return render(request, 'home/design.html', {'design':design})

def maps(request):
    maps = VastuMaps.objects.all()
    return render(request, 'home/maps.html', {'maps':maps})
    
def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        map_requirements=request.POST['map_requirements']
        plot_size = request.POST['plot_size']
        road_direction = request.POST['road_direction']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(map_requirements)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, address=address, map_requirements=map_requirements, plot_size=plot_size, road_direction=road_direction)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
            return redirect('home')
    return render(request, "home/contactus.html")

# def address(request):
#     #create map object.
#     if request.method == 'POST':
#         form = searchForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('address')
#     else:
#         form = searchForm()
#     address = Search.objects.all().last()
#     location = geocoder.osm(address)
#     lat = location.lat
#     lng = location.lng
#     country = location.country
#     m = folium.Map(location = [19, -12], zoom_start = 2)
#     folium.Marker([lat, lng], tooltip='Click for more', popup=country).add_to(m)
#     #Get HTML representation of the map
#     m = m._repr_html_()
#     context = {
#         'm':m,
#         'form':form,
#     }
#     return render(request, "home/address.html", context)


