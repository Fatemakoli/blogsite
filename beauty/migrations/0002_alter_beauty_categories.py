# Generated by Django 3.2.5 on 2021-08-21 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20210818_2108'),
        ('beauty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beauty',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.category'),
        ),
    ]
