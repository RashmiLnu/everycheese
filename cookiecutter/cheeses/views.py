from django.urls import reverse_lazy
# from django.views.generic import ListView, DetailView
from .models import Cheese
# from django.views.generic import CreateView
from django.views.generic import DeleteView
# from django.views.generic import UpdateView
from django.views.generic import (
ListView,
DetailView,
CreateView,
UpdateView
)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model = Cheese

class CheeseCreateView(LoginRequiredMixin, CreateView):
    model = Cheese
    fields = [
            "name",
            "description",
            "firmness",
            "country_of_origin",
    ]

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)



class CheeseDeleteView(DeleteView):
    model = Cheese
    template_name = "cheeses/cheese_confirm_delete.html"
    success_url = reverse_lazy("cheeses:list")

class CheeseUpdateView(LoginRequiredMixin, UpdateView):
    model = Cheese
    fields = [
            "name",
            "description",
            "firmness",
            "country_of_origin",
    ]
    action = "Update"
    # def get_success_url(self):
    #     return reverse_lazy('cheeses:detail', kwargs={'slug': self.object.slug})
