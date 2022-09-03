# Generated by Django 4.1 on 2022-09-03 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatApp', '0007_alter_cats_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cats',
            name='Age',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='employees',
            name='Pay',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
