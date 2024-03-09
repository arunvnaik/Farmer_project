from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from quickstart.models import Farmer, Crop, Earnings
from quickstart.serializer import FarmerSerializer, CropSerializer, EarningsSerializer
# from rest_framework.permissions import IsAdminOrReadOnly
# 
#  from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.permissions import IsAuthenticated
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.permissions import IsAdminOrReadOnly
# from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly



class FarmerAPIView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    
    def get(self, request):
        farmers = Farmer.objects.all()
        serializer = FarmerSerializer(farmers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FarmerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
class FarmerDetailView(APIView):
    # Permission_classes=IsAdminOrReadOnly
    def get (self,request,pk):
        try:
            farmer=Farmer.objects.get(pk=pk)
            serializer=FarmerSerializer(farmer)
            return Response(serializer.data)
        except Farmer.DoesNotExist:
            return Response({'error': "not found"})
    
    
    def put (self,request,pk):
        try:
            farmer=Farmer.objects.get(pk=pk)
            serializer =FarmerSerializer (farmer,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Farmer.DoesNotExist:
            return Response({"errors": "Farmer does not exist"}, status=status.HTTP_404_NOT_FOUND)

        
    def delete(self,request,pk) :     
        try:
            farmer = Farmer.objects.get(pk=pk)
            farmer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Farmer.DoesNotExist:
            return Response({"errors": "Farmer does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
            

class CropAPIView(APIView):
    # permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        crops = Crop.objects.all()
        serializer = CropSerializer(crops, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CropSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class CropDetailView(APIView):
    def get(self, request, pk):
        try:
            crop = Crop.objects.get(pk=pk)
            serializer = CropSerializer(crop)
            return Response(serializer.data)
        except Crop.DoesNotExist:
            return Response({'error': "Crop not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
    def put (self,request,pk):
        try:
            crop=Crop.objects.get(pk=pk)
            serializer=CropSerializer(crop,data=request.data) 
            if serializer.is_valid():
                serializer.save() 
                return Response(serializer.data)
            return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Crop.DoesNotExist:
            return Response({"error":"not found "},status=status.HTTP_400_BAD_REQUEST)
            
    def delete (self,request,pk):
        try:
            crop=Crop.objects.get(pk=pk)
            crop.delete()
            return Response ({'message': "crop deletecing succesfully"},status=status.HTTP_204_NO_CONTENT)
        except Crop.DoesNotExist()  :
            return Response ({'error': "not found"})         
        
class EarningsAPIView(APIView):
    
      
    
    def get(self, request):
        earnings = Earnings.objects.all()
        serializer = EarningsSerializer(earnings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EarningsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class EarningDetailView(APIView):
    
    def get(self, request, pk):
        try:
            earnings = Earnings.objects.get(pk=pk)
            serializer = EarningsSerializer(earnings)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Earnings.DoesNotExist:
            return Response({'error': "Earning not found"}, status=status.HTTP_404_NOT_FOUND)
            
    def put(self, request, pk):
        try:
            earnings = Earnings.objects.get(pk=pk)
        except Earnings.DoesNotExist:
            return Response({'error': "Earning not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EarningsSerializer(earnings, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            earnings = Earnings.objects.get(pk=pk)
            earnings.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Earnings.DoesNotExist:
            return Response({'error': "Earning not found"}, status=status.HTTP_404_NOT_FOUND)