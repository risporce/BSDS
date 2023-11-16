from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging

class LogicOpenRandomCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeVInt(0)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["Unk1"] = calling_instance.readVInt()
        # fields["RewardType"] = calling_instance.readVInt()
        # fields["RewardAmount"] = calling_instance.readVInt()
        # fields["Unk2"] = calling_instance.readVInt()
        #fields["Unk3"] = calling_instance.readVInt()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields):
        pass

    def getCommandType(self):
        return 571