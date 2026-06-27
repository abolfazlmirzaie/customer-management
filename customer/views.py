from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from customer.models import Customer, Note
from customer.serializers import CustomerSerializer, NoteSerializer


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



class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer


    def get_queryset(self):
        return Note.objects.filter(customer_id=self.kwargs['customer_pk'])


    def perform_create(self, serializer):
        customer = Customer.objects.get(pk=self.kwargs['customer_pk'])
        serializer.save(customer=customer)