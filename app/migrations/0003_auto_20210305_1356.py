# Generated by Django 2.2 on 2021-03-05 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210305_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='headre_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]