# Generated by Django 4.2.4 on 2023-08-28 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedFox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogos',
            name='horario',
            field=models.DateField(default=1, null=''),
            preserve_default=False,
        ),
    ]
