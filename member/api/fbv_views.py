from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from member.models import Account
from member.serializers import AccountSerializer


class MyViewSet(ViewSet):

    # @require_http_methods(["GET", "POST"])
    @method_decorator(name='list', decorator=swagger_auto_schema(
        operation_summary='이건 서머리 ',
    ))
    def list(self, request):
        # I can assume now that only GET or POST requests make it this far
        # ...
        print(request.version)

        queryset = Account.objects.filter(is_superuser=True)
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)
