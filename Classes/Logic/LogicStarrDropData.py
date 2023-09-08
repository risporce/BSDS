from Classes.Files.Classes.Cards import Cards
from Classes.Files.Classes.Pins import Emotes
from Classes.Files.Classes.PlayerThumbnails import PlayerThumbnails
from Classes.Files.Classes.Skins import Skins
from Classes.Files.Classes.Sprays import Sprays
from Classes.Files.Classes.Characters import Characters

import random

items_ids = {
    "Coins": {
        "OfferID": 1,
        "DeliveryID": 7
    },
    "TokenDoubler": {
        "OfferID": 9,
        "DeliveryID": 2
    },
    "Credits": {
        "OfferID": 38,
        "DeliveryID": 22
    },
    "ChromaCredits": {
        "OfferID": 39,
        "DeliveryID": 23
    },
    "PowerPoints": {
        "OfferID": 41,
        "DeliveryID": 24
    },
    "Bling": {
        "OfferID": 45,
        "DeliveryID": 25
    },
    "Brawler": {
        "OfferID": 3,
        "DeliveryID": 1
    },
    "Skin": {
        "OfferID": 4,
        "DeliveryID": 9
    },
    "Pin": {
        "OfferID": 19,
        "DeliveryID": 11
    },
    "ProfilePic": {
        "OfferID": 25,
        "DeliveryID": 11
    },
    "Spray": {
        "OfferID": 35,
        "DeliveryID": 11
    },
    "StarPower": {
        "OfferID": 5,
        "DeliveryID": 4
    },
    "Gadget": {
        "OfferID": 5,
        "DeliveryID": 4
    },
}

starrDrop_data = {
    "Rare": {
        "Rarity_ID": 0,
        "DropChance": 50,
        "TotalTickets": 215,
        "Possibilities": {
            "Coins_s": {
                "Type": "Coins",
                "Tickets": 75,
                "Min": 50,
                "Max": 70,
                "Fallback": []
            },
            "PowerPoints_s": {
                "Type": "PowerPoints",
                "Tickets": 85,
                "Min": 20,
                "Max": 30,
                "Fallback": []
            },
            "Credits_s": {
                "Type": "Credits",
                "Tickets": 5,
                "Min": 20,
                "Max": 28,
                "Fallback": []
            },
            "Blings_s": {
                "Type": "Bling",
                "Tickets": 5,
                "Min": 20,
                "Max": 28,
                "Fallback": []
            },
            "TokenDoubler_s": {
                "Type": "TokenDoubler",
                "Tickets": 45,
                "Min": 100,
                "Max": 150,
                "Fallback": ["Credits", 100]
            }
        }
    },
    "Super_Rare": {
        "Rarity_ID": 1,
        "DropChance": 28,
        "TotalTickets": 151,
        "Possibilities": {
            "Coins_m": {
                "Type": "Coins",
                "Tickets": 45,
                "Min": 100,
                "Max": 140,
                "Fallback": []
            },
            "PowerPoints_m": {
                "Type": "PowerPoints",
                "Tickets": 60,
                "Min": 50,
                "Max": 70,
                "Fallback": []
            },
            "Credits_m": {
                "Type": "Credits",
                "Tickets": 4,
                "Min": 50,
                "Max": 60,
                "Fallback": []
            },
            "Blings_m": {
                "Type": "Bling",
                "Tickets": 5,
                "Min": 50,
                "Max": 60,
                "Fallback": []
            },
            "TokenDoubler_m": {
                "Type": "TokenDoubler",
                "Tickets": 37,
                "Min": 500,
                "Max": 575,
                "Fallback": ["Credits", 100]
            }
        }
    },
    "Epic": {
        "Rarity_ID": 2,
        "DropChance": 15,
        "TotalTickets": 227,
        "Possibilities": {
            "Coins_l": {
                "Type": "Coins",
                "Tickets": 90,
                "Min": 200,
                "Max": 240,
                "Fallback": []
            },
            "PowerPoints_l": {
                "Type": "PowerPoints",
                "Tickets": 60,
                "Min": 100,
                "Max": 130,
                "Fallback": []
            },
            "Brawler_Rare": {
                "Type": "Brawler",
                "Rarity": "rare",
                "Tickets": 7,
                "Fallback": ["Credits", 100]
            },
            "Brawler_SuperRare": {
                "Type": "Brawler",
                "Rarity": "super_rare",
                "Tickets": 3,
                "Fallback": ["Credits", 250]
            },
            "Pin_1-9Gems": {
                "Type": "Pin",
                "Tickets": 10,
                "MinPrice": 1,
                "MaxPrice": 9,
                "Fallback": ["Credits", 100]
            },
            "Spray_1-19Gems": {
                "Type": "Spray",
                "Tickets": 5,
                "MinPrice": 1,
                "MaxPrice": 19,
                "Fallback": ["Credits", 100]
            },
            "ProfilePic": {
                "Type": "ProfilePic",
                "Tickets": 7,
                "Fallback": ["Credits", 200]
            },
            "TokenDoubler_l": {
                "Type": "TokenDoubler",
                "Tickets": 45,
                "Min": 1000,
                "Max": 1200,
                "Fallback": ["Credits", 100]
            }
        }
    },
    "Mythic": {
        "Rarity_ID": 3,
        "DropChance": 5,
        "TotalTickets": 135,
        "Possibilities": {
            "Coins_xl": {
                "Type": "Coins",
                "Tickets": 25,
                "Min": 500,
                "Max": 540,
                "Fallback": []
            },
            "PowerPoints_xl": {
                "Type": "PowerPoints",
                "Tickets": 35,
                "Min": 240,
                "Max": 280,
                "Fallback": []
            },
            "Brawler_Epic": {
                "Type": "Brawler",
                "Rarity": "epic",
                "Tickets": 7,
                "Fallback": ["Credits", 500]
            },
            "Brawler_Mythic": {
                "Type": "Brawler",
                "Rarity": "mega_epic",
                "Tickets": 2,
                "Fallback": ["Credits", 1000]
            },
            "Skin_1-29Gems": {
                "Type": "Skin",
                "Tickets": 10,
                "MinPrice": 1,
                "MaxPrice": 29,
                "Fallback": ["Credits", 200]
            },
            "Skin_30-79Gems": {
                "Type": "Skin",
                "Tickets": 2,
                "MinPrice": 30,
                "MaxPrice": 79,
                "Fallback": ["Credits", 250]
            },
            "Pin_1-9Gems": {
                "Type": "Pin",
                "Tickets": 25,
                "MinPrice": 1,
                "MaxPrice": 9,
                "Fallback": ["Credits", 100]
            },
            "Pin_10-29Gems": {
                "Type": "Pin",
                "Tickets": 10,
                "MinPrice": 10,
                "MaxPrice": 29,
                "Fallback": ["Credits", 150]
            },
            "Spray_1-19Gems": {
                "Type": "Spray",
                "Tickets": 5,
                "MinPrice": 1,
                "MaxPrice": 19,
                "Fallback": ["Credits", 100]
            },
            "ProfilePic": {
                "Type": "ProfilePic",
                "Tickets": 14,
                "Fallback": ["Credits", 200]
            }
        }

    },
    "Legendary": {
        "Rarity_ID": 4,
        "DropChance": 2,
        "TotalTickets": 116,
        "Possibilities": {
            "Gadget": {
                "Type": "Gadget",
                "Tickets": 35,
                "Fallback": ["Coins", 1000]
            },
            "StarPower": {
                "Type": "StarPower",
                "Tickets": 30,
                "Fallback": ["Coins", 1000]
            },
            "Brawler_Epic": {
                "Type": "Brawler",
                "Rarity": "epic",
                "Tickets": 9,
                "Fallback": ["Credits", 500]
            },
            "Brawler_Mythic": {
                "Type": "Brawler",
                "Rarity": "mega_epic",
                "Tickets": 3,
                "Fallback": ["Credits", 1000]
            },
            "Brawler_Legendary": {
                "Type": "Brawler",
                "Rarity": "legendary",
                "Tickets": 2,
                "Fallback": ["Credits", 2000]
            },
            "Skin_1-29Gems": {
                "Type": "Skin",
                "Tickets": 10,
                "MinPrice": 1,
                "MaxPrice": 29,
                "Fallback": ["Credits", 200]
            },
            "Skin_30-79Gems": {
                "Type": "Skin",
                "Tickets": 6,
                "MinPrice": 30,
                "MaxPrice": 79,
                "Fallback": ["Credits", 250]
            },
            "Skin_80-149Gems": {
                "Type": "Skin",
                "Tickets": 4,
                "MinPrice": 80,
                "MaxPrice": 149,
                "Fallback": ["Credits", 300]
            },
            "Pin_30-39Gems": {
                "Type": "Pin",
                "Tickets": 12,
                "MinPrice": 30,
                "MaxPrice": 999,
                "Fallback": ["Credits", 200]
            },
            "Spray_20-29Gems": {
                "Type": "Spray",
                "Tickets": 5,
                "MinPrice": 20,
                "MaxPrice": 999,
                "Fallback": ["Credits", 150]
            }
        }

    },
}
class LogicStarrDropData():
    def __init__(self):
        self.starrDrop_data = starrDrop_data
        self.items_ids = items_ids
        self.starr_drop_encoding_data = []
        self.range_price_items = ["Skin", "Pin", "Spray"]
        self.skin = Skins()
        self.pin = Emotes()
        self.spray = Sprays()
        self.brawler = Characters()
        self.card = Cards()
        self.profile_pic = PlayerThumbnails()
        self.rare_count = 0
        self.super_rare_count = 0
        self.epic_count = 0
        self.mythic_count = 0
        self.legendary_count = 0

    def choose_random_starrDrop(self):
        random_number = random.randint(1, 100)
        cumulative = 0
        chosen_drop = None

        for box_type in self.starrDrop_data.items():
            cumulative += self.starrDrop_data[f"{box_type[0]}"]["DropChance"]
            if random_number <= cumulative:
                chosen_drop = box_type
                break
        return chosen_drop[0]
    
    def choose_random_reward(self, chosen_drop):
        random_number = random.randint(1, self.starrDrop_data[f"{chosen_drop}"]["TotalTickets"])
        cumulative = 0
        chosen_reward = None
        for item, data in self.starrDrop_data[f"{chosen_drop}"]["Possibilities"].items():
            cumulative += data["Tickets"]
            if random_number <= cumulative:
                chosen_reward = item
                break
        return chosen_reward

    def create_starrDrop_opening(self, drop_count, starrDrop_rarity = None, rarity_set = None):
        for i in range(drop_count):
            starrDrop = []
            if rarity_set is None:
                starrDrop_rarity = self.choose_random_starrDrop()
                starrDrop_reward = self.choose_random_reward(starrDrop_rarity)
            else:
                starrDrop_reward = self.choose_random_reward(starrDrop_rarity)
            try:
                starrDrop_reward_amount = random.randint(self.starrDrop_data[f"{starrDrop_rarity}"]["Possibilities"][f"{starrDrop_reward}"]["Min"],self.starrDrop_data[f"{starrDrop_rarity}"]["Possibilities"][f"{starrDrop_reward}"]["Max"])
            except KeyError:
                starrDrop_reward_amount = 1
            starrDrop_type = self.starrDrop_data[f"{starrDrop_rarity}"]["Possibilities"][f"{starrDrop_reward}"]["Type"]
            self.updateCount(self.starrDrop_data[f"{starrDrop_rarity}"]["Rarity_ID"])
            starrDrop.append(self.starrDrop_data[f"{starrDrop_rarity}"]["Rarity_ID"])
            starrDrop.append(starrDrop_type)
            starrDrop.append(starrDrop_reward_amount)
            if starrDrop_type in self.range_price_items:
                starrDrop.append(self.getRewarditemID(starrDrop_type, min=self.starrDrop_data[f"{starrDrop_rarity}"]["Possibilities"][f"{starrDrop_reward}"]["MinPrice"], max=self.starrDrop_data[f"{starrDrop_rarity}"]["Possibilities"][f"{starrDrop_reward}"]["MaxPrice"]))
            elif starrDrop_type == "Brawler":
                starrDrop.append(self.getRewarditemID(starrDrop_type, additional=self.starrDrop_data[f"{starrDrop_rarity}"]["Possibilities"][f"{starrDrop_reward}"]["Rarity"]))
            elif starrDrop_type == "StarPower":
                starrDrop.append(self.getRewarditemID(starrDrop_type, additional=4))
            elif starrDrop_type == "Gadget":
                starrDrop.append(self.getRewarditemID(starrDrop_type, additional=5))
            elif starrDrop_type == "ProfilePic":
                starrDrop.append(self.getRewarditemID(starrDrop_type))

            self.starr_drop_encoding_data.append(starrDrop)
        self.setStarrDropEncodingData(self.starr_drop_encoding_data)

    def getDeliveryIdFromOfferType(self, offer_type):
        return self.items_ids[f"{offer_type}"]["DeliveryID"]
    
    def getStarrDropEncoding(self):
        return self.starr_drop_encoding_data
    
    def setStarrDropEncodingData(self, starr_drop_encoding):
        self.starr_drop_encoding_data = starr_drop_encoding

    def refreshData(self):
        self.starr_drop_encoding_data.pop(0)
        self.setStarrDropEncodingData(self.starr_drop_encoding_data)
    
    def getRewarditemID(self, item, min=None, max=None, additional=None):
        if item == "Skin":
            skin_possibilities = self.skin.getSkinsIDSSpecificPrice(min, max)
            skin_awarded = random.randint(0, len(skin_possibilities) -1)
            return skin_possibilities[skin_awarded]
        elif item == "Pin":
            pin_possibilities = self.pin.getPinsIDSSpecificPrice(min, max)
            pin_awarded = random.randint(0, len(pin_possibilities) -1)
            return pin_possibilities[pin_awarded]
        elif item == "Spray":
            spray_possibilities = self.spray.getSpraysIDSSpecificPrice(min, max)
            spray_awarded = random.randint(0, len(spray_possibilities) -1)
            return spray_possibilities[spray_awarded]
        elif item == "Brawler":
            brawler_possibilities = self.brawler.getBrawlerFromSepcificRarity(additional)
            brawler_awarded = random.randint(0, len(brawler_possibilities) -1)
            return brawler_possibilities[brawler_awarded]
        elif item == "StarPower" or item == "Gadget":
            card_possibilities = self.card.getCardsListFromMetaType(additional)
            card_awarded = random.randint(0, len(card_possibilities) -1)
            return card_possibilities[card_awarded]
        elif item == "ProfilePic":
            return random.randint(0, self.profile_pic.getThumbnailsCount())
        
    def updateCount(self, rarity_id):
        if rarity_id == 0:
            self.rare_count +=1
        elif rarity_id == 1:
            self.super_rare_count += 1
        elif rarity_id == 2: 
            self.epic_count += 1
        elif rarity_id == 3:
            self.mythic_count += 1
        elif rarity_id == 4:
            self.legendary_count += 1

    def encode(self, ByteStream):
        ByteStream.writeVInt(5)
        for i in range(5):
            ByteStream.writeDataReference(80, i)
            ByteStream.writeVInt(-1)
            ByteStream.writeVInt(0)
        ByteStream.writeVInt(len(self.starr_drop_encoding_data))
        for x in range(len(self.starr_drop_encoding_data)):
            ByteStream.writeDataReference(80,self.starr_drop_encoding_data[len(self.starr_drop_encoding_data )-x -1][0])
        ByteStream.writeVInt(len(self.starr_drop_encoding_data))
        for x in range(len(self.starr_drop_encoding_data)):
            ByteStream.writeByte(1)
            reward_type = self.starr_drop_encoding_data[x][1]
            offer_id_type = self.items_ids[reward_type]["OfferID"]
            ByteStream.writeVInt(offer_id_type)
            ByteStream.writeVInt(self.starr_drop_encoding_data[x][2])
            ByteStream.writeDataReference(0, 0)
            ByteStream.writeVInt(0)
        ByteStream.writeInt(-1788180018)
        ByteStream.writeVInt(0) # progression step in battles
        ByteStream.writeVInt(0)
        ByteStream.writeVInt(73529) # timer until refresh
        ByteStream.writeVInt(0) #v51 new count
        ByteStream.writeVInt(0) #v51 new count

starrDropOpening = LogicStarrDropData()

