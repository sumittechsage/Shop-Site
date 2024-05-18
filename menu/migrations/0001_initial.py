# Generated by Django 3.2.9 on 2024-05-18 13:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='ITEM NAME')),
                ('price', models.PositiveIntegerField(verbose_name='ITEM PRICE')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='SOFT DELETE ITEM')),
                ('category', models.ManyToManyField(blank=True, related_name='item', to='menu.Category')),
            ],
        ),
    ]
