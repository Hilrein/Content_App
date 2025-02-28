# Generated by Django 4.2.19 on 2025-02-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner_app', '0002_content_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
