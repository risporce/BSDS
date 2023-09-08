from Classes.Packets.PiranhaMessage import PiranhaMessage


class PlayerProfileMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVLong(fields["PlayerHighID"], fields["PlayerLowID"])
        self.writeDataReference(0)
        self.writeVInt(63)
        for i in range(63):
            self.writeDataReference(16, i)
            self.writeDataReference(0)
            self.writeVInt(500) # trophies
            self.writeVInt(1250) # highestTrophies
            self.writeVInt(11) #power level
        
        self.writeVInt(17)

        self.writeVInt(1) 
        self.writeVInt(1) # 3v3 victories

        self.writeVInt(2)
        self.writeVInt(2) # total exp

        self.writeVInt(3)
        self.writeVInt(3) # current trophies

        self.writeVInt(4)
        self.writeVInt(4) # highest trophies

        self.writeVInt(5) 
        self.writeVInt(5) # unlocked brawler?

        self.writeVInt(8)
        self.writeVInt(6) # solo victories

        self.writeVInt(11) 
        self.writeVInt(7) # duo victories

        self.writeVInt(9) 
        self.writeVInt(8) # highest level robo rumble

        self.writeVInt(12) 
        self.writeVInt(9) # highest level boss fight

        self.writeVInt(13)
        self.writeVInt(10) # highest power league points

        self.writeVInt(14)
        self.writeVInt(11) # some power league stuff

        self.writeVInt(15)
        self.writeVInt(12) # most challenge win

        self.writeVInt(16) #highest level city rampage
        self.writeVInt(13)

        self.writeVInt(18) #highest solo power league rank
        self.writeVInt(14)

        self.writeVInt(17) #highest team power league rank
        self.writeVInt(15)

        self.writeVInt(19) # highest Club league rank
        self.writeVInt(16)

        self.writeVInt(20) # number fame
        self.writeVInt(69)

        self.writeString("risporce")  #PlayerInfo
        self.writeVInt(100)
        self.writeVInt(28000001)
        self.writeVInt(43000001)
        self.writeVInt(14)

        self.writeBoolean(True)
        self.writeVInt(0)

        self.writeString("hello world")
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeBoolean(True) #alliance
        self.writeLong(0,1) #alliance ID
        self.writeString("haccers") #alliance name
        self.writeDataReference(8,1) # alliance icon
        self.writeVInt(1) # type
        self.writeVInt(1) # member count
        self.writeVInt(10000) # total trophies
        self.writeVInt(1) # minimum trophies to enter
        self.writeDataReference(0)
        self.writeString("CA") #location
        self.writeVInt(4) # unknown
        self.writeBoolean(True) #is Family friendly
        self.writeVInt(0)
        

        self.writeDataReference(25, 1) #alliance role

    def decode(self):
        pass
        # fields = {}
        # fields["PlayerCount"] = self.readVInt()
        # fields["Text"] = self.readString()
        # fields["Unk1"] = self.readVInt()
        # super().decode(fields)
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24113

    def getMessageVersion(self):
        return self.messageVersion