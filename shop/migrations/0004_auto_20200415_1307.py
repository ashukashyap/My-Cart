# Generated by Django 3.0.4 on 2020-04-15 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=110)),
                ('address', models.CharField(max_length=110)),
                ('city', models.CharField(max_length=110)),
                ('state', models.CharField(max_length=110)),
                ('zip_code', models.CharField(max_length=110)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.CharField(default='', max_length=500),
        ),
    ]
