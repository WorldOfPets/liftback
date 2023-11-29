from rest_framework import viewsets, permissions

from . import serializers
from . import models


class frequently_used_liftsViewSet(viewsets.ModelViewSet):
    """ViewSet for the frequently_used_lifts class"""

    queryset = models.frequently_used_lifts.objects.all()
    serializer_class = serializers.frequently_used_liftsSerializer
    permission_classes = [permissions.IsAuthenticated]


class liftViewSet(viewsets.ModelViewSet):
    """ViewSet for the lift class"""

    queryset = models.lift.objects.all()
    serializer_class = serializers.liftSerializer
    permission_classes = [permissions.IsAuthenticated]


class lift_imagesViewSet(viewsets.ModelViewSet):
    """ViewSet for the lift_images class"""

    queryset = models.lift_images.objects.all()
    serializer_class = serializers.lift_imagesSerializer
    permission_classes = [permissions.IsAuthenticated]


class lift_infoViewSet(viewsets.ModelViewSet):
    """ViewSet for the lift_info class"""

    queryset = models.lift_info.objects.all()
    serializer_class = serializers.lift_infoSerializer
    permission_classes = [permissions.IsAuthenticated]


class reportViewSet(viewsets.ModelViewSet):
    """ViewSet for the report class"""

    queryset = models.report.objects.all()
    serializer_class = serializers.reportSerializer
    permission_classes = [permissions.IsAuthenticated]


class requestsViewSet(viewsets.ModelViewSet):
    """ViewSet for the requests class"""

    queryset = models.requests.objects.all()
    serializer_class = serializers.requestsSerializer
    permission_classes = [permissions.IsAuthenticated]


class status_requestViewSet(viewsets.ModelViewSet):
    """ViewSet for the status_request class"""

    queryset = models.status_request.objects.all()
    serializer_class = serializers.status_requestSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomUserViewSet(viewsets.ModelViewSet):
    """ViewSet for the CustomUser class"""

    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
