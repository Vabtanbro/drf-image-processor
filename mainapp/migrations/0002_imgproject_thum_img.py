# Generated by Django 4.0.3 on 2022-12-31 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imgproject',
            name='thum_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
