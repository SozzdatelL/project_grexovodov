#написать код что бы в выводе была кличка собаки, порода, окрас.
class Zhivotnoe:
    def __init__(self, vid, kolichestvo_lap, tsvet_shersti):
        self.vid = vid
        self.kolichestvo_lap = kolichestvo_lap
        self.tsvet_shersti = tsvet_shersti


class Sobaka(Zhivotnoe):
    def __init__(self, vid, kolichestvo_lap, tsvet_shersti, klichka, poroda):
        super().__init__(vid, kolichestvo_lap, tsvet_shersti)
        self.klichka = klichka
        self.poroda = poroda


dog = Sobaka("sobaka", 4, "ryzhiy", "Sharik", "Dvornaga")
print(dog.klichka, dog.poroda, dog.vid)
