# Generated by Django 3.1.3 on 2021-01-28 11:44

import app.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20210128_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicules',
            name='image10_vehicule',
            field=models.ImageField(storage=app.storage.OverwriteStorage(), upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='image1_vehicule',
            field=models.ImageField(storage=app.storage.OverwriteStorage(), upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='image2_vehicule',
            field=models.ImageField(storage=app.storage.OverwriteStorage(), upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='image3_vehicule',
            field=models.ImageField(storage=app.storage.OverwriteStorage(), upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='image4_vehicule',
            field=models.ImageField(storage=app.storage.OverwriteStorage(), upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='image5_vehicule',
            field=models.ImageField(storage=app.storage.OverwriteStorage(), upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='image6_vehicule',
            field=models.ImageField(storage=app.storage.OverwriteStorage(), upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='image7_vehicule',
            field=models.ImageField(storage=app.storage.OverwriteStorage(), upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='image8_vehicule',
            field=models.ImageField(storage=app.storage.OverwriteStorage(), upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='vehicules',
            name='image9_vehicule',
            field=models.ImageField(storage=app.storage.OverwriteStorage(), upload_to='static/images/'),
        ),
    ]
