import csv


class Cards:
    def getCardsListFromMetaType(self, meta_type):
        CardsID = []
        with open('Classes/Files/Assets/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[8] == str(meta_type) and row[4].lower() != "true":
                        CardsID.append(line_count - 2)
                    line_count += 1

            return CardsID
        
    def getBrawlerFromSepcificRarity(self, rarity):
        BrawlersCardsIds = []
        codenames = []
        Brawlers = []
        with open('Classes/Files/Assets/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[8] == '0' and row[4].lower() != "true" and row[15].lower() == rarity:
                        BrawlersCardsIds.append(line_count - 2)
                        codenames.append(row[3])
                    line_count += 1
            with open("Classes/Files/Assets/characters.csv") as characters:
                csv_reader = csv.reader(characters, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0 or line_count == 1:
                        line_count+=1
                    else:
                        if row[0] in codenames and row[26] == 'Hero':
                            Brawlers.append(line_count -2)
            return Brawlers
