# Generated by Django 2.0 on 2020-06-07 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]
