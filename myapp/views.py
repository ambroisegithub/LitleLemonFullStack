
from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem
from .serializers import  MenuItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
# Create your views here.

class MenuItemView(generics.ListCreateAPIView):
    
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    
class SingletMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    

# @api_view()
# def menu_items(request):
#     items = MenuItem.objects.select_related('category').all()
#     serialized_items = MenuItemSerializer(items,many=True)
#     return Response(serialized_items.data)
#     # return Response(items.values())
    
    
# @api_view()
# def single_items(request,id):
#     items = get_object_or_404(MenuItem, pk=id)
#     serialized_items = MenuItemSerializer1(items)
#     return Response(serialized_items.data)  


# deserialization 
# filtering and searching  
@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.all()  
        serialized_items = MenuItemSerializer(items, many=True)
        return Response(serialized_items.data)
    elif request.method == 'POST':
        reservation_data = request.data.get('reservation_data')
        reservation_slot = request.data.get('reservation_slot')

        # Check if reservation already exists with the same data and slot
        existing_reservation = MenuItem.objects.filter(reservation_data=reservation_data, reservation_slot=reservation_slot).first()
        if existing_reservation:
            return Response({"error": "Reservation already exists for the same data and slot."}, status=status.HTTP_400_BAD_REQUEST)

        serialized_items = MenuItemSerializer(data=request.data)
        serialized_items.is_valid(raise_exception=True)
        serialized_items.save()
        return Response(serialized_items.data, status=status.HTTP_201_CREATED)

    # return Response(items.values())
 
# handling single items
  
@api_view()
def single_items(request,id):
    items = get_object_or_404(MenuItem, pk=id)
    serialized_items = MenuItemSerializer(items)
    return Response(serialized_items.data)     
 
#  handling html
def base(request):
    return render(request,'base.html')
def allreservations(request):
    return render(request,'allreservations.html')