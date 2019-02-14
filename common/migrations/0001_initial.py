# Generated by Django 2.1.7 on 2019-02-14 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draw', models.IntegerField(blank=True, null=True)),
                ('draw_date', models.DateField(blank=True, null=True)),
                ('num1', models.IntegerField(blank=True, null=True)),
                ('num2', models.IntegerField(blank=True, null=True)),
                ('num3', models.IntegerField(blank=True, null=True)),
                ('num4', models.IntegerField(blank=True, null=True)),
                ('num5', models.IntegerField(blank=True, null=True)),
                ('num6', models.IntegerField(blank=True, null=True)),
                ('powerball', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'base',
                'verbose_name_plural': 'base',
                'db_table': 'base',
            },
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('counts', models.IntegerField()),
                ('depth', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'populations',
                'verbose_name_plural': 'populations',
                'db_table': 'populations',
            },
        ),
    ]
