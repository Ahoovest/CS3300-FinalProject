# Generated by Django 5.0.4 on 2024-04-08 00:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('username', models.CharField(max_length=200, unique=True, verbose_name='Username')),
                ('contact_email', models.EmailField(blank=True, max_length=254, verbose_name='Contact Email')),
                ('plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workout_app.plan')),
            ],
        ),
    ]
