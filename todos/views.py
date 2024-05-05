from rest_framework import generics 

from .models import Todo 
from .serializers import TodoSerializer


"""""
CRUD Operation
c = Create
R = Read
U = Update 
D = Delete 
"""


class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all().order_by('-id')
    serializer_class = TodoSerializer
    
    
class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    