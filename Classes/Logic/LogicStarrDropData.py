from Classes.Files.Classes.Cards import Cards
from Classes.Files.Classes.Pins import Emotes
from Classes.Files.Classes.PlayerThumbnails import PlayerThumbnails
from Classes.Files.Classes.Skins import Skins
from Classes.Files.Classes.Sprays import Sprays
from Classes.Files.Classes.Characters import Characters

import random

shop_ids = {
    "Coins": {
        "OfferID": 1,
    },
    "TokenDoubler": {
        "OfferID": 9,
    },
    "Credits": {
        "OfferID": 38,
    },
    "ChromaCredits": {
        "OfferID": 39,
    },
    "PowerPoints": {
        "OfferID": 41,
    },
    "Blings": {
        "OfferID": 45,
    },
    "Brawler": {
        "OfferID": 3,
    },
    "Skin": {
        "OfferID": 4,
    },
    "Pin": {
        "OfferID": 19,
    },
    "ProfilePic": {
        "OfferID": 25,
    },
    "Spray": {
        "OfferID": 35,
    },
    "StarPower": {
        "OfferID": 5,
    },
    "Gadget": {
        "OfferID": 5,
    },
    "Overcharge": {
        "OfferID": 47,
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
                "Tickets": 90,
                "Min": 50,
                "Max": 50,
                "Fallback": []
            },
            "PowerPoints_s": {
                "Type": "PowerPoints",
                "Tickets": 70,
                "Min": 25,
                "Max": 25,
                "Fallback": []
            },
            "Credits_s": {
                "Type": "Credits",
                "Tickets": 5,
                "Min": 10,
                "Max": 10,
                "Fallback": []
            },
            "Blings_s": {
                "Type": "Blings",
                "Tickets": 5,
                "Min": 20,
                "Max": 20,
                "Fallback": []
            },
            "TokenDoubler_s": {
                "Type": "TokenDoubler",
                "Tickets": 45,
                "Min": 100,
                "Max": 100,
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
                "Tickets": 64,
                "Min": 100,
                "Max": 100,
                "Fallback": []
            },
            "PowerPoints_m": {
                "Type": "PowerPoints",
                "Tickets": 50,
                "Min": 50,
                "Max": 50,
                "Fallback": []
            },
            "Credits_m": {
                "Type": "Credits",
                "Tickets": 5,
                "Min": 30,
                "Max": 30,
                "Fallback": []
            },
            "Blings_m": {
                "Type": "Blings",
                "Tickets": 5,
                "Min": 50,
                "Max": 50,
                "Fallback": []
            },
            "Pin_1-9Gems": {
                "Type": "Pin",
                "Tickets": 5,
                "MinPrice": 1,
                "MaxPrice": 9,
                "Fallback": ["Credits", 100]
            },
            "Spray_1-19Gems": {
                "Type": "Spray",
                "Tickets": 2,
                "MinPrice": 1,
                "MaxPrice": 19,
                "Fallback": ["Credits", 100]
            },
            "TokenDoubler_m": {
                "Type": "TokenDoubler",
                "Tickets": 20,
                "Min": 200,
                "Max": 200,
                "Fallback": ["Credits", 100]
            }
        }
    },
    "Epic": {
        "Rarity_ID": 2,
        "DropChance": 15,
        "TotalTickets": 95,
        "Possibilities": {
            "Coins_l": {
                "Type": "Coins",
                "Tickets": 20,
                "Min": 200,
                "Max": 200,
                "Fallback": []
            },
            "PowerPoints_l": {
                "Type": "PowerPoints",
                "Tickets": 20,
                "Min": 100,
                "Max": 100,
                "Fallback": []
            },
            "Brawler_Rare": {
                "Type": "Brawler",
                "Rarity": "rare",
                "Tickets": 5,
                "Fallback": ["Credits", 100]
            },
            "Skin_1-29Gems": {
                "Type": "Skin",
                "Tickets": 5,
                "MinPrice": 1,
                "MaxPrice": 29,
                "Fallback": ["Blings", 500]
            },
            "Pin_1-9Gems": {
                "Type": "Pin",
                "Tickets": 15,
                "MinPrice": 1,
                "MaxPrice": 9,
                "Fallback": ["Blings", 100]
            },
            "Pin_10-29Gems": {
                "Type": "Pin",
                "Tickets": 5,
                "MinPrice": 10,
                "MaxPrice": 29,
                "Fallback": ["Blings", 100]
            },
            "Spray_1-19Gems": {
                "Type": "Spray",
                "Tickets": 15,
                "MinPrice": 1,
                "MaxPrice": 19,
                "Fallback": ["Blings", 100]
            },
            "TokenDoubler_l": {
                "Type": "TokenDoubler",
                "Tickets": 10,
                "Min": 500,
                "Max": 500,
                "Fallback": ["Credits", 100]
            }
        }
    },
    "Mythic": {
        "Rarity_ID": 3,
        "DropChance": 5,
        "TotalTickets": 158,
        "Possibilities": {
            "Coins_xl": {
                "Type": "Coins",
                "Tickets": 15,
                "Min": 500,
                "Max": 500,
                "Fallback": []
            },
            "Gadget": {
                "Type": "Gadget",
                "Tickets": 25,
                "Fallback": ["Coins", 1000]
            },
            "PowerPoints_xl": {
                "Type": "PowerPoints",
                "Tickets": 30,
                "Min": 200,
                "Max": 200,
                "Fallback": []
            },
            "Brawler_SuperRare": {
                "Type": "Brawler",
                "Rarity": "super_rare",
                "Tickets": 15,
                "Fallback": ["Credits", 200]
            },
            "Brawler_Epic": {
                "Type": "Brawler",
                "Rarity": "epic",
                "Tickets": 10,
                "Fallback": ["Credits", 500]
            },
            "Brawler_Mythic": {
                "Type": "Brawler",
                "Rarity": "mega_epic",
                "Tickets": 3,
                "Fallback": ["Credits", 1000]
            },
            "Skin_1-29Gems": {
                "Type": "Skin",
                "Tickets": 25,
                "MinPrice": 1,
                "MaxPrice": 29,
                "Fallback": ["Blings", 500]
            },
            "Pin_10-29Gems": {
                "Type": "Pin",
                "Tickets": 10,
                "MinPrice": 10,
                "MaxPrice": 29,
                "Fallback": ["Blings", 100]
            },
            "Pin_30-39Gems": {
                "Type": "Pin",
                "Tickets": 5,
                "MinPrice": 30,
                "MaxPrice": 999,
                "Fallback": ["Blings", 100]
            },
            "Spray_20-29Gems": {
                "Type": "Spray",
                "Tickets": 10,
                "MinPrice": 20,
                "MaxPrice": 999,
                "Fallback": ["Blings", 100]
            },
            "ProfilePic": {
                "Type": "ProfilePic",
                "Tickets": 10,
                "Fallback": ["Blings", 100]
            }
        }

    },
    "Legendary": {
        "Rarity_ID": 4,
        "DropChance": 2,
        "TotalTickets": 92,
        "Possibilities": {
            "StarPower": {
                "Type": "StarPower",
                "Tickets": 25,
                "Fallback": ["Coins", 1000]
            },
            "Brawler_Epic": {
                "Type": "Brawler",
                "Rarity": "epic",
                "Tickets": 10,
                "Fallback": ["Credits", 500]
            },
            "Brawler_Mythic": {
                "Type": "Brawler",
                "Rarity": "mega_epic",
                "Tickets": 5,
                "Fallback": ["Credits", 1000]
            },
            "Brawler_Legendary": {
                "Type": "Brawler",
                "Rarity": "legendary",
                "Tickets": 2,
                "Fallback": ["Credits", 1000]
            },
            "Skin_30-79Gems": {
                "Type": "Skin",
                "Tickets": 33,
                "MinPrice": 30,
                "MaxPrice": 79,
                "Fallback": ["Blings", 1000]
            },
            "Skin_80-149Gems": {
                "Type": "Skin",
                "Tickets": 2,
                "MinPrice": 80,
                "MaxPrice": 149,
                "Fallback": ["Blings", 1000]
            },
            "Overcharge": {
                "Type": "Overcharge",
                "Tickets": 15,
                "Fallback": ["Coins", 1000]
            }
        }

    },
}
class LogicStarrDropData():
    def __init__(self):
        self.starrDrop_data = starrDrop_data
        self.shop_ids = shop_ids
        self.starr_drop_encoding_data = []
        self.range_price_items = ["Skin", "Pin", "Spray"]
        self.skin = Skins()
        self.pin = Emotes()
        self.spray = Sprays()
        self.brawler = Characters()
        self.card = Cards()
        self.starPowerIds = self.card.getCardsListFromMetaType(4)
        self.GadgetIds = self.card.getCardsListFromMetaType(5)
        self.OverchargeIds = self.card.getCardsListFromMetaType(6)
        self.profile_pic = PlayerThumbnails()
        self.profile_pic_count = self.profile_pic.getThumbnailsCount()
        self.rare_count = 0
        self.super_rare_count = 0
        self.epic_count = 0
        self.mythic_count = 0
        self.legendary_count = 0

        self.coin_total = 0
        self.powerPoint_total = 0
        self.tokenDoubler_Total = 0
        self.bling_total = 0
        self.skin_total = 0
        self.brawler_total = 0
        self.spray_total = 0
        self.pin_total = 0
        self.credit_total = 0
        self.gadget_total = 0
        self.starPower_total = 0
        self.overcharge_total = 0
        self.profilePic_total = 0

        self.fast_open = False

    def choose_random_starrDrop(self):
        drop_types = list(self.starrDrop_data.keys())
        drop_chances = [self.starrDrop_data[drop]["DropChance"] for drop in drop_types]
        return random.choices(drop_types, weights=drop_chances, k=1)[0]
    
    def choose_random_reward(self, chosen_drop):
        rewards = list(self.starrDrop_data[chosen_drop]["Possibilities"].keys())
        reward_tickets = [self.starrDrop_data[chosen_drop]["Possibilities"][reward]["Tickets"] for reward in rewards]
        return random.choices(rewards, weights=reward_tickets, k=1)[0]

    def create_starrDrop_opening(self, drop_count, starrDrop_rarity = None, rarity_set = None):
        self.fast_open = drop_count > 100
        type_mapping = {
            "StarPower": lambda: random.randint(0, len(self.starPowerIds) - 1),
            "Gadget": lambda: random.randint(0, len(self.GadgetIds) - 1),
            "Overcharge": lambda: random.randint(0, len(self.OverchargeIds) - 1),
            "ProfilePic": lambda: random.randint(0, self.profile_pic_count),
        }
        for i in range(drop_count):
            starrDrop = []
            if rarity_set is None:
                starrDrop_rarity = self.choose_random_starrDrop()
                starrDrop_reward = self.choose_random_reward(starrDrop_rarity)
            else:
                starrDrop_reward = self.choose_random_reward(starrDrop_rarity)
            starrDrop_type = self.starrDrop_data[f"{starrDrop_rarity}"]["Possibilities"][f"{starrDrop_reward}"]["Type"]
            starrDrop_reward_amount = self.starrDrop_data[f"{starrDrop_rarity}"]["Possibilities"][f"{starrDrop_reward}"].get("Min", 1)
            self.updateCount(self.starrDrop_data[f"{starrDrop_rarity}"]["Rarity_ID"], starrDrop_type, starrDrop_reward_amount)
            starrDrop.extend([
                self.starrDrop_data[f"{starrDrop_rarity}"]["Rarity_ID"],
                starrDrop_type,
                starrDrop_reward_amount
            ])
            if starrDrop_type in self.range_price_items:
                starrDrop.append(self.getRewarditemID(starrDrop_type, min=self.starrDrop_data[f"{starrDrop_rarity}"]["Possibilities"][f"{starrDrop_reward}"]["MinPrice"], max=self.starrDrop_data[f"{starrDrop_rarity}"]["Possibilities"][f"{starrDrop_reward}"]["MaxPrice"]))
            elif starrDrop_type == "Brawler":
                brawler_possibilities = self.brawler.getBrawlerFromSepcificRarity(self.starrDrop_data[f"{starrDrop_rarity}"]["Possibilities"][f"{starrDrop_reward}"]["Rarity"])
                starrDrop.append(random.randint(0, len(brawler_possibilities) -1))
            elif starrDrop_type in type_mapping:
                starrDrop.append(type_mapping[starrDrop_type]())

            self.starr_drop_encoding_data.append(starrDrop)
        print(self.prettyPrintRewards())
    
    def getStarrDropEncoding(self):
        return self.starr_drop_encoding_data
    
    def setStarrDropEncodingData(self, starr_drop_encoding):
        self.starr_drop_encoding_data = starr_drop_encoding

    def refreshData(self):
        self.starr_drop_encoding_data.pop(0)
    
    def getRewarditemID(self, item, min=None, max=None):
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
        
    def updateCount(self, rarity_id, reward, amount):
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

        if reward == "Coins":
            self.coin_total += amount
        elif reward == "PowerPoints":
            self.powerPoint_total += amount
        elif reward == "TokenDoubler":
            self.tokenDoubler_Total += amount
        elif reward == "Credits":
            self.credit_total += amount
        elif reward == "Blings":
            self.bling_total += amount
        elif reward == "Pin":
            self.pin_total += amount
        elif reward == "Skin":
            self.skin_total += amount
        elif reward == "Spray":
            self.spray_total += amount
        elif reward == "Gadget":
            self.gadget_total += amount
        elif reward == "StarPower":
            self.starPower_total += amount
        elif reward == "Overcharge":
            self.overcharge_total += amount
        elif reward == "Brawler":
            self.brawler_total += amount
        elif reward == "ProfilePic":
            self.profilePic_total += amount

    def prettyPrintRewards(self):
        return (f'''Coins: {self.coin_total}
PowerPoints: {self.powerPoint_total}
Token Doublers: {self.tokenDoubler_Total}
Blings: {self.bling_total}
Credits: {self.credit_total}
Pin: {self.pin_total}
Skin: {self.skin_total}
Spray: {self.spray_total}
Gadget: {self.gadget_total}
Star Power: {self.starPower_total}
HyperCharge: {self.overcharge_total}
Brawler {self.brawler_total}
Profile Icon: {self.profilePic_total} \n
Rare Starr Drop: {self.rare_count}
Super Rare Starr Drop: {self.super_rare_count}
Epic Starr Drop: {self.epic_count}
Mythic Starr Drop: {self.mythic_count}
Legendary Starr Drop: {self.legendary_count}
              ''')

    def encode(self, ByteStream):
        ByteStream.writeVInt(5)
        for i in range(5):
            ByteStream.writeDataReference(80, i)
            ByteStream.writeVInt(-1)
            ByteStream.writeVInt(0)
        if (len(self.starr_drop_encoding_data) != 0):
            ByteStream.writeVInt(1)
            ByteStream.writeDataReference(80,self.starr_drop_encoding_data[0][0])
            ByteStream.writeVInt(1)

            ByteStream.writeByte(1)
            reward_type = self.starr_drop_encoding_data[0][1]
            offer_id_type = self.shop_ids[reward_type]["OfferID"]
            ByteStream.writeVInt(offer_id_type)
            ByteStream.writeVInt(self.starr_drop_encoding_data[0][2])
            ByteStream.writeDataReference(0, 0)
            ByteStream.writeVInt(0)
        else:
            ByteStream.writeVInt(0)
            ByteStream.writeVInt(0)
        ByteStream.writeInt(-1788180018)
        ByteStream.writeVInt(0) # progression step in battles
        ByteStream.writeVInt(0)
        ByteStream.writeVInt(73529) # timer until refresh
        ByteStream.writeVInt(1) #v51 new count
        ByteStream.writeVInt(10) # vint count
        ByteStream.writeVInt(1) # count idk why
        ByteStream.writeVInt(4) # number of press before starr drop opens

starrDropOpening = LogicStarrDropData()

