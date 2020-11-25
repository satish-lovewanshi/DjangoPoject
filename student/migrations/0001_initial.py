# Generated by Django 3.1 on 2020-11-25 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_questions', models.IntegerField()),
                ('attempt', models.IntegerField()),
                ('right', models.IntegerField()),
                ('wrong', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('score', models.IntegerField()),
                ('test_id', models.IntegerField()),
                ('branch', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=100)),
            ],
        ),
    ]
