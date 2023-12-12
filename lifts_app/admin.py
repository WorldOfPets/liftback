from django.contrib import admin
from django import forms
import csv
from django.http import HttpResponse
from django.contrib.auth.admin import UserAdmin
from . import models
import pygsheets
import pandas as pd


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        gc = pygsheets.authorize(service_file='creds.json')
        df = pd.DataFrame()
        field_names = [field.name for field in meta.fields]
        for i in field_names:
            df[f'{i}'] = [getattr(obj, i) for obj in queryset]
        sh = gc.open('testpython')
        #select the first sheet 
        wks = sh[0]
        #update the first sheet with df, starting at cell B2. 
        wks.set_dataframe(df,(1,1))

    export_as_csv.short_description = "Export Selected"

class frequently_used_liftsAdminForm(forms.ModelForm):

    class Meta:
        model = models.frequently_used_lifts
        fields = "__all__"


class frequently_used_liftsAdmin(admin.ModelAdmin):
    form = frequently_used_liftsAdminForm
    list_display = [
        "id",
        "lift",
        "count",
    ]
    list_display_links = ["lift"]
    list_editable = ["count"]
    list_filter = ["lift"]
    search_fields = ["lift__vendor_code"]


class liftAdminForm(forms.ModelForm):

    class Meta:
        model = models.lift
        fields = "__all__"


class liftAdmin(admin.ModelAdmin):
    form = liftAdminForm
    list_display = [
        "id",
        "vendor_code",
        "is_booked",
        "state",
        "price",
    ]
    list_display_links = ["id", "vendor_code"]
    list_editable = ["is_booked"]
    list_filter = ["is_booked", "state", "price"]
    search_fields = ["vendor_code"]


class lift_imagesAdminForm(forms.ModelForm):

    class Meta:
        model = models.lift_images
        fields = "__all__"


class lift_imagesAdmin(admin.ModelAdmin):
    form = lift_imagesAdminForm
    list_display = [
        "id",
        "created",
    ]
    list_display_links = [ "id",
        "created",]


class lift_infoAdminForm(forms.ModelForm):

    class Meta:
        model = models.lift_info
        fields = "__all__"


class lift_infoAdmin(admin.ModelAdmin):
    form = lift_infoAdminForm
    list_display = [
        "id",
        "description",
    ]
    list_display_links = ["id", "description"]
    search_fields = ["description"]


class reportAdminForm(forms.ModelForm):

    class Meta:
        model = models.report
        fields = "__all__"


class reportAdmin(admin.ModelAdmin):
    form = reportAdminForm
    list_display = [
        "id",
        "manager",
        "last_updated",
        "sales_amount",
        "created",
        "expenses",
    ]
    list_display_links = ["id", "manager"]
    list_filter = ["manager", "date", "created"]
    search_fields = ["manager__username"]


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
    list_display_links = ["id", "lift"]
    #prepopulated_fields = ["customer", "manager"]
    list_select_related = ["lift"]
    list_filter = ["status"]
    search_fields = ["price", "id", "lift__vendor_code"]
    actions = ["export_as_csv"]


class status_requestAdminForm(forms.ModelForm):

    class Meta:
        model = models.status_request
        fields = "__all__"


class status_requestAdmin(admin.ModelAdmin):
    form = status_requestAdminForm
    list_display =  ["id", "name"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]





class CustomUserAdmin(UserAdmin):
    list_display = [
        "id",
        "username",
        "email",
        "is_superuser",
        "is_staff",
        "is_active",
    ]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Персональная информация", {"fields": ("first_name", "last_name", "email", "favorite_lifts")}),
        (
            "Права доступа",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Важные даты", {"fields": ("last_login", "date_joined")}),
    )
    list_filter = ["is_superuser",
        "is_staff",
        "is_active",]
    search_fields = ["username",
        "email"]
    list_editable = ["is_superuser", "is_staff", "is_active"]
    list_display_links = ["id", "username", "email"]


admin.site.register(models.frequently_used_lifts, frequently_used_liftsAdmin)
admin.site.register(models.lift, liftAdmin)
admin.site.register(models.lift_images, lift_imagesAdmin)
admin.site.register(models.lift_info, lift_infoAdmin)
admin.site.register(models.report, reportAdmin)
admin.site.register(models.requests, requestsAdmin)
admin.site.register(models.status_request, status_requestAdmin)
admin.site.register(models.CustomUser, CustomUserAdmin)
