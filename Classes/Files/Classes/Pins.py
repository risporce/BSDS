import csv

class Emotes:

    def getPinsIDSSpecificPrice(self, min, max):
        EmotesID = []
        with open('Classes/Files/Assets/emotes.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[1].lower() != 'true':
                        pin_gem_price = row[18]
                        if (pin_gem_price != ''):
                            if int(pin_gem_price) >= min and int(pin_gem_price) <= max:
                                EmotesID.append(line_count - 2)
                    if row[0] != "":
                        line_count += 1

            return EmotesID