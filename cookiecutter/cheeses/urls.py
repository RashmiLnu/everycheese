from django.urls import path
from . import views

app_name = "cheeses"

urlpatterns = [
    path(route="",
         view=views.CheeseListView.as_view(),
         name="list"
    ),

    path(
        route='add/',
        view=views.CheeseCreateView.as_view(),
        name='add'
    ),

    path(
       route='<slug:slug>/update/',
       view=views.CheeseUpdateView.as_view(),
       name='update'
    ),


    path(
        route='delete/<slug:slug>/',
        view=views.CheeseDeleteView.as_view(),
        name='delete'
    ),

    # URL Pattern for the CheeseDetailView
    path(route="<slug:slug>/",
         view=views.CheeseDetailView.as_view(),
         name="detail"
    ),

    path('cheeses/<slug:slug>/rate/', views.RatingCreateView.as_view(), name='rate_cheese'),
    path('cheeses/<slug:slug>/rate/update/', views.RatingUpdateView.as_view(), name='update_rating'),



]
