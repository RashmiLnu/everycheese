from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Cheese
from django.views.generic import CreateView
from django.views.generic import DeleteView

class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model = Cheese

class CheeseCreateView(CreateView):
    model = Cheese
    fields = [
            "name",
            "description",
            "firmness",
            "country_of_origin",
    ]

class CheeseDeleteView(DeleteView):
    model = Cheese
    template_name = "cheeses/cheese_confirm_delete.html"
    success_url = reverse_lazy("cheeses:list")
