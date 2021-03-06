# Generated by Django 3.1.2 on 2020-10-15 18:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_gabinete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitore',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Codigo unico del producto', primary_key=True, serialize=False)),
                ('marca', models.CharField(choices=[('s', 'Seleccione'), ('a', 'Aorus'), ('d', 'Dell'), ('o', 'Ozone')], default='s', help_text='Marca del producto', max_length=1)),
                ('modelo', models.CharField(max_length=50)),
                ('pulgadas', models.CharField(choices=[('sele', 'Seleccione'), ('23.0', '23.0"'), ('24.0', '24.0"'), ('25.0', '25.0"'), ('26.0', '26.0"'), ('27.0', '27.0"')], default='sele', help_text='Pulgadas del monitor', max_length=4)),
                ('resolucion', models.CharField(max_length=50)),
                ('tiempo_respuesta', models.CharField(choices=[('s', 'Seleccione'), ('1', '1 ms'), ('2', '2 ms'), ('3', '3 ms'), ('4', '4 ms')], default='s', help_text='Tiempo de respuesta del monitor', max_length=1)),
                ('tasa_refresco', models.CharField(choices=[('sel', 'Seleccione'), ('120', '120 Hz'), ('144', '144 Hz'), ('165', '165 Hz')], default='sel', help_text='Tasa de refresco del monitor', max_length=3)),
                ('precio', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='Almacenamieto',
            new_name='Almacenamiento',
        ),
        migrations.RenameModel(
            old_name='FuentePoder',
            new_name='FuentesPoder',
        ),
        migrations.RenameModel(
            old_name='PlacaMadre',
            new_name='PlacasMadre',
        ),
        migrations.RenameModel(
            old_name='Procesador',
            new_name='Procesadore',
        ),
    ]
