# Generated by Django 3.2.11 on 2022-04-24 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_auto_20220324_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business_income_tax_dashbaord_json_file',
            name='xmlfile',
        ),
        migrations.AddField(
            model_name='business_income_tax_dashbaord_json_file',
            name='json_file',
            field=models.FileField(default='a', upload_to='business_income_tax/xml_file/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='business_gst_dashbaord_xmlfile',
            name='json_file',
            field=models.FileField(upload_to='business_dashbaord/gst/'),
        ),
        migrations.AlterField(
            model_name='business_income_tax_dashbaord_xmlfile',
            name='xmlfile',
            field=models.FileField(upload_to='business_income_tax/xml_file/'),
        ),
        migrations.AlterField(
            model_name='gst_dashbaord_data',
            name='gst3_pdf',
            field=models.FileField(blank=True, null=True, upload_to='GST3/'),
        ),
    ]
