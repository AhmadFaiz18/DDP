class Gempa:
    lokasi = ""
    skala = 0

    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self, skala):
        if skala < 2:
            print('Gempa tidak terasa')
        elif 2 <= skala <= 4:
            print('Gempa berdampak bangunan retak')
        elif 4 <= skala <= 6:
            print('Gempa berdampak bangunan roboh')
        elif skala > 6:
            print('Gempa berdampak bangunan roboh dan berpotensi tsunami')
                
        print('lokasi Gempa:',self.lokasi)
        print('skala Gempa',self.skala)