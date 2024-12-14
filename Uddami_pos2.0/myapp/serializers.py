from rest_framework import serializers
from .models import User, Meetings, Finance, Inventory, Projects

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MeetingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meetings
        fields = '__all__'


class FinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finance
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
