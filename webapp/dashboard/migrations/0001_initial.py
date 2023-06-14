# Generated by Django 4.2.2 on 2023-06-14 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('adress', models.CharField(max_length=225)),
                ('gender', models.CharField(choices=[('laki-laki', 'laki-laki'), ('perempuan', 'perempuan')], max_length=225)),
                ('employeeType', models.CharField(choices=[('pembina - I/A', 'pembina - I/A'), ('pembina - II/A', 'pembina - II/A'), ('pembina - III/A', 'pembina - I/IIA'), ('pembina - II/B', 'pembina - II/B'), ('penata - I/A', 'penata - I/A'), ('penata - II/A', 'penata - II/A'), ('penata - II/B', 'penata - II/B'), ('penata - III/C', 'penata - IIICA')], max_length=50)),
            ],
        ),
    ]