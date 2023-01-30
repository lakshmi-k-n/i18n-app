# Generated by Django 3.2.16 on 2023-01-30 00:05

from django.db import migrations, models
import django.db.models.deletion
import django_jsonform.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', django_jsonform.models.fields.JSONField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_genres', to='books.bookgenre')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]