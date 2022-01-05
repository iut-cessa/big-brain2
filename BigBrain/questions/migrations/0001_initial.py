# Generated by Django 4.0 on 2021-12-18 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('score', models.IntegerField()),
                ('description', models.CharField(max_length=2000)),
                ('answer', models.CharField(max_length=300)),
            ],
        ),
    ]
