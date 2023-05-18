# Generated by Django 4.2.1 on 2023-05-09 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=25)),
                ('weight', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]
