# Generated by Django 4.0.4 on 2022-05-21 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=255)),
                ('cidade', models.CharField(default='saopaulo', max_length=50)),
                ('sexo', models.CharField(max_length=1)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('sobre', models.TextField()),
                ('danca', models.CharField(max_length=2)),
                ('viagem', models.CharField(max_length=2)),
                ('cozinhar', models.CharField(max_length=2)),
                ('filmes', models.CharField(max_length=2)),
                ('barzinhos', models.CharField(max_length=2)),
                ('shows', models.CharField(max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='media')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
