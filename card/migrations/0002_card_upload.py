# Generated by Django 4.0.6 on 2022-08-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='upload',
            field=models.ImageField(default='../default/duplex.jpeg', upload_to='uploads/'),
        ),
    ]