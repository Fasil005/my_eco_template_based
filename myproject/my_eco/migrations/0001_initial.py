# Generated by Django 3.2.7 on 2021-09-24 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statements',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField()),
                ('type', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100)),
                ('balance', models.FloatField()),
            ],
        ),
    ]