from rest_framework import serializers

from mvm_server.mvm_server_app.models import Minion, CaseHuile


class MinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minion
        fields = ('id', 'posX', 'posY')


class CaseHuilenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseHuile
        fields = ('id', 'posX', 'posY')