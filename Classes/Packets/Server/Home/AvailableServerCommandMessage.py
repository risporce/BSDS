from Classes.Logic.LogicCommandManager import LogicCommandManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class AvailableServerCommandMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(fields["ServerCommandID"])
        command = LogicCommandManager.createCommand(fields["ServerCommandID"], self.messagePayload)
        self.messagePayload = command.encode(fields)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24111

    def getMessageVersion(self):
        return self.messageVersion