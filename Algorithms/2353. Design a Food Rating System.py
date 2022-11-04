from typing import List
from sortedcontainers import SortedDict, SortedSet, SortedList
from collections import defaultdict

"""
# Method 1: Use SortedDict and SortedSet. More conplex than necessary, because we
# need to delete empty containers.

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.data = defaultdict(SortedDict)
        self.map = {}
        self.rating = {}
        for i in range(len(foods)):
            f = foods[i]
            c = cuisines[i]
            r = ratings[i]
            if r in self.data[c]:
                self.data[c][r].add(f)
            else:
                ss = SortedSet()
                ss.add(f)
                self.data[c][r] = ss
            self.map[f] = c
            self.rating[f] = r

    def changeRating(self, food: str, newRating: int) -> None:
        ctype = self.map[food]
        oldrating = self.rating[food]
        if oldrating == newRating:
            return
        if newRating in self.data[ctype]:
            self.data[ctype][newRating].add(food)
        else:
            ss = SortedSet()
            ss.add(food)
            #self.data[ctype].setdefault(newRating, ss)
            self.data[ctype][newRating] = ss
        self.data[ctype][oldrating].remove(food)
        if len(self.data[ctype][oldrating]) == 0:
            del self.data[ctype][oldrating]
        self.rating[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        setv = self.data[cuisine].peekitem()
        return setv[1][0]

"""

## Method 2: preferred method. Use SortedList.
## Time: O(log(n))
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cui = {}
        self.cur_rating = {}
        self.ratings = defaultdict(SortedList)
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cui[f] = c
            self.cur_rating[f] = -r
            self.ratings[c].add((-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cui = self.food_to_cui[food]
        cur_rating = self.cur_rating[food]
        self.ratings[cui].remove((cur_rating, food))
        self.ratings[cui].add((-newRating, food))
        self.cur_rating[food] = -newRating

    def highestRated(self, cuisine: str) -> str:
        return self.ratings[cuisine][0][1]


if __name__ == '__main__':
    def tester(calls, paras):
        assert len(calls) == len(paras)
        assert calls[0] == "FoodRatings"

        #obj = FoodRatings(paras[0][0], paras[0][1], paras[0][2])
        obj = FoodRatings(*paras[0])
        print(None)
        for i in range(1, len(calls)):
            if calls[i] == "highestRated":
                print(obj.highestRated(*paras[i]))
            elif calls[i] == "changeRating":
                print(obj.changeRating(*paras[i]))
            else:
                RuntimeError("Error")

    # calls = ["FoodRatings", "highestRated", "highestRated",
    #          "changeRating", "highestRated", "changeRating", "highestRated"]
    # paras = [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], 
    # ["korean", "japanese", "japanese", "greek", "japanese","korean"], 
    # [9, 12, 8, 15, 14, 7]], 
    # ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]

    calls = ["FoodRatings","changeRating","changeRating","highestRated","changeRating","changeRating","highestRated","highestRated","highestRated","changeRating","highestRated","changeRating","highestRated","changeRating","changeRating","highestRated","changeRating","highestRated","changeRating","changeRating","changeRating","highestRated","changeRating","highestRated","changeRating","changeRating","highestRated","highestRated","highestRated","changeRating","highestRated","highestRated","changeRating","highestRated","changeRating","changeRating","highestRated","highestRated","changeRating","changeRating","highestRated","changeRating","changeRating","changeRating","changeRating","changeRating","changeRating","changeRating","highestRated","changeRating","changeRating","changeRating","changeRating","changeRating","changeRating","highestRated","changeRating","highestRated","changeRating","highestRated","changeRating","highestRated","changeRating","changeRating","changeRating","highestRated","changeRating","changeRating","highestRated","changeRating","changeRating","highestRated","changeRating","highestRated","highestRated","highestRated","changeRating","changeRating","highestRated","changeRating","highestRated","highestRated","changeRating","highestRated","highestRated","highestRated","highestRated","changeRating","changeRating","highestRated","changeRating","changeRating","changeRating","highestRated","changeRating","changeRating","changeRating","highestRated","highestRated","highestRated","highestRated","highestRated","changeRating","changeRating","highestRated","highestRated","changeRating","changeRating","changeRating","highestRated","highestRated","highestRated","highestRated"]
    paras = [[["wayfnkzb","eqiyfjefmx","pfe","atlqeka","iqtf","akbtinchc","pchazissxl","qfehnltip","vyavqiaha","gpkieuuj","cmmevexdu","vy","skrqgtqcol","xsydpmavlp","cprtdfwmcl","iqmcqgb","mzwtzlvjud","dqgys","emdmcsv","ebrckogq","txnsrgoz","bogmosr","usmxuzwwwg","kxwhpirwqd","nmuukr","wnhajrqpux","stczw","sywjkh","hmodhglhuy","fbrefccega","sgcggzyjbe","dcfzm","inuzyvkre","uvbeprr","nbbgq","yohckl","mulurwuvrd","dwlqqoxz","ejzec","rd","rgaxj","wsjswolesx","dmddhdnhm","woguqmkc","hhmkj","dcveeeor","holkfujdgy","lg","uxbmcubn","qsdouuk","orqn","uyyksfql","gxdhpvy","bhwxoepw","ynmtwtb","cfcqsiitm","ezwsqzcyy","toafgd","izqhhhkdwe","itcxa","senrcaz","uvnogrjcr","qeeclian","zslurjd","bzlvx","aibtvlpryg","oyqxgjyrnh","lmmwtkgyyo","mynkq","rhxfybuakp","vvadaflbt","opcpi","ytqmebeo","qevszdh","itkvzv","qqtjye","aqjwrbyr","potiiecni","smqifbhwzm","hyhza","cvfi"],["ikzdtynn","tm","tvmsdpsup","tvmsdpsup","ikzdtynn","tm","tm","jbatpoby","vrchucermi","ylfyymwb","tvmsdpsup","ikzdtynn","jbatpoby","ikzdtynn","dm","jbatpoby","vrchucermi","tvmsdpsup","tm","dm","dm","tm","jbatpoby","ylfyymwb","ylfyymwb","vrchucermi","jbatpoby","vrchucermi","tvmsdpsup","ikzdtynn","tvmsdpsup","ikzdtynn","tm","dm","jbatpoby","jbatpoby","vrchucermi","ylfyymwb","tm","tvmsdpsup","vrchucermi","ikzdtynn","ylfyymwb","ylfyymwb","ylfyymwb","tm","tvmsdpsup","tm","tvmsdpsup","dm","dm","ylfyymwb","dm","ylfyymwb","jbatpoby","tvmsdpsup","ikzdtynn","ikzdtynn","ylfyymwb","dm","tm","vrchucermi","dm","jbatpoby","ylfyymwb","tvmsdpsup","dm","ylfyymwb","jbatpoby","dm","tvmsdpsup","ikzdtynn","tm","ikzdtynn","ylfyymwb","ikzdtynn","tm","tm","dm","ikzdtynn","ylfyymwb"],[577,115,150,549,727,490,585,511,700,724,641,539,282,439,229,97,524,511,27,713,359,232,895,769,326,186,342,913,915,523,360,903,310,355,383,173,129,6,579,7,49,168,711,925,524,882,393,848,165,652,692,39,370,252,472,472,875,844,562,436,901,329,597,645,208,444,219,873,924,597,210,774,805,331,919,548,145,162,537,818,848]],["txnsrgoz",657],["bzlvx",932],["tvmsdpsup"],["wsjswolesx",159],["toafgd",75],["tvmsdpsup"],["jbatpoby"],["ikzdtynn"],["dcveeeor",698],["vrchucermi"],["emdmcsv",634],["tm"],["dqgys",975],["nmuukr",509],["ikzdtynn"],["woguqmkc",779],["jbatpoby"],["usmxuzwwwg",857],["bogmosr",900],["uvnogrjcr",768],["tvmsdpsup"],["vy",522],["tm"],["rd",881],["vy",373],["dm"],["jbatpoby"],["jbatpoby"],["qevszdh",880],["ikzdtynn"],["vrchucermi"],["holkfujdgy",481],["vrchucermi"],["woguqmkc",596],["opcpi",702],["jbatpoby"],["ylfyymwb"],["smqifbhwzm",418],["uxbmcubn",161],["dm"],["potiiecni",496],["gxdhpvy",764],["rd",330],["holkfujdgy",949],["pchazissxl",296],["qqtjye",763],["inuzyvkre",25],["dm"],["ezwsqzcyy",101],["gpkieuuj",484],["nbbgq",545],["toafgd",347],["bzlvx",567],["cfcqsiitm",230],["jbatpoby"],["iqtf",588],["ylfyymwb"],["toafgd",93],["ylfyymwb"],["ynmtwtb",927],["tvmsdpsup"],["ezwsqzcyy",32],["akbtinchc",129],["uxbmcubn",174],["ylfyymwb"],["atlqeka",186],["qevszdh",964],["tm"],["aibtvlpryg",270],["toafgd",911],["ikzdtynn"],["zslurjd",900],["tm"],["tvmsdpsup"],["ylfyymwb"],["qsdouuk",847],["bogmosr",131],["dm"],["kxwhpirwqd",729],["dm"],["tm"],["iqmcqgb",48],["tm"],["dm"],["tm"],["dm"],["uxbmcubn",364],["itcxa",285],["tm"],["iqmcqgb",500],["sywjkh",915],["rd",774],["vrchucermi"],["izqhhhkdwe",753],["usmxuzwwwg",938],["skrqgtqcol",644],["jbatpoby"],["tvmsdpsup"],["tvmsdpsup"],["dm"],["tvmsdpsup"],["mynkq",540],["rgaxj",437],["ikzdtynn"],["dm"],["senrcaz",9],["rd",14],["gxdhpvy",390],["ikzdtynn"],["dm"],["ikzdtynn"],["dm"]]
    
    tester(calls, paras)
