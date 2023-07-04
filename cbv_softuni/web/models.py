from django.db import models


class Employee(models.Model):
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=30,
    )
    seniority_level = models.CharField(
        max_length=30,
        choices=(
            ('Senior', 'Senior'),
            ('Junior', 'Junior'),
        )
    )

    # def get_absolute_url(self):
    #     pass