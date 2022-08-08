from django.contrib import admin
from django.urls import path

from .views import TicketViewList, TicketCreateView,TicketCloseView, TicketDeleteView,UserRegistrationView

urlpatterns = [
    path("tickets/all", TicketViewList.as_view(), name="tickets"),
    path("tickets/new", TicketCreateView.as_view(), name="tickets_new"),
    path("tickets/markAsClosed", TicketCloseView.as_view(), name="tickets_close"),
    path("tickets/delete", TicketDeleteView.as_view(), name="tickets_delete"),
    path("users/new", UserRegistrationView.as_view(), name="tickets_delete"),

]
