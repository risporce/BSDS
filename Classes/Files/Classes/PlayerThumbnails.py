import csv


class PlayerThumbnails:
    def getThumbnailsCount(self):
        with open('Classes/Files/Assets/player_thumbnails.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if row[0] != "":
                    line_count += 1
            return line_count - 3