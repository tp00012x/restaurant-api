# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models


class Restaurant(models.Model):
    # Adding blank=False make these fields required. Django will take care of the validations.
    name = models.CharField(max_length=100, blank=False)
    opening_time = models.TimeField(blank=False)
    closing_time = models.TimeField(blank=False)

    # Make is_open an attribute that will automatically be calculated on model creation or GET request made API endpoint
    @property
    def is_open(self):
        return True if self.opening_time <= datetime.now().time() < self.closing_time else False

    def __str__(self):
        return self.name
