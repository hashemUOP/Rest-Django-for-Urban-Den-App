# Generated by Django 5.2.4 on 2025-07-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewsmodels',
            name='review_user',
        ),
        migrations.AddField(
            model_name='reviewsmodels',
            name='firestore_user_uid',
            field=models.CharField(default='whzTBWGXyzO9IErTWtbwkfF3inn2', max_length=300),
            preserve_default=False,
        ),
    ]
