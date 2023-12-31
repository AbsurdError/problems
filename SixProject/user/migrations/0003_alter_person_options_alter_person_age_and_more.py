# Generated by Django 4.2.7 on 2023-12-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_person_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Человека', 'verbose_name_plural': 'Люди'},
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(default=1, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthDay',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.BooleanField(verbose_name='Гендер'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='person',
            name='surname',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
    ]
