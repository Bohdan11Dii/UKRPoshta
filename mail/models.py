from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Day(models.Model):
    DAY = (
        ("Mon", "Monday"),
        ("Tues", "Tuesday"),
        ("Wed", "Wednesday"),
        ("Thurs", "Thursday"),
        ("Fri", "Friday"),
        ("Sat", "Saturday"),
        ("Sun", "Sunday"),
    )
    day = models.CharField(
        max_length=5,
        choices=DAY,
        default="Mon"
    )

    def __str__(self):
        return self.day
    
    class Meta:
        ordering = ("day", )


class Route(models.Model):
    title = models.CharField(max_length=255)
    day = models.ManyToManyField(Day, related_name="routs")
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title


class Village(models.Model):
    title = models.CharField(max_length=255)
    sub_index = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("title", )

class Directions(models.Model):
    title = models.CharField(max_length=255)
    main_index = models.IntegerField()
    time = models.TimeField()
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        related_name="villages",
    )
    village = models.ManyToManyField(
        Village,
        related_name="villages",
        blank=True
    )

    def __str__(self):
        return f"{self.title} - {self.main_index}"