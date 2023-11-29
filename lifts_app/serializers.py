from rest_framework import serializers

from . import models


class frequently_used_liftsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.frequently_used_lifts
        fields = [
            "created",
            "last_updated",
            "lift",
        ]

class liftSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.lift
        fields = [
            "last_updated",
            "vendor_code",
            "is_booked",
            "state",
            "created",
            "price",
        ]

class lift_imagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.lift_images
        fields = [
            "last_updated",
            "created",
            "image",
            "lift",
        ]

class lift_infoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.lift_info
        fields = [
            "created",
            "description",
            "last_updated",
            "lift",
        ]

class reportSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.report
        fields = [
            "date",
            "last_updated",
            "sales_amount",
            "created",
            "expenses",
            "manager",
            "requests",
            "frequently_used_lifts",
        ]



class status_requestSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.status_request
        fields = [
            "last_updated",
            "name",
            "created",
        ]

class CustomUserSerializer(serializers.ModelSerializer):

    favorite_lifts = liftSerializer(many=True, read_only=False)

    class Meta:
        model = models.CustomUser
        fields = [
            "phone_number",
            "second_name",
            "favorite_lifts",
            
        ]

class requestsSerializer(serializers.ModelSerializer):

    manager = CustomUserSerializer(many=False, read_only=True)
    customer = CustomUserSerializer(many=False, read_only=True)

    class Meta:
        model = models.requests
        fields = [
            "date_closed",
            "price",
            "created",
            "date_booking",
            "last_updated",
            "customer",
            "manager",
            "status",
            "reports",
        ]
