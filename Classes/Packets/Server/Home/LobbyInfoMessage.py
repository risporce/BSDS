from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Logic.LogicStarrDropData import starrDropOpening


class LobbyInfoMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(ClientsManager.GetCount())
        self.writeString(f"""Project BSDS \n Version: {player.ClientVersion}
starrdrop rare count: {starrDropOpening.rare_count}
starrdrop super rare count: {starrDropOpening.super_rare_count}
starrdrop epic count: {starrDropOpening.epic_count}
starrdrop mythic count: {starrDropOpening.mythic_count}
starrdrop legendary count: {starrDropOpening.legendary_count}
""")
        self.writeVInt(0) # count event
        self.writeVInt(0) # new timer in v51

    def decode(self):
        fields = {}
        fields["PlayerCount"] = self.readVInt()
        fields["Text"] = self.readString()
        fields["Unk1"] = self.readVInt()
        super().decode(fields)
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 23457

    def getMessageVersion(self):
        return self.messageVersion