from Classes.Commands.LogicServerCommand import LogicServerCommand
from Classes.Logic.LogicStarrDropData import starrDropOpening
import random


class LogicGiveDeliveryItemsCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        starrDrop = starrDropOpening.getStarrDropEncoding()
        print(starrDrop)
        self.writeVInt(30)
        self.writeVInt(1) # count rewards
        for x in range(1):
            item_name = starrDrop[0][1]
            deliveryID = starrDropOpening.getDeliveryIdFromOfferType(item_name)
            self.writeVInt(100) # type
            self.writeVInt(1)
            for y in range(1):
                self.writeVInt(starrDrop[0][2]) # amount
                if item_name == "Brawler":
                    self.writeDataReference(16,starrDrop[0][3])
                else:
                    self.writeDataReference(0, 0) # brawler id
                self.writeVInt(deliveryID)
                if item_name == "Skin":
                    self.writeDataReference(29, starrDrop[0][3])
                else:
                    self.writeDataReference(0,0) # skin id
                if item_name == "Pin":
                    self.writeDataReference(52,starrDrop[0][3]) # pin/thumbnail/spray
                elif item_name == "ProfilePic":
                    self.writeDataReference(28,starrDrop[0][3]) # pin/thumbnail/spray
                elif item_name == "Spray":
                    self.writeDataReference(68,starrDrop[0][3]) # pin/thumbnail/spray
                else:
                    self.writeDataReference(0, 0)
                if item_name == "StarPower" or item_name == "Gadget":
                    self.writeDataReference(23,starrDrop[0][3]) #star power/gadget
                else:
                    self.writeDataReference(0, 0)
                self.writeVInt(x)
                self.writeVInt(x)
                self.writeVInt(1)

        self.writeByte(1) # forced drop
        if True:
            self.writeVInt(200)
            self.writeVInt(200)
            self.writeVInt(5)
            for x in range(1):
                self.writeVInt(93)
                self.writeVInt(206)
                self.writeVInt(456)
                self.writeVInt(1001)
                self.writeVInt(2264)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(5)
        self.writeByte(2)
        self.writeDataReference(0, 0)
        self.writeVInt(-1)
        self.writeVInt(-1)
            
        LogicServerCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        return LogicServerCommand.decode(calling_instance, fields)

    def getCommandType(self):
        return 203