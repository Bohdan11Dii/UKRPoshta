from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from mail.forms import (DirectionForm, DirectionSearchForm, RouteForm,
                        RouteSearchForm, VillageSearchForm)
from mail.models import Directions, Route, Village


# Create your views here.
def hello_world(request):
    route = Route.objects.count()
    village = Village.objects.count()
    directions = Directions.objects.count()
    context = {
        "route": route,
        "village": village,
        "directions": directions

    }
    return render(request, "mail/index.html", context=context)

#Route CRUD
class RouteListView(LoginRequiredMixin, generic.ListView):
    model = Route
    paginate_by = 10

    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(RouteListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = RouteSearchForm(
            initial={
                "title": title
            }
        )
        return context

    def get_queryset(self):
        queryset = Route.objects.all().prefetch_related("day")

        form = RouteSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(title__icontains=form.cleaned_data["title"])
        return queryset
    

class RouteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Route
    form_class = RouteForm
    success_url = reverse_lazy("mail:route-list")


class RouteUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Route
    form_class = RouteForm
    success_url = reverse_lazy("mail:route-list")


class RouteDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Route
    success_url = reverse_lazy("mail:route-list")

#Village CRUD
class VillageCreateView(LoginRequiredMixin, generic.CreateView):
    model = Village
    fields = "__all__"
    success_url = reverse_lazy("mail:village-list")


class VillageListView(LoginRequiredMixin, generic.ListView):
    model = Village
    paginate_by = 10

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(VillageListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = VillageSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self):
        queryset = Village.objects.all().prefetch_related("villages")

        form = VillageSearchForm(self.request.GET)

        if form.is_valid():
            queryset = queryset.filter(
                Q(title__icontains=form.cleaned_data["name"])
                | Q(sub_index__icontains=form.cleaned_data["name"])
            )
        return queryset
 

class VillageCreateView(LoginRequiredMixin, generic.CreateView):
    model = Village
    fields = "__all__"
    success_url = reverse_lazy("mail:village-list")


class VillageUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Village
    fields = "__all__"
    success_url = reverse_lazy("mail:village-list")


class VillageDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Village
    success_url = reverse_lazy("mail:village-list")

#Directions CRUD
class DirectionsListView(LoginRequiredMixin, generic.ListView):
    model = Directions
    paginate_by = 10

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(DirectionsListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DirectionSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self):
        queryset = Directions.objects.all().select_related("route")

        form = DirectionSearchForm(self.request.GET)

        if form.is_valid():
            queryset = queryset.filter(
                Q(title__icontains=form.cleaned_data["name"])
                | Q(main_index__icontains=form.cleaned_data["name"])
            )
        return queryset


class DirectionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Directions


class DirectionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Directions
    form_class = DirectionForm
    success_url = reverse_lazy("mail:direction-list")


class DirectionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Directions
    form_class = DirectionForm
    success_url = reverse_lazy("mail:direction-list")


class DirectionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Directions
    success_url = reverse_lazy("mail:direction-list")