# Generated by Django 4.2.5 on 2023-09-23 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('secondname', models.CharField(max_length=20)),
                ('age', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Clinicaldata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componentName', models.CharField(choices=[('hw', 'Height/Weight'), ('bp', 'Blood Pressure'), ('heartrate', 'Heart Rate')], max_length=20)),
                ('componentsValue', models.CharField(max_length=20)),
                ('measureDateTime', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicapp.patient')),
            ],
        ),
    ]