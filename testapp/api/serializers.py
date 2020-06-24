




from rest_framework.serializers import ModelSerializer
from testapp.models import Tea
class TeaSerializer(ModelSerializer):
    class Meta:
        model=Tea
        fields='__all__'