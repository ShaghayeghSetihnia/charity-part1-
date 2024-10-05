from django.db import models
from accounts.models import User
from django.db.models import Q


class Benefactor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(choices=[(0, 'Beginner'), (1, 'Intermediate'), (2, 'Expert')], default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.user.username


class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        return self.filter(charity__user=user)

    def related_tasks_to_benefactor(self, user):
        return self.filter(assigned_benefactor__user=user)

    def all_related_tasks_to_user(self, user):
        return self.filter(
            Q(charity__user=user) | 
            Q(assigned_benefactor__user=user) | 
            Q(state='P')
        )


class Task(models.Model):
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    assigned_benefactor = models.ForeignKey(Benefactor, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    age_limit_from = models.IntegerField(blank=True, null=True)
    age_limit_to = models.IntegerField(blank=True, null=True)
    gender_limit = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], blank=True, null=True)
    state = models.CharField(max_length=1, choices=[('P', 'Pending'), ('W', 'Waiting'), ('A', 'Assigned'), ('D', 'Done')], default='P')

    objects = TaskManager()

    def __str__(self):
        return self.title
