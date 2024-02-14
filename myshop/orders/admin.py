import csv
import datetime
from django.http import HttpResponse
from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Order, OrderItem


def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=orders.csv'
    writer = csv.writer(response)

    # Write header row
    writer.writerow([
        'Order ID',
        'Customer Name',
        'Customer Address',
        'Ordered Date',
        'Product Name',
        'Price',
        'Quantity',
        'Total Price'
    ])

    # Write data rows
    for order in queryset:
        for item in order.items.all():
            writer.writerow([
                order.id,
                f"{order.first_name} ",
                order.address,
                order.created.strftime('%d/%m/%Y'),
                item.product.name,
                item.price,
                item.quantity,
                item.get_cost()
            ])

    return response

export_to_csv.short_description = 'Export to CSV'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


def order_pdf(obj):
    url = reverse('orders:admin_order_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')
order_pdf.short_description = 'Invoice'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name',
                    'address', order_pdf, 'paid', 'phone',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    search_fields = ['first_name', 'address', 'phone']
    inlines = [OrderItemInline]
    actions = [export_to_csv]


