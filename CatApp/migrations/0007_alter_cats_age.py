# Generated by Django 4.1 on 2022-09-03 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatApp', '0006_alter_cats_dateofarrival_alter_employees_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cats',
            name='Age',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
