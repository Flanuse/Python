# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-25 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'my_user',
            },
        ),
        migrations.CreateModel(
            name='Promission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'promission',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.CharField(max_length=30)),
                ('r_p', models.ManyToManyField(to='adminback.Promission')),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='UserTicketModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=255)),
                ('out_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminback.MyUser')),
            ],
            options={
                'db_table': 'my_user_ticket',
            },
        ),
        migrations.AddField(
            model_name='myuser',
            name='r',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminback.Role'),
        ),
    ]
