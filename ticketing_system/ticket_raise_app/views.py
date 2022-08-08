from rest_framework import status, views
from rest_framework.response import Response
from django.db.models import Q
from .models import TicketRaise, UserRegistration
from ticket_raise_app.serializers import TickerCreateSerializer, TickerListSerializer, UserCreateSerializer


class UserRegistrationView(views.APIView):
    @staticmethod
    def post(request):
        try:
            serial_data = UserCreateSerializer(data=request.data)
            if serial_data.is_valid(raise_exception=False):
                user_detail = UserRegistration.objects.create(username=serial_data.data["username"],
                                                                 role=serial_data.data["role"])
                return Response({"token Id": "xdakdakdakdakdadka"}, status.HTTP_201_CREATED)
            return Response(serial_data.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class TicketViewList(views.APIView):
    @staticmethod
    def get(request):
        try:
            title, status_data, priority = (
                request.GET.get("title"),
                request.GET.get("status"),
                request.GET.get("priority"),
            )
            query = Q()
            if title:
                query.add(Q(title__icontains=title), Q.AND)
            if status_data:
                query.add(Q(status=status_data), Q.AND)
            if priority:
                query.add(Q(priority=priority), Q.AND)
            return Response(
                TickerListSerializer(TicketRaise.objects.filter(query), many=True).data,
                status.HTTP_200_OK
            )
        except Exception as e:
            return Response(e, status.HTTP_400_BAD_REQUEST)


class TicketCreateView(views.APIView):
    @staticmethod
    def post(request):
        try:
            serial_data = TickerCreateSerializer(data=request.data)
            if serial_data.is_valid(raise_exception=False):
                ticket_details = TicketRaise.objects.create(title=serial_data.data["title"],
                                                            description=serial_data.data["description"])
                return Response({"ticket Id": ticket_details.id}, status.HTTP_201_CREATED)
            return Response(serial_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class TicketCloseView(views.APIView):
    @staticmethod
    def post(request):
        try:
            ticket_id = request.data.get("ticketID")
            ticket_details = TicketRaise.objects.get(id=ticket_id)
            if ticket_details.priority == "high":
                return Response("A higher priority task remains to be closed")
            ticket_details.status = "close"
            ticket_details.save()
            return Response({"message": "Ticket close successfully"}, status.HTTP_200_OK)
        except TicketRaise.DoesNotExist:
            return Response({"Message": "This id does not exit"}, status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class TicketDeleteView(views.APIView):
    @staticmethod
    def post(request):
        try:
            ticket_id = request.data.get("ticketID")
            ticket_details = TicketRaise.objects.get(id=ticket_id)
            ticket_details.delete()
            return Response({"message": "Ticket delete successfully"}, status.HTTP_200_OK)
        except TicketRaise.DoesNotExist:
            return Response({"Message": "This id does not exit"}, status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)
