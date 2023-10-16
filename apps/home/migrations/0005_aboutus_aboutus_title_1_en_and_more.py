# Generated by Django 4.0.3 on 2022-03-21 09:12

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_aboutus_banner_desc_1_en_aboutus_banner_desc_1_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='aboutus_title_1_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Блок №1'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='aboutus_title_1_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Блок №1'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='aboutus_title_2_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Блок №2'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='aboutus_title_2_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Блок №2'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='aboutus_title_3_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Блок №3'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='aboutus_title_3_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Блок №3'),
        ),
    ]