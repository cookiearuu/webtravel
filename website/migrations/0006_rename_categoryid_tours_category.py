# Generated by Django 4.0.1 on 2023-04-28 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_category_tours_categoryid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tours',
            old_name='categoryid',
            new_name='category',
        ),
    ]
