from .models import Reporter
from rest_framework import serializers
# from .models import Reporter


# class ReporterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reporter
#         fields = "__all__"

class ReporterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = "__all__"

        # fields = ("first_name", "last_name")
        # read_only_fields
        #write_only_fields