# Generated by Django 5.2.2 on 2025-06-10 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karunya_app', '0006_remove_testimonial_rating_testimonial_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='title',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]
