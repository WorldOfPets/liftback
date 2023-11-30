from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import api
from . import views


router = routers.DefaultRouter()
router.register("frequently_used_lifts", api.frequently_used_liftsViewSet)
router.register("lift", api.liftViewSet)
router.register("lift_images", api.lift_imagesViewSet)
router.register("lift_info", api.lift_infoViewSet)
router.register("report", api.reportViewSet)
router.register("requests", api.requestsViewSet)
router.register("status_request", api.status_requestViewSet)
router.register("CustomUser", api.CustomUserViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth-token/', include('djoser.urls.authtoken')),
    path("lifts_app/frequently_used_lifts/", views.frequently_used_liftsListView.as_view(), name="lifts_app_frequently_used_lifts_list"),
    path("lifts_app/frequently_used_lifts/create/", views.frequently_used_liftsCreateView.as_view(), name="lifts_app_frequently_used_lifts_create"),
    path("lifts_app/frequently_used_lifts/detail/<int:pk>/", views.frequently_used_liftsDetailView.as_view(), name="lifts_app_frequently_used_lifts_detail"),
    path("lifts_app/frequently_used_lifts/update/<int:pk>/", views.frequently_used_liftsUpdateView.as_view(), name="lifts_app_frequently_used_lifts_update"),
    path("lifts_app/frequently_used_lifts/delete/<int:pk>/", views.frequently_used_liftsDeleteView.as_view(), name="lifts_app_frequently_used_lifts_delete"),
    path("lifts_app/lift/", views.liftListView.as_view(), name="lifts_app_lift_list"),
    path("lifts_app/lift/create/", views.liftCreateView.as_view(), name="lifts_app_lift_create"),
    path("lifts_app/lift/detail/<int:pk>/", views.liftDetailView.as_view(), name="lifts_app_lift_detail"),
    path("lifts_app/lift/update/<int:pk>/", views.liftUpdateView.as_view(), name="lifts_app_lift_update"),
    path("lifts_app/lift/delete/<int:pk>/", views.liftDeleteView.as_view(), name="lifts_app_lift_delete"),
    path("lifts_app/lift_images/", views.lift_imagesListView.as_view(), name="lifts_app_lift_images_list"),
    path("lifts_app/lift_images/create/", views.lift_imagesCreateView.as_view(), name="lifts_app_lift_images_create"),
    path("lifts_app/lift_images/detail/<int:pk>/", views.lift_imagesDetailView.as_view(), name="lifts_app_lift_images_detail"),
    path("lifts_app/lift_images/update/<int:pk>/", views.lift_imagesUpdateView.as_view(), name="lifts_app_lift_images_update"),
    path("lifts_app/lift_images/delete/<int:pk>/", views.lift_imagesDeleteView.as_view(), name="lifts_app_lift_images_delete"),
    path("lifts_app/lift_info/", views.lift_infoListView.as_view(), name="lifts_app_lift_info_list"),
    path("lifts_app/lift_info/create/", views.lift_infoCreateView.as_view(), name="lifts_app_lift_info_create"),
    path("lifts_app/lift_info/detail/<int:pk>/", views.lift_infoDetailView.as_view(), name="lifts_app_lift_info_detail"),
    path("lifts_app/lift_info/update/<int:pk>/", views.lift_infoUpdateView.as_view(), name="lifts_app_lift_info_update"),
    path("lifts_app/lift_info/delete/<int:pk>/", views.lift_infoDeleteView.as_view(), name="lifts_app_lift_info_delete"),
    path("lifts_app/report/", views.reportListView.as_view(), name="lifts_app_report_list"),
    path("lifts_app/report/create/", views.reportCreateView.as_view(), name="lifts_app_report_create"),
    path("lifts_app/report/detail/<int:pk>/", views.reportDetailView.as_view(), name="lifts_app_report_detail"),
    path("lifts_app/report/update/<int:pk>/", views.reportUpdateView.as_view(), name="lifts_app_report_update"),
    path("lifts_app/report/delete/<int:pk>/", views.reportDeleteView.as_view(), name="lifts_app_report_delete"),
    path("lifts_app/requests/", views.requestsListView.as_view(), name="lifts_app_requests_list"),
    path("lifts_app/requests/create/", views.requestsCreateView.as_view(), name="lifts_app_requests_create"),
    path("lifts_app/requests/detail/<int:pk>/", views.requestsDetailView.as_view(), name="lifts_app_requests_detail"),
    path("lifts_app/requests/update/<int:pk>/", views.requestsUpdateView.as_view(), name="lifts_app_requests_update"),
    path("lifts_app/requests/delete/<int:pk>/", views.requestsDeleteView.as_view(), name="lifts_app_requests_delete"),
    path("lifts_app/status_request/", views.status_requestListView.as_view(), name="lifts_app_status_request_list"),
    path("lifts_app/status_request/create/", views.status_requestCreateView.as_view(), name="lifts_app_status_request_create"),
    path("lifts_app/status_request/detail/<int:pk>/", views.status_requestDetailView.as_view(), name="lifts_app_status_request_detail"),
    path("lifts_app/status_request/update/<int:pk>/", views.status_requestUpdateView.as_view(), name="lifts_app_status_request_update"),
    path("lifts_app/status_request/delete/<int:pk>/", views.status_requestDeleteView.as_view(), name="lifts_app_status_request_delete"),
    path("lifts_app/CustomUser/", views.CustomUserListView.as_view(), name="lifts_app_CustomUser_list"),
    path("lifts_app/CustomUser/create/", views.CustomUserCreateView.as_view(), name="lifts_app_CustomUser_create"),
    path("lifts_app/CustomUser/detail/<int:pk>/", views.CustomUserDetailView.as_view(), name="lifts_app_CustomUser_detail"),
    path("lifts_app/CustomUser/update/<int:pk>/", views.CustomUserUpdateView.as_view(), name="lifts_app_CustomUser_update"),
    path("lifts_app/CustomUser/delete/<int:pk>/", views.CustomUserDeleteView.as_view(), name="lifts_app_CustomUser_delete"),

)
