
from django.shortcuts import render , redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car , Modification
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def car_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', {'cars': cars})

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'base.html')

def about(request):
    # Send a simple HTML response
    return render(request, 'about.html')

# views.py
@login_required
def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    modifications_car_doesnt_have = Modification.objects.exclude(id__in = car.modifications.all().values_list('id'))
   

    return render(request, 'cars/detail.html', {'car': car,'modifications': modifications_car_doesnt_have}
      )



def car_index(request):
    cars = Car.objects.all()
    # Render the cats/index.html template with the cats data
    return render(request, 'cars/index.html', {'cars': cars})



# main-app/views.py




class Home(LoginView):
    template_name = 'home.html'

class CarCreate(LoginRequiredMixin,CreateView):
    model = Car
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/cars/'


class CarUpdate(LoginRequiredMixin,UpdateView):
    model = Car
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['model', 'brand', 'color']

class CarDelete(LoginRequiredMixin,DeleteView):
    model = Car
    success_url = '/cars/'




class ModificationCreate(LoginRequiredMixin,CreateView):
    model = Modification
    fields = '__all__'


class ModificationList(LoginRequiredMixin,ListView):
    model = Modification


class ModificationDetail(LoginRequiredMixin,DetailView):
    model = Modification



class ModificationUpdate(LoginRequiredMixin,UpdateView):
    model = Modification
    fields = ['name', 'price']



class ModificationDelete(LoginRequiredMixin,DeleteView):
    model = Modification
    success_url = '/modifications/'

def associate_modification(request, car_id, modification_id):
    Car.objects.get(id=car_id).modifications.add(modification_id)
    return redirect('car-detail', car_id=car_id)

def remove_modification(request, car_id, modification_id):
    # Look up the car
    car = Car.objects.get(id=car_id)
    # Look up the modification
    modification = Modification.objects.get(id=modification_id)
    # Remove the modification from the car
    car.modifications.remove(modification)
    return redirect('car-detail', car_id=car.id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('car-index')
        else:
            error_message = "Invalid sign up - try again"

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)