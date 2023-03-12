# Generated by Django 4.1.7 on 2023-03-08 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CEntry',
            fields=[
                ('coordinate_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=11)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=11)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tb_coordinates',
            },
        ),
    ]