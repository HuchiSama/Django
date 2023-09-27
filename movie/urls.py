from django.urls import path
from movie import views as Movie

urlpatterns = [
    path('addCollect/', Movie.addCollect, name="addCollect"),
    path('addMovie/', Movie.addMovie, name="addMovie"),
    path('collectMovie/', Movie.collectMovie, name="collectMovie"),
    path('delete/', Movie.deleteCollect, name="delete"),
    path('query/', Movie.query, name="query"),
    path('getOne/', Movie.getOne, name="getOne"),
    path('myRequest/', Movie.myRequest, name="myRequest"),
    path('myResponse/', Movie.myResponse, name="myResponse"),
]