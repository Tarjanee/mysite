# Generated by Django 4.2.5 on 2023-11-01 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_contact_city_alter_contact_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(default='', max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
    ]