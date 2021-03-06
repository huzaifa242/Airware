# Generated by Django 2.0.3 on 2018-04-05 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=20)),
                ('flightid', models.CharField(max_length=5)),
                ('source', models.CharField(max_length=4)),
                ('destination', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='LiveFlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
                ('flightid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Flight')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('flightid', models.CharField(max_length=5)),
                ('source', models.CharField(max_length=4)),
                ('destination', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('pnr', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('boardstatus', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='passenger',
            name='pnr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livestatus.Status'),
        ),
        migrations.AddField(
            model_name='goods',
            name='pnr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livestatus.Status'),
        ),
    ]
