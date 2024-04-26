# Generated by Django 3.2.23 on 2023-11-14 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Обслуживается'), ('o', 'Выдана читателю'), ('a', 'Доступна'), ('r', 'Забронирована')], default='m', help_text='Забронировать наличие.', max_length=1),
        ),
    ]
