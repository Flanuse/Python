from django.db import models


class Promission(models.Model):
    p_name = models.CharField(max_length=30)

    class Meta:

        db_table = 'promission'


class Role(models.Model):
    r_name = models.CharField(max_length=30)
    r_p = models.ManyToManyField(Promission)

    class Meta:
        db_table = 'role'


class MyUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255, null=False)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=0)
    r = models.ForeignKey(Role, null=True)

    class Meta:
        db_table = 'my_user'


class UserTicketModel(models.Model):
    user = models.ForeignKey(MyUser)
    ticket = models.CharField(max_length=255)
    out_time = models.DateTimeField()

    class Meta:
        db_table = 'my_user_ticket'

