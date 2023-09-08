from Classes.Commands.LogicServerCommand import LogicServerCommand
from Classes.Logic.LogicStarrDropData import starrDropOpening


class LogicRefreshRandomRewardsCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        starrDropOpening.refreshData()

        self.writeVInt(1)
        self.writeVInt(-1)
        self.writeVInt(-1)
        self.writeVLong(0, 1)
        self.writeVInt(1)
        starrDropOpening.encode(self)

        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        return LogicServerCommand.decode(calling_instance, fields)

    def getCommandType(self):
        return 228