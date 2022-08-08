from django.db import models

ACCOUNT_CHOICES = (("employee", "employee"), ("admin", "admin"))


class UserRegistration(models.Model):
    class Meta:
        db_table = "user_registration"

    username = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=255, choices=ACCOUNT_CHOICES)


STATUS_CHOICE = (("open", "open"), ("close", "close"))
PRIORITY = (("low", "low"), ("medium", "medium"), ("high", "high"))


class TicketRaise(models.Model):
    class Meta:
        db_table = "ticket_raise"

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICE, default="open")
    priority = models.CharField(choices=PRIORITY, max_length=255, default="low")
    assigned_to = models.ForeignKey("UserRegistration", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
