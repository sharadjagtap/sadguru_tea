


from rest_framework.viewsets import ModelViewSet
from testapp.models import Tea
from testapp.api.serializers import TeaSerializer
class TeaCRUD(ModelViewSet):
    queryset = Tea.objects.all()
    serializer_class = TeaSerializer

