# Generated by Django 4.1.2 on 2022-11-30 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aspirante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('tipo_documento', models.CharField(max_length=100, verbose_name='Tipo de documento')),
                ('numero_documento', models.CharField(max_length=100, unique=True, verbose_name='Documento de identidad')),
                ('profesion', models.CharField(max_length=100, verbose_name='Profesión')),
                ('ciudad', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('edad', models.IntegerField(default=0, verbose_name='Edad')),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Apellido')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoAdmision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluacionAdmision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha de evaluación')),
                ('puntos_cv', models.IntegerField(default=0, verbose_name='Puntos Hoja de Vida')),
                ('puntos_experiencias', models.IntegerField(default=0, verbose_name='Puntos Hoja de Vida')),
                ('puntos_postgrados', models.IntegerField(default=0, verbose_name='Puntos Postgrados')),
                ('puntos_certificaciones', models.IntegerField(default=0, verbose_name='Puntos Certificaciones')),
                ('puntos_ingles', models.IntegerField(default=0, verbose_name='Puntos Ingles')),
                ('total_puntos', models.IntegerField(default=0, verbose_name='Total Puntos')),
                ('admision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admision', to='aspirante.estadoadmision')),
                ('aspirante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aspirante', to='aspirante.aspirante')),
                ('cargo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cargo', to='aspirante.cargo')),
            ],
        ),
    ]