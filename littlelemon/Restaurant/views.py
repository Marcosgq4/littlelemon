from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

# Create your views here.
def home(request):
    return render(request, 'restaurant/index.html', {})

    
class MenuView(ListCreateAPIView):
    
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response({"menu": serializer.data})
    
    def post(self, request):
        item = request.data.get('menu')
        serializer = MenuSerializer(data=item)
        if serializer.is_valid(raise_exception=True):
            item_saved = serializer.save()
        return Response({"success": "Menu '{}' created successfully".format(item_saved.title)})
    
class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    
    def get(self, request, pk):
        item = Menu.objects.get(pk=pk)
        serializer = MenuSerializer(item)
        return Response({"menu_item": serializer.data})
    
    def put(self, request, pk):
        saved_item = Menu.objects.get(pk=pk)
        data = request.data.get('menu')
        serializer = MenuSerializer(instance=saved_item, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            item_saved = serializer.save()
        return Response({"success": "Menu item '{}' updated successfully".format(item_saved.title)})
    
    def delete(self, request, pk):
        item = Menu.objects.get(pk=pk)
        item.delete()
        return Response({"message": "Menu item with id `{}` has been deleted.".format(pk)}, status=204)
    

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

#class BookingView(APIView):
#    
#    def get(self, request):
#        items = Booking.objects.all()
#        serializer = BookingSerializer(items, many=True)
#        return Response({"bookings": serializer.data})

#class UserViewSet(viewsets.ModelViewSet):
#   queryset = User.objects.all() 
#   serializer_class = UserSerializer
#   permission_classes = [permissions.IsAuthenticated] 