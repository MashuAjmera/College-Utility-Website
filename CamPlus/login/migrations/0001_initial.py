# Generated by Django 2.0.6 on 2018-07-10 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(choices=[('LNMIIT', 'The LNM Institute Of Information Technology'), ('VIT', 'Vellore Institute Of Technology'), ('SRM', 'SRM')], max_length=10)),
                ('year', models.CharField(choices=[('Y18', 'Y18'), ('Y17', 'Y17'), ('Y16', 'Y16'), ('Y15', 'Y15')], max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]