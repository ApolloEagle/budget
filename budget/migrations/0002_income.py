# Generated by Django 3.0.5 on 2020-05-16 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.DecimalField(decimal_places=2, max_digits=16)),
            ],
        ),
    ]
