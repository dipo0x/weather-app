# Generated by Django 3.2.7 on 2021-09-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=96, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
