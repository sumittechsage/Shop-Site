# Generated by Django 3.2.9 on 2024-05-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20240502_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='item', to='menu.Category'),
        ),
    ]
