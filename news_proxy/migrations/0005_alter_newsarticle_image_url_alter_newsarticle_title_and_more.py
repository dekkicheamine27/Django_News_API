# Generated by Django 5.0.1 on 2024-02-03 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_proxy', '0004_alter_newsarticle_image_url_alter_newsarticle_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='image_url',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='url',
            field=models.URLField(max_length=500),
        ),
    ]
