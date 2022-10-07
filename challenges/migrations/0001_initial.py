# Generated by Django 4.1.2 on 2022-10-05 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateField(auto_now_add=True)),
                ('end_time', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('credits', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_received', models.DateField(auto_now_add=True)),
                ('credit_no', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
            ],
            options={
                'ordering': ['-date_received'],
            },
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenges.challenge')),
                ('reward', models.ManyToManyField(to='challenges.reward')),
            ],
        ),
        migrations.AddField(
            model_name='challenge',
            name='rewards',
            field=models.ManyToManyField(to='challenges.reward'),
        ),
    ]
