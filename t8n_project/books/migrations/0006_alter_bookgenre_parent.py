# Generated by Django 3.2.16 on 2023-01-30 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_bookgenre_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookgenre',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_genres', to='books.bookgenre'),
        ),
    ]