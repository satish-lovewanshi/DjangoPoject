# Generated by Django 3.1 on 2020-10-28 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_number', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=200)),
                ('mobile', models.IntegerField(unique=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logins.branch')),
                ('college_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logins.code')),
            ],
        ),
        migrations.CreateModel(
            name='StudentReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('roll_number', models.CharField(max_length=100)),
                ('mobile', models.IntegerField(unique=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logins.branch')),
                ('college_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logins.code')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logins.year')),
            ],
        ),
    ]