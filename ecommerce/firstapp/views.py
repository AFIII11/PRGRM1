from django.shortcuts import render
from.serializers import ProductSerializer
from.models import product
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
class addproduct(GenericAPIView):
    serializer_class=ProductSerializer

    def post(self,request):
        
        productnames=request.data.get('productname')
        prices=request.data.get('price')
        ratings=request.data.get('rating')
        catagorys=request.data.get('catagory')
        
        serializer=self.serializer_class(data={'productname':productnames,'price':prices,'rating':ratings,'catagory':catagorys})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'Product added Successfully', 'success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.error,'message':'Failed','success':False},status=status.HTTP_400_BAD_REQUEST)
    class Update_product(GenericAPIView):
        serializer_class=ProductSerializer
        def put(self,request,id):
            queryset=product.objects.get(pk=id)
            print(queryset)
            serializer=ProductSerializer(instance=queryset,data=request.data,partial=True)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'message':'updated succesfully','success':True},)
            else:
                return Response({'data':'something went wrong','success':False},status=status.HTTP_400_BAD_REQUEST)
class getproduct(GenericAPIView):
        serializer_class=ProductSerializer
        def get(self,request):
            queryset=product.objects.all()
            if(queryset.count()>0):
                serializer=ProductSerializer(queryset,many=True)
                return Response({'data':serializer.data,'message':'all package hotel set','success':True},status=status.HTTP_200_OK)
            else:
                return Response({'data':'no data available','success':False},status=status.HTTP_201_CREATED)
        

        #single package Hotel view
class Get_single_PackageproductAPIView(GenericAPIView):
    def get(self,request,id):
        queryset=product.objects.filter(id=id).values()
        return Response({'data':queryset,'message':'single product data','success':True},status=status.HTTP_200_OK)
        
class Delete_PackageproductAPIView(GenericAPIView):
    def delete(self,request,id):
        deldata=product.objects.get(id=id)
        deldata.delete()
        return Response({'message':'Deleted successfully','success':True},status=status.HTTP_200_OK)

            



class Update_product(GenericAPIView):
    serializer_class=ProductSerializer
    def put(self,request,id):
        queryset=product.objects.get(pk=id)
        print(queryset)
        serializer=ProductSerializer(instance=queryset,data=request.data,partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'updated successfully','success':True},status=status.HTTP_200_OK)
        else:
            return Response({'data':serializer.error,'message':'Update Failed','success':False},status=status.HTTP_400_BAD_REQUEST)





