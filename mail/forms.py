import datetime as dt

from bootstrap_datepicker_plus.widgets import TimePickerInput
from django import forms
from django.contrib.admin.widgets import AdminTimeWidget

from mail.models import Day, Directions, Route, Village


class RouteForm(forms.ModelForm):
    day = forms.ModelMultipleChoiceField(
        queryset=Day.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        
    )

    start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    end_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

    class Meta:
        model = Route
        fields = "__all__"


class DirectionForm(forms.ModelForm):
    village = forms.ModelMultipleChoiceField(
        queryset=Village.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Directions
        fields = "__all__"


class RouteSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )


class VillageSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name or index"}
        )
    )


class DirectionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name or index"}
        )
    )


