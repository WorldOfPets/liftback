from django.contrib import admin
from django import forms

from . import models


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
    readonly_fields = [
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
        "description",
        "last_updated",
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


class requestsAdmin(admin.ModelAdmin):
    form = requestsAdminForm
    list_display = [
        "date_closed",
        "price",
        "created",
        "date_booking",
        "last_updated",
    ]
    readonly_fields = [
        "date_closed",
        "price",
        "created",
        "date_booking",
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
        "name",
        "created",
    ]


class CustomUserAdminForm(forms.ModelForm):

    class Meta:
        model = models.CustomUser
        fields = "__all__"


class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserAdminForm
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
