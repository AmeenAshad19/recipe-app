# Generated by Django 5.1 on 2024-08-23 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('ingredients', models.JSONField()),
                ('instructions', models.JSONField()),
                ('search_tags', models.JSONField()),
                ('is_vegetarian', models.BooleanField(default=False)),
                ('image_name', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
