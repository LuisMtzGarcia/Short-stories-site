# Generated by Django 3.2.9 on 2021-11-26 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('short_stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='short_stories.genre'),
        ),
    ]
