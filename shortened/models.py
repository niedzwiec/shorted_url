import random
import string

from django.db import models
from django.utils.translation import gettext as _

from .base_int_operation import number_to_str


class UrlKeeper(models.Model):
    original = models.URLField(verbose_name=_("Your Url"))
    shortened = models.URLField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.id is None:
            generator = HashGenerator.get_generator()
            self.shortened = generator.generate_shortened_url()
        super().save(force_insert, force_update, using, update_fields)

    def get_absolute_url(self):
        return f'/{self.id}'

    def __str__(self):
        return self.shortened


class HashGenerator(models.Model):
    BASE = 36
    current_value = models.CharField(max_length=10, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.id is None:
            self.current_value = "1" + HashGenerator.generate_random_str(length=9)
        super().save(force_insert, force_update, using, update_fields)

    @staticmethod
    def generate_random_str(length):
        return "".join([random.choice(string.ascii_letters + string.digits) for _ in range(length)])

    @classmethod
    def get_generator(cls):
        obj = cls.objects.first()
        if obj is None:
            obj = cls()
            obj.save()
        return obj

    def set_number(self, number):
        self.current_value = number_to_str(number, self.BASE)
        self.save()

    def generate_shortened_url(self):
        number = int(self.current_value, self.BASE)
        number += 1
        self.set_number(number)
        return self.current_value
