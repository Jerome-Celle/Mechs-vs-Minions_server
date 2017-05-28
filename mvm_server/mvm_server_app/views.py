from mvm_server.mvm_server_app.models import Minion, CaseHuile
from mvm_server.mvm_server_app.serializers import MinionSerializer, CaseHuilenSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from mvm_server.mvm_server_app import services


class MinionList(generics.ListCreateAPIView):
    queryset = Minion.objects.all()
    serializer_class = MinionSerializer


class MinionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Minion.objects.all()
    serializer_class = MinionSerializer


class MinionMove(APIView):
    def get_object(self, pk):
        try:
            return Minion.objects.get(pk=pk)
        except Minion.DoesNotExist:
            raise Http404

    def get(self, request, pk, pMove, format=None):
        minion = self.get_object(pk)
        services.move(pmove=pMove, pSelectedMinion=minion)
        serializer = MinionSerializer(minion)
        return Response(serializer.data)


class CaseHuileList(generics.ListCreateAPIView):
    queryset = CaseHuile.objects.all()
    serializer_class = CaseHuilenSerializer


class CaseHuileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CaseHuile.objects.all()
    serializer_class = CaseHuilenSerializer