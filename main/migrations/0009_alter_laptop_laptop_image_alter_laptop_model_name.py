# Generated by Django 4.1.3 on 2023-01-04 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_laptop_specs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='laptop_image',
            field=models.ImageField(default='default-laptop.jpg', upload_to='laptop_pics'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='model_name',
            field=models.CharField(max_length=75),
        ),
    ]
