from django.db import models


class UserModel(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=64, unique=True)
    img = models.ImageField(upload_to='icon', null=True)
    rename = models.CharField(max_length=32, default='')
    readdress = models.CharField(max_length=124, default='')
    postcode = models.CharField(max_length=20, default='')
    rephone = models.CharField(max_length=20, default='')

    class Meta:
        db_table = 'fruit_users'


class TicketModel(models.Model):
    user = models.ForeignKey(UserModel)
    session_id = models.CharField(max_length=255)
    out_time = models.DateTimeField()

    class Meta:
        db_table = 'fruit_ticket'