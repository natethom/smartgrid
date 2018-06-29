# Generated by Django 2.0.5 on 2018-06-27 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0002_auto_20180627_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aggregator',
            fields=[
                ('aggregator_id', models.AutoField(primary_key=True, serialize=False)),
                ('aggregator_consumption', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.AutoField(primary_key=True, serialize=False)),
                ('region_consumption', models.BigIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='aggregator',
            name='region_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.Region'),
        ),
    ]