# Generated by Django 3.2.7 on 2021-10-02 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_alter_position_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]