# Generated by Django 3.1.2 on 2020-10-14 21:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20201014_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacaMadre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Codigo unido del producto', primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('frecuencia', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
