from rest_framework import serializers

from customer.models import Customer, Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'note', 'created_at']
        read_only_fields = ('id', 'created_at')





class CustomerSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')