# Generated by Django 3.2.4 on 2021-06-30 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_vacation_packing'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='packing',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='packing',
            name='category',
            field=models.CharField(choices=[('B', 'BOTTOMS'), ('T', 'TOPS')], default='B', max_length=10),
        ),
    ]
