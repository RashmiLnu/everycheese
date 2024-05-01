from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
# from django.views.generic import ListView, DetailView
from .models import Cheese, Rating
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
from django.urls import reverse

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['rating'] = Rating.objects.get(cheese=self.object, user=self.request.user)
        except Rating.DoesNotExist:
            context['rating'] = None
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        rating, created = Rating.objects.get_or_create(
            cheese=self.object,
            user=self.request.user,
            defaults={'rating': self.request.POST['rating']},
        )
        if not created:
            rating.rating = self.request.POST['rating']
            rating.save()
        return response

    def get_success_url(self):
        print(f"Slug: {self.object.slug}")  # Add this line
        # redirect to cheese list
        return reverse('cheeses:list')
        # return reverse('cheeses:detail', kwargs={'slug': self.object.slug})

class RatingCreateView(LoginRequiredMixin, CreateView):
    model = Rating
    fields = ['rating']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.cheese = get_object_or_404(Cheese, slug=self.kwargs['slug'])
        return super().form_valid(form)

class RatingUpdateView(LoginRequiredMixin, UpdateView):
    model = Rating
    fields = ['rating']

    def get_object(self, queryset=None):
        return get_object_or_404(Rating, cheese__slug=self.kwargs['slug'], user=self.request.user)

