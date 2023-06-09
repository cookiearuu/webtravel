# Generated by Django 4.0.1 on 2023-03-25 15:43

from django.db import migrations, models
import django.db.models.deletion
import website.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='touragencies',
            fields=[
                ('name', models.CharField(max_length=50, unique=True)),
                ('BIN', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phonenumber', models.IntegerField(unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tours',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('place', models.CharField(max_length=100)),
                ('transport', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=10)),
                ('description', models.TextField(max_length=2000)),
                ('image', models.ImageField(upload_to=website.models.get_file_path)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('agency', models.ForeignKey(default=874516, on_delete=django.db.models.deletion.CASCADE, to='website.touragencies')),
            ],
        ),
    ]
