from django.urls import path
from myApp import views as myApp

urlpatterns = [
    path('index/', myApp.demo, name="index"),
    path('index2/', myApp.index, name='index2'),
    path('users/', myApp.getUsers, name='users'),
    path('add/', myApp.addInfo, name='add'),
    path('delete/', myApp.deleteInfo, name='delete'),
    path('update/', myApp.updateInfo, name='update'),
    path('get/', myApp.getInfo, name='get'),
    path('pagination/<int:page>/', myApp.pagination, name='pagination'),
    path('pagination2/<int:page>/', myApp.pagination2, name='pagination2'),
    path('addUserType/', myApp.addUserType, name='addUserType'),
    path('deletePeple/', myApp.deletePeple, name='deletePeple'),
    path('addPeple/', myApp.addPeple, name='addPeple'),
    path('delUserType/', myApp.deleteUserType, name='deleteUserType'),
]

