# Generated by Django 3.2.4 on 2021-07-03 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_merge_20210630_1904'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='packing',
            options={'ordering': ['category']},
        ),
        migrations.AlterField(
            model_name='packing',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vacation',
            name='style',
            field=models.CharField(choices=[('L', 'Luxury'), ('F', 'Family'), ('E', 'Expedition'), ('C', 'Cheap')], default='L', max_length=1),
        ),
        migrations.AlterField(
            model_name='vacation',
            name='transportation',
            field=models.CharField(choices=[('C', 'Car'), ('A', 'Airplane'), ('T', 'Train'), ('B', 'Bike'), ('S', 'Ship')], default='C', max_length=1),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('vacation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.vacation')),
            ],
        ),
    ]