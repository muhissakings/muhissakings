# Generated by Django 4.0.5 on 2022-06-22 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('username', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField()),
                ('location', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'trainees',
            },
        ),
    ]
