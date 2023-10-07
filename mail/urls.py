from django.urls import path

from mail.views import (DirectionCreateView, DirectionDeleteView,
                        DirectionDetailView, DirectionsListView,
                        DirectionUpdateView, RouteCreateView, RouteDeleteView,
                        RouteListView, RouteUpdateView, VillageCreateView,
                        VillageDeleteView, VillageListView, VillageUpdateView,
                        hello_world)

urlpatterns = [
    path("", hello_world, name="home"),

    path("routes/", RouteListView.as_view(), name="route-list"),
    path("routes/create/", RouteCreateView.as_view(), name="route-create"),
    path("routes/<int:pk>/update/", RouteUpdateView.as_view(), name="route-update"),
    path("routes/<int:pk>/delete/", RouteDeleteView.as_view(), name="route-delete"),

    path("villages/", VillageListView.as_view(), name="village-list"),
    path("villages/create/", VillageCreateView.as_view(), name="village-create"),
    path("villages/<int:pk>/update/", VillageUpdateView.as_view(), name="village-update"),
    path("villages/<int:pk>/delete/", VillageDeleteView.as_view(), name="village-delete"),

    path("directions/", DirectionsListView.as_view(), name="direction-list"),
    path("directions/<int:pk>/", DirectionDetailView.as_view(), name="direction-detail"),
    path("directions/create/", DirectionCreateView.as_view(), name="direction-create"),
    path("directions/<int:pk>/update/", DirectionUpdateView.as_view(), name="direction-update"),
    path("directions/<int:pk>/delete/", DirectionDeleteView.as_view(), name="direction-delete"),
]

app_name = "mail"