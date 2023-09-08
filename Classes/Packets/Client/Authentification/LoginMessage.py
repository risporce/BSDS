from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage


class LoginMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["AccountID"] = self.readLong()
        fields["PassToken"] = self.readString()
        fields["ClientMajor"] = self.readInt()
        fields["ClientMinor"] = self.readInt()
        fields["ClientBuild"] = self.readInt()
        fields["ResourceSha"] = self.readString()
        fields["Device"] = self.readString()
        fields["PreferredLanguage"] = self.readDataReference()
        fields["PreferredDeviceLanguage"] = self.readString()
        fields["OSVersion"] = self.readString()
        fields["isAndroid"] = self.readBoolean()
        fields["IMEI"] = self.readString()
        fields["AndroidID"] = self.readString()
        fields["isAdvertisingEnabled"] = self.readBoolean()
        fields["AppleIFV"] = self.readString()
        fields["RndKey"] = self.readInt()
        fields["AppStore"] = self.readVInt()
        fields["ClientVersion"] = self.readString()
        fields["TencentOpenId"] = self.readString()
        fields["TencentToken"] = self.readString()
        fields["TencentPlatform"] = self.readVInt()
        fields["DeviceVerifierResponse"] = self.readString()
        fields["AppLicensingSignature"] = self.readString()
        fields["DeviceVerifierResponse"] = self.readString()
        fields["SupercellIdToken"] = self.readCompressedString()
        fields["UpdateMaintenanceMode"] = self.readBoolean()
        fields["YoozooOsdkTicket"] = self.readString()
        fields["YoozooDeviceId"] = self.readString()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        pass
        calling_instance.player.ClientVersion = f'{str(fields["ClientMajor"])}.{str(fields["ClientBuild"])}.{str(fields["ClientMinor"])}'
        fields["Socket"] = calling_instance.client
        # ClientsManager.AddPlayer(calling_instance.player.ID, calling_instance.client)
        Messaging.sendMessage(20104, fields, cryptoInit, calling_instance.player)
        Messaging.sendMessage(24101, fields, cryptoInit, calling_instance.player)
        Messaging.sendMessage(24399, fields, cryptoInit, calling_instance.player)

    def getMessageType(self):
        return 10101

    def getMessageVersion(self):
        return self.messageVersion