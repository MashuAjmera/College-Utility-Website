# Generated by Django 2.0.7 on 2018-07-10 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='institute',
            field=models.CharField(choices=[('LNMIIT', 'The LNM Institute Of Information Technology'), ('VIT', 'Vellore Institute Of Technology'), ('SRM', 'Sri Ramaswamy Memoria Institute')], max_length=10),
        ),
    ]