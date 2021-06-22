# Generated by Django 3.2.3 on 2021-06-17 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_nm', models.CharField(default='', max_length=200)),
                ('cust_em', models.EmailField(default='', max_length=200)),
                ('cust_con', models.CharField(default='', max_length=50)),
                ('cust_add1', models.TextField(default='')),
                ('cust_add2', models.TextField(default='')),
                ('cust_pass', models.CharField(default='', max_length=200)),
                ('cust_regi_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('cust_profile', models.ImageField(blank=True, default='', max_length=300, null=True, upload_to='Cust_Pic/')),
                ('comp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company_details')),
            ],
        ),
        migrations.CreateModel(
            name='Company_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_nm', models.CharField(default='', max_length=200)),
                ('prod_price', models.PositiveIntegerField(default=0)),
                ('prod_qty', models.PositiveIntegerField(default=0)),
                ('prod_img', models.ImageField(blank=True, default='', max_length=300, null=True, upload_to='ProductPic/')),
                ('comp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company_details')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=0)),
                ('tot_price', models.PositiveIntegerField(default=0)),
                ('order_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(default='False', max_length=200)),
                ('comp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company_details')),
                ('cust', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company_customers')),
                ('prod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company_product')),
            ],
        ),
    ]
