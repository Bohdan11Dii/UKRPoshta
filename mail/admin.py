from django.contrib import admin

from mail.models import Day, Directions, Route, Village


# Register your models here.
@admin.register(Directions)
class DirectionsAdmin(admin.ModelAdmin):
    list_display = ["title", "main_index", "time", ]
    list_filter = ["route",]
    search_fields = ["title",]


admin.site.register(Route)

admin.site.register(Day)
admin.site.register(Village)
