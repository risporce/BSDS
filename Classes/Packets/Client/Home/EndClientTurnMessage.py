from Classes.Logic.LogicCommandManager import LogicCommandManager
from Classes.Logic.LogicStarrDropData import starrDropOpening

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Messaging import Messaging


class EndClientTurnMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        self.readBoolean()
        fields["Tick"] = self.readVInt()
        fields["Checksum"] = self.readVInt()
        fields["CommandsCount"] = self.readVInt()
        super().decode(fields)
        fields["Commands"] = []
        for i in range(fields["CommandsCount"]):
            fields["Commands"].append({"ID": self.readVInt()})
            if LogicCommandManager.commandExist(fields["Commands"][i]["ID"]):
                command = LogicCommandManager.createCommand(fields["Commands"][i]["ID"])
                print(fields["Commands"][i]["ID"])
                print("Command", LogicCommandManager.getCommandsName(fields["Commands"][i]["ID"]))
                if command is not None:
                    fields["Commands"][i]["Fields"] = command.decode(self)
                    fields["Commands"][i]["Instance"] = command
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        for command in fields["Commands"]:
            if "Instance" not in command.keys():
                return

            if hasattr(command["Instance"], 'execute'):
                command["Instance"].execute(calling_instance, command["Fields"])
            if command["ID"] == 571:
                pass
                fields["ServerCommandID"] = 203
                Messaging.sendMessage(24111, fields, cryptoInit, calling_instance.player)
                fields["ServerCommandID"] = 228
                Messaging.sendMessage(24111, fields, cryptoInit, calling_instance.player)
            elif command["ID"] == 519:
            #     fields["ServerCommandID"] = 203
            #     Messaging.sendMessage(24111, fields, cryptoInit, calling_instance.player)
            # elif command["ID"] == 203:
            #     fields["ServerCommandID"] = 228
            #     Messaging.sendMessage(24111, fields, cryptoInit, calling_instance.player)
                Messaging.sendMessage(24104, {"Socket": calling_instance.client, "ServerChecksum": 0, "ClientChecksum": 0, "Tick": 0}, cryptoInit)

    def getMessageType(self):
        return 14102

    def getMessageVersion(self):
        return self.messageVersion