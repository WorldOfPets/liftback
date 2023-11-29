import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_frequently_used_lifts_list_view(client):
    instance1 = test_helpers.create_lifts_app_frequently_used_lifts()
    instance2 = test_helpers.create_lifts_app_frequently_used_lifts()
    url = reverse("lifts_app_frequently_used_lifts_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_frequently_used_lifts_create_view(client):
    lift = test_helpers.create_lifts_app_lift()
    url = reverse("lifts_app_frequently_used_lifts_create")
    data = {
        "lift": lift.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_frequently_used_lifts_detail_view(client):
    instance = test_helpers.create_lifts_app_frequently_used_lifts()
    url = reverse("lifts_app_frequently_used_lifts_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_frequently_used_lifts_update_view(client):
    lift = test_helpers.create_lifts_app_lift()
    instance = test_helpers.create_lifts_app_frequently_used_lifts()
    url = reverse("lifts_app_frequently_used_lifts_update", args=[instance.pk, ])
    data = {
        "lift": lift.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_lift_list_view(client):
    instance1 = test_helpers.create_lifts_app_lift()
    instance2 = test_helpers.create_lifts_app_lift()
    url = reverse("lifts_app_lift_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_lift_create_view(client):
    url = reverse("lifts_app_lift_create")
    data = {
        "vendor_code": "text",
        "is_booked": True,
        "state": "text",
        "price": 1.0f,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_lift_detail_view(client):
    instance = test_helpers.create_lifts_app_lift()
    url = reverse("lifts_app_lift_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_lift_update_view(client):
    instance = test_helpers.create_lifts_app_lift()
    url = reverse("lifts_app_lift_update", args=[instance.pk, ])
    data = {
        "vendor_code": "text",
        "is_booked": True,
        "state": "text",
        "price": 1.0f,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_lift_images_list_view(client):
    instance1 = test_helpers.create_lifts_app_lift_images()
    instance2 = test_helpers.create_lifts_app_lift_images()
    url = reverse("lifts_app_lift_images_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_lift_images_create_view(client):
    lift = test_helpers.create_lifts_app_lift()
    url = reverse("lifts_app_lift_images_create")
    data = {
        "image": "anImage",
        "lift": lift.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_lift_images_detail_view(client):
    instance = test_helpers.create_lifts_app_lift_images()
    url = reverse("lifts_app_lift_images_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_lift_images_update_view(client):
    lift = test_helpers.create_lifts_app_lift()
    instance = test_helpers.create_lifts_app_lift_images()
    url = reverse("lifts_app_lift_images_update", args=[instance.pk, ])
    data = {
        "image": "anImage",
        "lift": lift.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_lift_info_list_view(client):
    instance1 = test_helpers.create_lifts_app_lift_info()
    instance2 = test_helpers.create_lifts_app_lift_info()
    url = reverse("lifts_app_lift_info_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_lift_info_create_view(client):
    lift = test_helpers.create_lifts_app_lift()
    url = reverse("lifts_app_lift_info_create")
    data = {
        "description": "text",
        "lift": lift.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_lift_info_detail_view(client):
    instance = test_helpers.create_lifts_app_lift_info()
    url = reverse("lifts_app_lift_info_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_lift_info_update_view(client):
    lift = test_helpers.create_lifts_app_lift()
    instance = test_helpers.create_lifts_app_lift_info()
    url = reverse("lifts_app_lift_info_update", args=[instance.pk, ])
    data = {
        "description": "text",
        "lift": lift.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_report_list_view(client):
    instance1 = test_helpers.create_lifts_app_report()
    instance2 = test_helpers.create_lifts_app_report()
    url = reverse("lifts_app_report_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_report_create_view(client):
    manager = test_helpers.create_lifts_app_CustomUser()
    requests = test_helpers.create_lifts_app_requests()
    frequently_used_lifts = test_helpers.create_lifts_app_frequently_used_lifts()
    url = reverse("lifts_app_report_create")
    data = {
        "date": datetime.now(),
        "sales_amount": 1.0f,
        "expenses": 1.0f,
        "manager": manager.pk,
        "requests": requests.pk,
        "frequently_used_lifts": frequently_used_lifts.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_report_detail_view(client):
    instance = test_helpers.create_lifts_app_report()
    url = reverse("lifts_app_report_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_report_update_view(client):
    manager = test_helpers.create_lifts_app_CustomUser()
    requests = test_helpers.create_lifts_app_requests()
    frequently_used_lifts = test_helpers.create_lifts_app_frequently_used_lifts()
    instance = test_helpers.create_lifts_app_report()
    url = reverse("lifts_app_report_update", args=[instance.pk, ])
    data = {
        "date": datetime.now(),
        "sales_amount": 1.0f,
        "expenses": 1.0f,
        "manager": manager.pk,
        "requests": requests.pk,
        "frequently_used_lifts": frequently_used_lifts.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_requests_list_view(client):
    instance1 = test_helpers.create_lifts_app_requests()
    instance2 = test_helpers.create_lifts_app_requests()
    url = reverse("lifts_app_requests_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_requests_create_view(client):
    customer = test_helpers.create_lifts_app_CustomUser()
    manager = test_helpers.create_lifts_app_CustomUser()
    status = test_helpers.create_lifts_app_status_request()
    reports = test_helpers.create_lifts_app_report()
    url = reverse("lifts_app_requests_create")
    data = {
        "date_closed": datetime.now(),
        "price": 1.0f,
        "date_booking": datetime.now(),
        "customer": customer.pk,
        "manager": manager.pk,
        "status": status.pk,
        "reports": reports.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_requests_detail_view(client):
    instance = test_helpers.create_lifts_app_requests()
    url = reverse("lifts_app_requests_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_requests_update_view(client):
    customer = test_helpers.create_lifts_app_CustomUser()
    manager = test_helpers.create_lifts_app_CustomUser()
    status = test_helpers.create_lifts_app_status_request()
    reports = test_helpers.create_lifts_app_report()
    instance = test_helpers.create_lifts_app_requests()
    url = reverse("lifts_app_requests_update", args=[instance.pk, ])
    data = {
        "date_closed": datetime.now(),
        "price": 1.0f,
        "date_booking": datetime.now(),
        "customer": customer.pk,
        "manager": manager.pk,
        "status": status.pk,
        "reports": reports.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_status_request_list_view(client):
    instance1 = test_helpers.create_lifts_app_status_request()
    instance2 = test_helpers.create_lifts_app_status_request()
    url = reverse("lifts_app_status_request_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_status_request_create_view(client):
    url = reverse("lifts_app_status_request_create")
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_status_request_detail_view(client):
    instance = test_helpers.create_lifts_app_status_request()
    url = reverse("lifts_app_status_request_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_status_request_update_view(client):
    instance = test_helpers.create_lifts_app_status_request()
    url = reverse("lifts_app_status_request_update", args=[instance.pk, ])
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_CustomUser_list_view(client):
    instance1 = test_helpers.create_lifts_app_CustomUser()
    instance2 = test_helpers.create_lifts_app_CustomUser()
    url = reverse("lifts_app_CustomUser_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_CustomUser_create_view(client):
    favorite_lifts = test_helpers.create_lifts_app_lift()
    url = reverse("lifts_app_CustomUser_create")
    data = {
        "phone_number": "text",
        "second_name": "text",
        "favorite_lifts": favorite_lifts.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_CustomUser_detail_view(client):
    instance = test_helpers.create_lifts_app_CustomUser()
    url = reverse("lifts_app_CustomUser_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_CustomUser_update_view(client):
    favorite_lifts = test_helpers.create_lifts_app_lift()
    instance = test_helpers.create_lifts_app_CustomUser()
    url = reverse("lifts_app_CustomUser_update", args=[instance.pk, ])
    data = {
        "phone_number": "text",
        "second_name": "text",
        "favorite_lifts": favorite_lifts.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
