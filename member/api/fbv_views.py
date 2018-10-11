from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from member.models import Account
from member.serializers import AccountSerializer


class MyViewSet(ViewSet):

    # @require_http_methods(["GET", "POST"])
    def list(self, request):
        # I can assume now that only GET or POST requests make it this far
        # ...

        queryset = Account.objects.filter(is_superuser=True)
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)
