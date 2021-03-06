# Generated by Django 3.0.8 on 2020-09-03 00:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('status', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="try again! You did't follow\n                                                                the format", regex='^9\\d{9}$')])),
                ('work_number', models.CharField(blank=True, max_length=20)),
                ('home_number', models.CharField(blank=True, max_length=20)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('Alborz', 'Alborz'), ('Ardabil', 'Ardabil'), ('Azerbaijan, East', 'Azerbaijan, East'), ('Azerbaijan, West', 'Azerbaijan, West'), ('Bushehr', 'Bushehr'), ('Chahar Mahaal and Bakhtiari', 'Chahar Mahaal and Bakhtiari'), ('Fars', 'Fars'), ('Gilan', 'Gilan'), ('Golestan', 'Golestan'), ('Hamadan', 'Hamadan'), ('Hormozgān', 'Hormozgān'), ('Ilam', 'Ilam'), ('Isfahan', 'Isfahan'), ('Kerman', 'Kerman'), ('Kermanshah', 'Kermanshah'), ('Khorasan, North', 'Khorasan, North'), ('Khorasan, Razavi', 'Khorasan, Razavi'), ('Khorasan, South ', 'Khorasan, South'), ('Khuzestan', 'Khuzestan'), ('Kohgiluyeh and Boyer - Ahmad', 'Kohgiluyeh and Boyer - Ahmad'), ('Kurdistan', 'Kurdistan'), ('Lorestan', 'Lorestan'), ('Markazi', 'Markazi'), ('Mazandaran', 'Mazandaran'), ('Qazvin', 'Qazvin'), ('Qom', 'Qom'), ('Semnan', 'Semnan'), ('Sistan, and Baluchestan', 'Sistan and Baluchestan'), ('Tehran', 'Tehran'), ('Yazd', 'Yazd'), ('Zanjan', 'Zanjan')], help_text='استان', max_length=30, null=True, verbose_name='استان')),
                ('city', models.CharField(help_text='شهر', max_length=30, null=True, verbose_name='شهر')),
                ('address', models.CharField(max_length=50, null=True, verbose_name='آدرس')),
                ('profile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
