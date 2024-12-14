import requests
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import User, Meetings, Finance, Inventory, Projects
from .serializers import UserSerializer, MeetingsSerializer, FinanceSerializer, InventorySerializer, ProjectsSerializer

# Replace with your ImgBB API key
IMG_API_KEY = "810cda668741509c61e657b991c996d7"

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
    parser_classes = [MultiPartParser, FormParser]  # For handling file uploads

    def post(self, request, *args, **kwargs):
        # Prepare a dictionary to store the final data
        data = request.data.dict()  # Convert request data to a dictionary

        image_fields = [
            "ownerImage",
            "room_image1",
            "room_image2",
            "room_image3",
            "room_image4",
            "room_image5"
        ]

        # Loop through the image fields and upload each to ImgBB
        for field in image_fields:
            if field in request.FILES:
                image_file = request.FILES[field]
                try:
                    # Upload the image to ImgBB
                    url = f"https://api.imgbb.com/1/upload?key={IMG_API_KEY}"
                    files = {'image': image_file.read()}
                    response = requests.post(url, files=files)

                    if response.status_code == 200:
                        # If the upload was successful, extract the image URL
                        imgbb_data = response.json()
                        image_url = imgbb_data['data']['url']
                        data[field] = image_url  # Replace the local file path with ImgBB URL
                    else:
                        return Response({"error": f"Failed to upload {field} to ImgBB"}, status=status.HTTP_400_BAD_REQUEST)
                finally:
                    # Ensure the file is closed properly after use
                    image_file.close()

        # Save the Project instance with updated data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProjectsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = "pk"