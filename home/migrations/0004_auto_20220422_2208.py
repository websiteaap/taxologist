# Generated by Django 3.2.11 on 2022-04-22 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220422_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing_plan',
            name='pr_img1',
            field=models.ImageField(blank=True, null=True, upload_to='pricing_plan_image/preferred_plan_image1/'),
        ),
        migrations.AlterField(
            model_name='pricing_plan',
            name='pr_img2',
            field=models.ImageField(blank=True, null=True, upload_to='pricing_plan_image/preferred_plan_image2/'),
        ),
        migrations.AlterField(
            model_name='pricing_plan',
            name='pr_img3',
            field=models.ImageField(blank=True, null=True, upload_to='pricing_plan_image/preferred_plan_image3/'),
        ),
    ]
