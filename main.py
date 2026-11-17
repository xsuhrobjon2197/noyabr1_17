1-m
class Hayvon:
    def __init__(self, nomi, yoshi ):
        self.nomi = nomi
        self.yoshi = yoshi

    def malumot(self):
        print(self.nomi , self.yoshi)


class It(Hayvon):
    def __init__(self, nomi, yoshi, zoti):
        super().__init__(nomi, yoshi)
        self.zoti = zoti

    def malumot(self):
        super().malumot()
        print(f"Zoti: {self.zoti}")

    it = It("Rex", 3 ,"Ovcharka")
    it.malumot()
