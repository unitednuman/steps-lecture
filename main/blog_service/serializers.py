from .models import Reporter, Article , Publisher
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

    def get_detailed_data(self, instance):
        return {
            "reporter": ReporterSerializers(instance.reporter).data,
        }
    def to_representation(self, instance):
        data = super(ArticleSerializers, self).to_representation(instance)
        data.update(self.get_detailed_data(instance))

        return data

class PublisherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"