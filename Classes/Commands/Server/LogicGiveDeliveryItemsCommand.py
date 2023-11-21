from Classes.Commands.LogicServerCommand import LogicServerCommand

delivery_ids = {
    "Coins": {
        "DeliveryID": 7
    },
    "TokenDoubler": {
        "DeliveryID": 2
    },
    "Credits": {
        "DeliveryID": 22
    },
    "ChromaCredits": {
        "DeliveryID": 23
    },
    "PowerPoints": {
        "DeliveryID": 24
    },
    "Blings": {
        "DeliveryID": 25
    },
    "Brawler": {
        "DeliveryID": 1
    },
    "Skin": {
        "DeliveryID": 9
    },
    "Pin": {
        "DeliveryID": 11
    },
    "ProfilePic": {
        "DeliveryID": 11
    },
    "Spray": {
        "DeliveryID": 11
    },
    "StarPower": {

        "DeliveryID": 4
    },
    "Gadget": {
        "DeliveryID": 4
    },
    "Overcharge": {
        "DeliveryID": 4
    },
}

class LogicGiveDeliveryItemsCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)
        self.delivery_ids = delivery_ids

    def encode(self, fields):
        reward = fields["reward"]
        self.writeVInt(1)
        self.writeVInt(1) # count rewards
        for x in range(1):

            self.writeVInt(100) # type
            self.writeVInt(1)
            for y in range(1):
                offer_type = reward[1]
                deliveryID = self.delivery_ids[f"{offer_type}"]["DeliveryID"]
                self.writeVInt(reward[2]) # amount
                if offer_type == "Brawler":
                    self.writeDataReference(16,reward[3])
                else:
                    self.writeDataReference(0, 0) # brawler id
                self.writeVInt(deliveryID)
                if offer_type == "Skin":
                    self.writeDataReference(29, reward[3])
                else:
                    self.writeDataReference(0,0) # skin id
                if offer_type == "Pin":
                    self.writeDataReference(52,reward[3]) # pin/thumbnail/spray
                elif offer_type == "ProfilePic":
                    self.writeDataReference(28,reward[3]) # pin/thumbnail/spray
                elif offer_type == "Spray":
                    self.writeDataReference(68,reward[3]) # pin/thumbnail/spray
                else:
                    self.writeDataReference(0, 0)
                if offer_type == "StarPower" or offer_type == "Gadget" or offer_type == "Overcharge":
                    self.writeDataReference(23,reward[3]) #star power/gadget
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
        self.writeVInt(10596)
        self.writeVInt(10596)
            
        LogicServerCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        return LogicServerCommand.decode(calling_instance, fields)

    def getCommandType(self):
        return 203