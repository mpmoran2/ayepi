from django.db.models import fields
from myapp.models import Googs
from rest_framework import serializers

class SheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Googs
        fields = ('Ethnicity', 'Location', 'From')
