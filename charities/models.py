from django.db import models
from accounts.models import User
from django.db.models import Q

GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
)

STATE_CHOICES = (
    ("P", "Pending"),
    ("W", "Waiting"),
    ("A", "Assigned"),
    ("D", "Done"),
)

EXPERIENCE_CHOICES = (
    (0, "Beginner"),
    (1, "Medium"),
    (2, "Expert"),
)


class Benefactor(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(choices=EXPERIENCE_CHOICES, default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)


class Charity(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        return Task.objects.filter(charity__user=user)

    def related_tasks_to_benefactor(self, user):
        return Task.objects.filter(assigned_benefactor__user=user)

    def all_related_tasks_to_user(self, user):
        return Task.objects.filter(Q(charity__user=user) | Q(state='P')) or \
            Task.objects.filter(Q(assigned_benefactor__user=user) | Q(state='P'))


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    assigned_benefactor = models.ForeignKey(Benefactor, null=True, on_delete=models.SET_NULL)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    ag_limit_form = models.IntegerField(blank=True, null=True)
    age_limit_to = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gender_limit = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default="P")
    title = models.CharField(max_length=60)

    objects = TaskManager()
    

