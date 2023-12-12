class schoolware_tools():
    def __init__(self,schoolware) -> None:
        self.schoolware = schoolware
        self.scores = []
        self.DW1 = []
        self.DW2 = []
        self.DW3 = []
        self.DW4 = []
        self.DW5 = []
        self.vaardig = 0.75

    def vaardigheden(self, list):
        total_kennis = 0
        total_vaardig = 0
        len_kennis = 0
        len_vaardig = 0
        for i in list:
            try:
                #print(f"Titel: {i['titel']} Cat: {i['cat']}")
                if("Vaardigheden" in i["cat"]):
                    punt = i["score"]
                    total_vaardig += punt * i["tot_sc"]
                    len_vaardig += i["tot_sc"]
                else:
                    punt = i["score"] * i["tot_sc"]
                    total_kennis += punt
                    len_kennis += i["tot_sc"]


            except ZeroDivisionError:
                print("zero division error")
                 
        #print(f"vaardig: {total_vaardig}/{len_vaardig}")
        #print(f"kennis: {total_kennis}/{len_kennis}")
        if(len_kennis != 0 and len_vaardig != 0): 
            total = round(((total_kennis/len_kennis * (1-self.vaardig)) + (total_vaardig/len_vaardig * self.vaardig)), 1)
        elif(len_vaardig != 0) :
            total = round(((total_vaardig/len_vaardig)), 1)
        elif(len_kennis != 0):
            total = round(((total_kennis/len_kennis)), 1)
        else:
            return "n/a"
        return total

    def mean(self, list):
        points = []
        tot = 0
        if(self.vak in self.vaardigheden_vakken):
            return self.vaardigheden(list)
        else:
            try:
                for i in list:
                    points.append(i["score"] * i['tot_sc'])
                    tot += i['tot_sc']
                total = round(sum(points) / tot, 1)
                return total
            except ZeroDivisionError:
                return "n/a"
        
    def split_dw(self,scores):
        
        for i in scores:
            match i["DW"]:
                case "DW 1":
                    self.DW1.append(i)
                case "DW 2":
                    self.DW2.append(i)
                case "DW 3":
                    self.DW3.append(i)
                case "DW 4":
                    self.DW4.append(i)
                case "DW 5":
                    self.DW5.append(i)

    def main(self,vak,vaardigheden, ex1="", ex2="", punten=""):
        self.scores = []
        self.DW1 = []
        self.DW2 = []
        self.DW3 = []
        self.DW4 = []
        self.DW5 = []
        self.vak = vak
        self.vaardigheden_vakken = vaardigheden
        self.ex1=ex1
        self.ex2=ex2

        if(punten == ""):
            punten = self.schoolware.punten()

        for i in punten:
            if(i["vak"] == self.vak):
                if(i["score"] != 'n/a'):
                    self.scores.append({
                        "titel": i["titel"],
                        "DW": i["DW"],
                        "score": float(i["score"]) * 100,
                        "cat": i["cat"],
                        "tot_sc": i['tot_sc']
                    })
        
        self.split_dw(self.scores)

        all = self.DW1 + self.DW2 + self.DW3 + self.DW4 + self.DW5
        if(self.ex1 != [] and self.ex1 != ""):
            all += self.ex1
        if(self.ex2 != [] and self.ex2 != ""):
            all += self.ex2
        return {
            "vak": vak,
            "DW1": self.mean(self.DW1),
            "DW2": self.mean(self.DW2),
            "DW3": self.mean(self.DW3),
            "DW4": self.mean(self.DW4),
            "DW5": self.mean(self.DW5),
            "jaar": self.mean(all)
        }
    def alle_vakken(self,vakken,vaardigheden, ex1="", ex2=""):
        punten = self.schoolware.punten()
        jaartotaal_result = []
        for vak in vakken:
            jaartotaal_result.append(self.main(vak=vak,vaardigheden=vaardigheden, punten=punten))
        return jaartotaal_result
