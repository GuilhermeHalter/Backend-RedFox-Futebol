# Generated by Django 4.2.4 on 2023-08-28 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RedFox', '0002_jogos_horario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogos',
            name='horario',
        ),
    ]