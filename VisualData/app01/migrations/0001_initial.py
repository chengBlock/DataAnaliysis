# Generated by Django 3.1.5 on 2021-01-14 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=8)),
                ('pwd', models.CharField(max_length=300)),
            ],
        ),
    ]