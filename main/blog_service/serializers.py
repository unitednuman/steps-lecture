from .models import Reporter, Article
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

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"