from django.urls import path
from . import views

app_name = "cheeses"
urlpatterns = [
    path(route="", view=views.CheeseListView.as_view(), name="list"),
    # URL Pattern for the CheeseDetailView
    path(route="<slug:slug>/", view=views.CheeseDetailView.as_view(), name="detail"),
]
