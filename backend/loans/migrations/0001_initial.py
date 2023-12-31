# Generated by Django 4.2.4 on 2023-08-09 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoanCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LoanProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Loan Provider Name')),
                ('total_funds', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Total Funds')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Loan Amount')),
                ('min_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Minimum Loan Amount')),
                ('max_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Maximum Loan Amount')),
                ('duration', models.PositiveIntegerField(verbose_name='Loan Duration in months')),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Interest Rate')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('loan_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans_customer', to='loans.loancustomer')),
                ('loan_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans_provider', to='loans.loanprovider')),
            ],
        ),
        migrations.CreateModel(
            name='AmortizationTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installment_number', models.PositiveIntegerField(verbose_name='Installment Numbers')),
                ('payment_date', models.DateField(verbose_name='Payment Date')),
                ('principal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Principal Value')),
                ('interest', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Interst')),
                ('total_payment', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Payment')),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.loan')),
            ],
        ),
    ]
