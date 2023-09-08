import csv

class Sprays:
    def getSpraysIDSSpecificPrice(self, min, max):
        SpraysID = []
        with open('Classes/Files/Assets/sprays.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[2].lower() != 'true':
                        spray_gem_price = row[17]
                        if (spray_gem_price != ''):
                            if int(spray_gem_price) >= min and int(spray_gem_price) <= max:
                                SpraysID.append(line_count - 2)
                    if row[0] != "":
                        line_count += 1

            return SpraysID
