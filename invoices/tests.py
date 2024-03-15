from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Invoice, InvoiceDetail

# Create your tests here.

class InvoiceTests(APITestCase):
    def test_create_invoice_with_details(self):
        data = {
            'date': '2024-03-15',
            'customer_name': 'Test Customer',
            'details': [
                {
                    'description': 'Test Description',
                    'quantity': 2,
                    'unit_price': '10.00',
                    'price': '20.00'
                }
            ]
        }
        response = self.client.post('/api/invoices/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(InvoiceDetail.objects.count(), 1)
        self.assertEqual(InvoiceDetail.objects.first().invoice.customer_name, 'Test Customer')


