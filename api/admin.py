from django.contrib import admin
from api.models import Order, OrderItem, User

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'status', 'created_at')
    list_editable = ('status',)
    inlines = [
        OrderItemInline
    ]
    actions = ['mark_as_confirmed', 'mark_as_cancelled']

    def mark_as_confirmed(self, request, queryset):
        queryset.update(status=Order.StatusChoices.CONFIRMED)
    mark_as_confirmed.short_description = "Mark selected orders as Confirmed"

    def mark_as_cancelled(self, request, queryset):
        queryset.update(status=Order.StatusChoices.CANCELLED)
    mark_as_cancelled.short_description = "Mark selected orders as Cancelled"

admin.site.register(Order, OrderAdmin)
admin.site.register(User)