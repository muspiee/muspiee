# Generated by Django 5.0.1 on 2024-02-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('age', models.PositiveIntegerField(default=50)),
                ('gender', models.CharField(blank=True, choices=[('Other', 'Other'), ('Female', 'Female'), ('Male', 'Male')], max_length=8, null=True)),
                ('address', models.CharField(default='n', max_length=200)),
                ('email', models.EmailField(blank=True, max_length=40, null=True)),
                ('mobile_number', models.TextField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]