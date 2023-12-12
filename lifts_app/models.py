from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class frequently_used_lifts(models.Model):

    # Relationships
    lift = models.ForeignKey("lifts_app.lift", on_delete=models.CASCADE, verbose_name="Подъемник")
    count = models.BigIntegerField(verbose_name="Количество заказов")

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Дата создания")
    last_updated = models.DateTimeField(auto_now=True, editable=False, verbose_name="Последнее обновление")

    class Meta:
        verbose_name= "Часто используемый подъемник"
        verbose_name_plural = "Часто используемые подъемники"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("lifts_app_frequently_used_lifts_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lifts_app_frequently_used_lifts_update", args=(self.pk,))



class lift(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False, verbose_name="Последнее обновление")
    vendor_code = models.CharField(max_length=150, verbose_name="Артикул")
    is_booked = models.BooleanField(verbose_name="Забронирован")
    state = models.CharField(max_length=30, verbose_name="Состояние")
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Дата создания")
    price = models.FloatField(verbose_name="Цена")

    class Meta:
        verbose_name= "Подъемник"
        verbose_name_plural = "Подъемники"

    def __str__(self):
        return str(self.vendor_code)

    # def get_absolute_url(self):
    #     return reverse("lifts_app_lift_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lifts_app_lift_update", args=(self.pk,))



class lift_images(models.Model):

    # Relationships
    lift = models.ForeignKey("lifts_app.lift", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False, verbose_name="Последнее обновление")
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Дата создания")
    image = models.ImageField(upload_to="upload/images/")

    class Meta:
        verbose_name= "Изображение подъемника"
        verbose_name_plural = "Изображения подъемников"

    def __str__(self):
        return str(self.pk)

    # def get_absolute_url(self):
    #     return reverse("lifts_app_lift_images_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lifts_app_lift_images_update", args=(self.pk,))



class lift_info(models.Model):

    # Relationships
    lift = models.OneToOneField("lifts_app.lift", on_delete=models.CASCADE, verbose_name="Подъемник")

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Дата создания")
    description = models.TextField(max_length=1500, verbose_name="Описание подъемника")
    last_updated = models.DateTimeField(auto_now=True, editable=False, verbose_name="Последнее обновление")

    class Meta:
        verbose_name= "Информация о подъемнике"
        verbose_name_plural = "Информация о подъемниках"

    def __str__(self):
        return str(self.pk)

    # def get_absolute_url(self):
    #     return reverse("lifts_app_lift_info_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lifts_app_lift_info_update", args=(self.pk,))



class report(models.Model):

    # Relationships
    manager = models.ForeignKey("lifts_app.CustomUser", related_name="fk_report_manager", on_delete=models.CASCADE, verbose_name="Менеджер")
    requests = models.ManyToManyField("lifts_app.requests", related_name="mtm_requests_for_report", verbose_name="Заявки")
    frequently_used_lifts = models.ForeignKey("lifts_app.frequently_used_lifts", on_delete=models.CASCADE, verbose_name="Часто используемые подъемники")

    # Fields
    date = models.DateTimeField(null=True, verbose_name="Дата отчета")
    last_updated = models.DateTimeField(auto_now=True, editable=False, verbose_name="Последнее обновление")
    sales_amount = models.FloatField(default=1000.0, verbose_name="Объем продаж")
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Дата создания")
    expenses = models.FloatField(default=500.0, verbose_name="Затраты")

    class Meta:
        verbose_name= "Отчет"
        verbose_name_plural = "Отчеты"

    def __str__(self):
        return str(self.pk)

    # def get_absolute_url(self):
    #     return reverse("lifts_app_report_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lifts_app_report_update", args=(self.pk,))



class requests(models.Model):

    # Relationships
    customer = models.ForeignKey("lifts_app.CustomUser", related_name="fk_requests_customer", on_delete=models.CASCADE, verbose_name="Заказчик")
    manager = models.ForeignKey("lifts_app.CustomUser", related_name="fk_requests_manager", on_delete=models.CASCADE, verbose_name="Менеджер")
    status = models.ForeignKey("lifts_app.status_request", on_delete=models.CASCADE, verbose_name="Статус")
    reports = models.ManyToManyField("lifts_app.report", related_name="mtm_reports_for_request", verbose_name="Отечеты")
    lift = models.ForeignKey("lifts_app.lift", related_name="fk_request_lift", on_delete=models.CASCADE, verbose_name="Подъемник")
    # Fields
    date_closed = models.DateTimeField(null=True, verbose_name="Дата завершения")
    price = models.FloatField(default=4000.0, verbose_name="Цена")
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Дата создания")
    date_booking = models.DateTimeField(default=timezone.now, verbose_name="Дата бронирования")
    last_updated = models.DateTimeField(auto_now=True, editable=False, verbose_name="Последнее обновление")

    class Meta:
        verbose_name= "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return str(self.pk)

    # def get_absolute_url(self):
    #     return reverse("lifts_app_requests_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lifts_app_requests_update", args=(self.pk,))



class status_request(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False, verbose_name="Последнее обновление")
    name = models.CharField(max_length=50, verbose_name="Назавние состояния")
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Дата создания")

    class Meta:
        verbose_name= "Статус заявки"
        verbose_name_plural = "Статусы заявок"

    def __str__(self):
        return str(self.name)

    # def get_absolute_url(self):
    #     return reverse("lifts_app_status_request_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lifts_app_status_request_update", args=(self.pk,))



class CustomUser(AbstractUser):

    # Relationships
    favorite_lifts = models.ManyToManyField("lifts_app.lift", verbose_name="Любимые подъемники")

    # Fields
    phone_number = models.CharField(max_length=30, verbose_name="Номер телефона")
    second_name = models.CharField(max_length=30, verbose_name="Отчество")

    class Meta:
        verbose_name= "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return str(self.username)

    # def get_absolute_url(self):
    #     return reverse("lifts_app_CustomUser_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lifts_app_CustomUser_update", args=(self.pk,))

