# Generated by Django 3.2.7 on 2021-10-02 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_alter_position_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
