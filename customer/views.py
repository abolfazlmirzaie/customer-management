from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


from customer.models import Customer, Note
from customer.serializers import CustomerSerializer, NoteSerializer, TelegramCustomerSerializer


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    @action(detail=True, methods=['post'])
    def change_status(self, request, *args, **kwargs):
        customer = self.get_object()

        serializer = self.get_serializer(
            customer,
            data={'status': request.data.get('status')},
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'updated'})

        return Response(serializer.errors, status=400)


    @action(detail=False, methods=['post'])
    def telegram(self, request, *args, **kwargs):
        serializer = TelegramCustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        customer, created = Customer.objects.update_or_create(
            telegram_id=serializer.validated_data["telegram_id"],
            defaults={
                "name": serializer.validated_data["name"],
                "phone": serializer.validated_data["phone"],
                "address": serializer.validated_data["address"],
            },
        )

        Note.objects.create(
            customer=customer,
            note=serializer.validated_data["message"],
        )

        return Response(
            {"success": True},
            status=status.HTTP_201_CREATED,
        )



class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer


    def get_queryset(self):
        return Note.objects.filter(customer_id=self.kwargs['customer_pk'])


    def perform_create(self, serializer):
        customer = Customer.objects.get(pk=self.kwargs['customer_pk'])
        serializer.save(customer=customer)

