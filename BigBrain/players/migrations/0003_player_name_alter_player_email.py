# Generated by Django 4.0 on 2021-12-24 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_alter_player_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='name',
            field=models.CharField(default='Player', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
