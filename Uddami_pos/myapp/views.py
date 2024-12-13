from rest_framework import generics
from .models import User, Meetings, Finance, Inventory, Projects
from .serializers import UserSerializer, MeetingsSerializer, FinanceSerializer, InventorySerializer, ProjectsSerializer

# User Views
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"


# Meetings Views
class MeetingsListCreate(generics.ListCreateAPIView):
    queryset = Meetings.objects.all()
    serializer_class = MeetingsSerializer


class MeetingsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meetings.objects.all()
    serializer_class = MeetingsSerializer
    lookup_field = "pk"


# Finance Views
class FinanceListCreate(generics.ListCreateAPIView):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer


class FinanceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer
    lookup_field = "pk"


# Inventory Views
class InventoryListCreate(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    lookup_field = "pk"


# Projects Views
class ProjectsListCreate(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class ProjectsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = "pk"
