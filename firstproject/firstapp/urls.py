from django.urls import path
from firstapp import views

urlpatterns = [
    path("",views.index,name='index'),
    path("fdnw",views.fdnw,name='fdnw'),
   path("view",views.view,name='view'),
   path("Adddata",views.Adddata,name='Adddata'),
   path("edit/<int:id>",views.edit,name='edit'),
    path("formupdate/<int:id>",views.formupdate,name='formupdate'),
     path("delete/<int:id>",views.delete,name='delete'),
]