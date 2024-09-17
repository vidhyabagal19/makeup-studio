# Generated by Django 5.0.1 on 2024-01-08 19:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Product_Name')),
                ('price', models.FloatField()),
                ('detail', models.CharField(max_length=100, verbose_name='Product_Detail')),
                ('cat', models.IntegerField(choices=[(1, 'Clothes'), (2, 'Mobile'), (3, 'Shoes')], verbose_name='Category')),
                ('is_active', models.BooleanField(default=True)),
                ('pimage', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('cprice', models.FloatField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ommoprettyapp.product')),
            ],
        ),
    ]
