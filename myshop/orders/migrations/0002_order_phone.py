# Generated by Django 4.1.13 on 2024-02-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=998, max_length=50),
            preserve_default=False,
        ),
    ]
