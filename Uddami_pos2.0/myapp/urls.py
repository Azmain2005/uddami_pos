from django.urls import path
from . import views

urlpatterns = [
    # User endpoints
    path("users/", views.UserListCreate.as_view(), name="user-list-create"),
    path("users/<int:pk>/", views.UserRetrieveUpdateDestroy.as_view(), name="user-detail"),

    # Meetings endpoints
    path("meetings/", views.MeetingsListCreate.as_view(), name="meetings-list-create"),
    path("meetings/<int:pk>/", views.MeetingsRetrieveUpdateDestroy.as_view(), name="meetings-detail"),

    # Finance endpoints
    path("finance/", views.FinanceListCreate.as_view(), name="finance-list-create"),
    path("finance/<int:pk>/", views.FinanceRetrieveUpdateDestroy.as_view(), name="finance-detail"),

    # Inventory endpoints
    path("inventory/", views.InventoryListCreate.as_view(), name="inventory-list-create"),
    path("inventory/<int:pk>/", views.InventoryRetrieveUpdateDestroy.as_view(), name="inventory-detail"),

    # Projects endpoints
    path("projects/", views.ProjectsListCreate.as_view(), name="projects-list-create"),
    path("projects/<int:pk>/", views.ProjectsRetrieveUpdateDestroy.as_view(), name="projects-detail"),
]
