# Generated by Django 5.0.1 on 2024-02-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_proxy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
