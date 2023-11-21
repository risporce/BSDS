from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Classes.Logic.LogicStarrDropData import starrDropOpening
from time import time

class LogicPurchaseOfferCommand(LogicCommand):
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
        fields["OfferIndex"] = calling_instance.readVInt()
        fields["Unk2"] = calling_instance.readDataReference()
        fields["Unk3"] = calling_instance.readDataReference()
        fields["Unk4"] = calling_instance.readVInt()
        
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields):
        if fields["OfferIndex"] == 0:
            starrDropOpening.create_starrDrop_opening(3)
        elif fields["OfferIndex"] == 1:
            starrDropOpening.create_starrDrop_opening(10)
        elif fields["OfferIndex"] == 2:
            starrDropOpening.create_starrDrop_opening(25)
        elif fields["OfferIndex"] == 3:
            starrDropOpening.create_starrDrop_opening(100)
        elif fields["OfferIndex"] == 4:
            starrDropOpening.create_starrDrop_opening(1100)
        elif fields["OfferIndex"] == 5:
            starrDropOpening.create_starrDrop_opening(10, "Rare", True)
        elif fields["OfferIndex"] == 6:
            starrDropOpening.create_starrDrop_opening(10, "Super_Rare", True)
        elif fields["OfferIndex"] == 7:
            starrDropOpening.create_starrDrop_opening(10, "Epic", True)
        elif fields["OfferIndex"] == 8:
            starrDropOpening.create_starrDrop_opening(10, "Mythic", True)
        elif fields["OfferIndex"] == 9:
            starrDropOpening.create_starrDrop_opening(10, "Legendary", True)

    def getCommandType(self):
        return 519