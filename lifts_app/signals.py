# code
from .models import *
 
def test_data(sender, **kwargs):
    lift1 = lift.objects.create(vendor_code="code1", is_booked=False, state="Normal", price=3400.0)
    lift2 = lift.objects.create(vendor_code="code2", is_booked=False, state="Normal", price=3800.0)
    lift3 = lift.objects.create(vendor_code="code3", is_booked=True, state="New", price=4000.0)

    admin = CustomUser.objects.create_user(username="admin", email='admin@admin.com', password="admin", is_superuser=True, is_staff=True, is_active=True)
    user = CustomUser.objects.create_user(username="user", email='user@user.com', password="user", is_active=True)
    user.favorite_lifts.set([lift1, lift3])
    user.save()
    manager = CustomUser.objects.create_user(username="manager", email="manager@manager.com", password="manager", is_active=True, is_staff=True)

    status_free = status_request.objects.create(name="Free")
    status_busy = status_request.objects.create(name="Busy")
    status_booked = status_request.objects.create(name="Booked")

    lift1_info = lift_info.objects.create(description="Information about 1 lift", lift=lift1)
    lift2_info = lift_info.objects.create(description="Information about 2 lift", lift=lift2)
    lift3_info = lift_info.objects.create(description="Information about 3 lift", lift=lift3)

    request1 = requests.objects.create(customer=user, manager=manager, status=status_free, lift=lift1)
    request2 = requests.objects.create(customer=user, manager=manager, status=status_busy, lift=lift2)
    request3 = requests.objects.create(customer=user, manager=manager, status=status_booked, lift=lift3)

    frequently_used_lifts1 = frequently_used_lifts.objects.create(lift=lift1, count=23)
    frequently_used_lifts2 = frequently_used_lifts.objects.create(lift=lift2, count=26)

    report1 = report.objects.create(manager=manager, frequently_used_lifts=frequently_used_lifts2)
    report1.requests.set([request1, request2, request3])
    report1.save()
