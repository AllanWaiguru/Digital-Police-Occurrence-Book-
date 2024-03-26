# Generated by Django 5.0.3 on 2024-03-26 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='messgae',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='customuser',
            name='subject',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]