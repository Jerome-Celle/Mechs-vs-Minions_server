"""from mvm_server.mvm_server_app.models import Minion
from mvm_server.mvm_server_app.serializers import MinionSerializer
from mvm_server.mvm_server_app import services

class MinionResourceBinding(ResourceBinding):
    model = Minion
    stream = 'minions'
    serializer_class = MinionSerializer
    queryset = Minion.objects.all()

    @detail_action()
    def move(self, pk, data=None, **kwargs):
        minion = self.get_object(pk)
        services.move(pmove=100, pSelectedMinion=minion)
        result = minion.publish()
        return result, 200

    @detail_action()
    def publish(self, pk, data=None, **kwargs):
        instance = self.get_object(pk)
        result = instance.publish()
        return result, 200



http://codeselfstudy.com/wiki/Django_Channels
https://github.com/linuxlewis/channels-api
https://www.youtube.com/watch?v=HzC_pUhoW0I
"""