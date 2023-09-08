import csv

class Skins:
    def getSkinsIDSSpecificPrice(self, min, max):
        SkinsID = []
        with open('Classes/Files/Assets/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[2].lower() != 'true':
                        skin_gem_price = row[15]
                        if (skin_gem_price != ''):
                            if int(skin_gem_price) >= min and int(skin_gem_price) <= max:
                                SkinsID.append(line_count - 2)
                    if row[0] != "":
                        line_count += 1

            return SkinsID
