# Generated by Django 3.0.4 on 2020-04-22 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('nome', models.CharField(max_length=250)),
                ('cpf', models.CharField(max_length=14)),
                ('email', models.CharField(max_length=250)),
                ('dataNascimento', models.CharField(max_length=250)),
                ('sexo', models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=1)),
                ('objetivo', models.CharField(max_length=240)),
                ('problema_de_saude', models.CharField(max_length=350)),
                ('ha_quanto_tempo', models.CharField(max_length=240)),
                ('como_se_encontra', models.CharField(max_length=540)),
                ('medicamento_utilizado', models.CharField(max_length=540)),
                ('fumante', models.CharField(choices=[('N', 'Não'), ('S', 'Sim')], default='N', max_length=3)),
                ('bebida_alcoolica', models.CharField(max_length=240)),
                ('habitos_alimentares', models.CharField(max_length=540)),
                ('suplementos', models.CharField(max_length=540)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ficha_fisica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('medida_costas', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('medida_peito', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('medida_abdome', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('medida_tricpes', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('medida_biceps', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('medida_antibraco', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('medida_coxa', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('medida_panturrilha', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('medida_peso', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('percentual_gordura', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Aluno')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
