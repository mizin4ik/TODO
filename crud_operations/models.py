from django.db import models


class ToDo(models.Model):

    title = models.CharField(
        max_length=50,
        blank=False)

    description = models.CharField(
        max_length=256,
        blank=False)

    start_task = models.DateField(
        blank=False)

    deadline = models.DateField(
        blank=False)

    todo = models.BooleanField(
        default=False)

    in_progress = models.BooleanField(
        default=False)

    done = models.BooleanField(
        default=False)
