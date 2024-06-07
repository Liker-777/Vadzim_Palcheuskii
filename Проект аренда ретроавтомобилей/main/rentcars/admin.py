from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Car, Feedback, UserClient
# Register your models here.

class FilterUsd(admin.SimpleListFilter):
    title = 'Price'
    parameter_name = 'price_usd'

    def lookups(self, request, model_admin):
        return[
            ('700 и более','Высокая цена'),
            ('от 350 до 700','Средняя цена'),
            ('менее 350','Низкая цена')
        ]


    def queryset(self, request, queryset: QuerySet):
        if self.value() =='700 и более':
            return queryset.filter(price_usd__gte=700)
        if self.value() =='от 350 до 700':
            return queryset.filter(price_usd__gte=350).filter(price_usd__lt=700)
        if self.value() =='менее 350':
            return queryset.filter(price_usd__lt=350)

        return queryset

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('make','model')}
    list_display = ['make','model','vin','engine','transmission','year','price_usd','status']
    list_editable =['price_usd', 'status']
    ordering =['make', 'model']
    list_per_page = 8
    search_fields = ['make','model']
    list_filter = ['make',FilterUsd]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['time','name','surname','email','feedback']
    ordering =['time']
    list_per_page = 10


@admin.register(UserClient)
class UserClientAdmin(admin.ModelAdmin):
    list_display = ['time','name','codphone','phone', 'ClientChoice']
    ordering =['time']
    list_per_page = 6