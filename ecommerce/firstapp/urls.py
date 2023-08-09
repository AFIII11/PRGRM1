
from django.urls import path
from . import views
urlpatterns = [
    
    path('addproduct',views.addproduct.as_view(),name='addproduct'),
    path('getproduct',views.getproduct.as_view(),name='getproduct'),
    path('Get_single_PackageproductAPIView/<int:id>',views.Get_single_PackageproductAPIView.as_view(),name='Get_single_PackageproductAPIView'),
    path('Update_product/<int:id>',views.Update_product.as_view(),name='Update_product'),
    path('Delete_PackageproductAPIView/<int:id>',views.Delete_PackageproductAPIView.as_view(),name='Delete_PackageproductAPIView'),
    
    
    
]

