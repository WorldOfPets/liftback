from django.contrib import admin
from django import forms
import csv
from django.http import HttpResponse
from django.contrib.auth.admin import UserAdmin
from . import models

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        data = []
        for i in field_names:
            data.append(i)
        writer.writerow(data)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

class frequently_used_liftsAdminForm(forms.ModelForm):

    class Meta:
        model = models.frequently_used_lifts
        fields = "__all__"


class frequently_used_liftsAdmin(admin.ModelAdmin):
    form = frequently_used_liftsAdminForm
    list_display = [
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class liftAdminForm(forms.ModelForm):

    class Meta:
        model = models.lift
        fields = "__all__"


class liftAdmin(admin.ModelAdmin):
    form = liftAdminForm
    list_display = [
        "last_updated",
        "vendor_code",
        "is_booked",
        "state",
        "created",
        "price",
    ]


class lift_imagesAdminForm(forms.ModelForm):

    class Meta:
        model = models.lift_images
        fields = "__all__"


class lift_imagesAdmin(admin.ModelAdmin):
    form = lift_imagesAdminForm
    list_display = [
        "last_updated",
        "created",
        "image",
    ]


class lift_infoAdminForm(forms.ModelForm):

    class Meta:
        model = models.lift_info
        fields = "__all__"


class lift_infoAdmin(admin.ModelAdmin):
    form = lift_infoAdminForm
    list_display = [
        "created",
        "description",
        "last_updated",
    ]
    readonly_fields = [
        "created",
    ]


class reportAdminForm(forms.ModelForm):

    class Meta:
        model = models.report
        fields = "__all__"


class reportAdmin(admin.ModelAdmin):
    form = reportAdminForm
    list_display = [
        "date",
        "last_updated",
        "sales_amount",
        "created",
        "expenses",
    ]
    readonly_fields = [
        "date",
        "last_updated",
        "sales_amount",
        "created",
        "expenses",
    ]


class requestsAdminForm(forms.ModelForm):

    class Meta:
        model = models.requests
        fields = "__all__"


class requestsAdmin(admin.ModelAdmin, ExportCsvMixin):
    form = requestsAdminForm
    list_display = [
        "id",
        "price",
        "lift",
        "customer",
        "manager",
        "status",
    ]
    list_display_links = ["id", "price"]
    #prepopulated_fields = ["customer", "manager"]
    list_select_related = ["lift"]
    list_filter = ["status"]
    search_fields = ["price", "id", "lift__vendor_code"]
    actions = ["export_as_csv"]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class status_requestAdminForm(forms.ModelForm):

    class Meta:
        model = models.status_request
        fields = "__all__"


class status_requestAdmin(admin.ModelAdmin):
    form = status_requestAdminForm
    list_display = [
        "last_updated",
        "name",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]





class CustomUserAdmin(UserAdmin):
    list_display = [
        "username",
        "email",
    ]


admin.site.register(models.frequently_used_lifts, frequently_used_liftsAdmin)
admin.site.register(models.lift, liftAdmin)
admin.site.register(models.lift_images, lift_imagesAdmin)
admin.site.register(models.lift_info, lift_infoAdmin)
admin.site.register(models.report, reportAdmin)
admin.site.register(models.requests, requestsAdmin)
admin.site.register(models.status_request, status_requestAdmin)
admin.site.register(models.CustomUser, CustomUserAdmin)
