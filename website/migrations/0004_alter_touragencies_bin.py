# Generated by Django 4.0.1 on 2023-03-29 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_touragencies_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touragencies',
            name='BIN',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, unique=True),
        ),
    ]