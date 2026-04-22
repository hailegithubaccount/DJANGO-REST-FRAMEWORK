# import django_filters
# from api.models import Product
# from rest_framework import filters

# class InStockFilterBackend(filters.BaseFilterBackend):
#     def filter_queryset(self, request, queryset, view):
#         return queryset.filter(stock__gt=0)

#         # if it's filter = it displayed all products but not the stock is zero
#         #if it's exculded= it displayed the stock is zero



# class ProductFilter(django_filters.FilterSet):
#     class Meta:
#         model = Product
#         fields = {
#             'name': ['iexact', 'icontains'], 
#             'price': ['exact', 'lt', 'gt', 'range']
#         }