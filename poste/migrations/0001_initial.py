# Generated by Django 4.0.4 on 2022-04-20 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tache', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('tache', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tache.taches')),
            ],
        ),
    ]