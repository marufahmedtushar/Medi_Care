# Generated by Django 3.0.3 on 2020-04-19 10:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicare', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription_pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=300)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='prescription')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bloodds',
            fields=[
                ('donner_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('age', models.CharField(default='', max_length=1000)),
                ('phone', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('bloodgroup', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=600)),
                ('lastdonate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
