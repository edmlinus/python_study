import operator

# 데이터 문자열 한 라인을 설문답변 데이터 딕셔너리를 만든다.
def lineToDic(line):
    cols = line.replace("\n", "").split(",")
    dic = {"q1": int(cols[1]), "q2": int(cols[2]), "q3": int(cols[3]), "q4": rankDic(cols[4])}
    return dic


# 순위 스트링을 받아 순위 딕셔너리(곡아이디:순위)를 만든다
def rankDic(rankStr):
    list = rankStr.split(":")
    if list[0] == "99":
        list.remove("99")
        list.append("99")
    list2 = list[0:list.index("99")]
    dict = {k: v + 1 for v, k in enumerate(list2)}
    return dict


# mdic 에 rank(순위 딕셔너리)를 받아 카운트를 갱신한다.
def countRank(mdic, rank):
    for m, r in rank.items():
        if m in mdic.keys():
            rdic = mdic[m]
            if r in rdic.keys():
                rdic[r] += 1
            else:
                rdic[r] = 1
        else:
            mdic[m] = {r: 1}


# 총점으로 각 곡에 대한 점수를 계산하여 정렬한 튜플(순위,곡코드,곡이름,점수)의 리스트를 반환
def getTotalRanks(mdic):
    res = {}
    for it in mdic.items():
        total = sum([(37 - k) * v for k, v in mdic[it[0]].items()])
        res[it[0]] = total
    ranks = sorted(res.items(), key=operator.itemgetter(1))
    ranks.reverse()
    return [ (k+1,v[0],nameDic[v[0]],v[1]) for k,v  in enumerate(ranks) ]

# input : id  output : print (8회) (입덕시기, (순위, 곡이름, 점수), 인원수)
def printRank1():
    print("")
    id = ""
    while id != "Q":
        id = input(">>")
        if id != "Q":
            for a1 in range(8):
                flst = [d for d in filter(lambda d: d["q1"]==a1+1 , datalist)]
                msdic = createMusicCountDic(flst)
                if id in msdic.keys():
                    totranks = getTotalRanks(msdic)
                    totdic = {id: (rank, name, point) for rank, id, name, point in totranks}
                    print(a1+1,totdic[id],len(flst))
                else:
                    print("곡아이디를 찾을 수 없습니다.")
# input : id  output : print  (입, (순위, 곡이름, 점수), 인원수)
def printRank2():
    print("")
    id = ""
    while id != "Q":
        id = input(">>")
        if id != "Q":
            if id in musicDic.keys():
                print(totalDic[id],"\n", musicDic[id])
            else:
                print("곡아이디를 찾을 수 없습니다.")
# 곡아이디와 명칭을 매칭하는 딕셔너리
nameDic = {
    "11": "(걸인베) Candy Jelly Love",
    "12": "(걸인베) 어제처럼 굿나잇",
    "13": "(걸인베) 이별 Chapter1",
    "14": "(걸인베) 비밀여행",
    "15": "(1집리팩) 안녕",
    "16": "(1집리팩) 놀이공원",
    "21": "(럽8) 아츄",
    "22": "(럽8) 작별하나",
    "23": "(럽8) 예쁜 여자가 되는 법",
    "24": "(럽8) Hug Me",
    "25": "(럽8) 새콤달콤",
    "26": "(럽8) 라푼젤",
    "31": "(LVLNS) 그대에게",
    "32": "(LVLNS) Circle",
    "33": "(LVLNS) BeBe",
    "41": "(뉴트릴) Destiny",
    "42": "(뉴트릴) 퐁당",
    "43": "(뉴트릴) 책갈피",
    "44": "(뉴트릴) 1 cm",
    "45": "(뉴트릴) 마음(*취급주의)",
    "46": "(뉴트릴) 인형",
    "51": "(2집리팩) 지금,우리",
    "52": "(2집리팩) 아야(Aya)",
    "53": "(RUR) WoW!",
    "54": "(RUR) Cameo",
    "55": "(RUR) Emotion",
    "56": "(RUR) 첫눈",
    "57": "(RUR) 똑똑",
    "58": "(RUR) Night and Day",
    "59": "(RUR) 숨바꼭질",
    "50": "(Fever) Take Me Somwhere",
    "61": "(폴인럽) 종소리",
    "62": "(폴인럽) 삼각형",
    "63": "(폴인럽) 그냥",
    "64": "(폴인럽) 비밀정원",
    "65": "(폴인럽) FALLIN'",
    "66": "(폴인럽) 졸린꿈"
}

# 결과 파일을 읽어서 딕셔너리의 리스트로 만든다...
with open('result.txt', 'r') as f:
    lines = f.readlines()
    datalist = list(map(lineToDic, lines))

#
# 데이터 필터들을 정의한다.
f0 = lambda d : True # 모든 투표 데이터
f1 = lambda d : len(d["q4"])==37 # 모든 순위를 결정한 투표 데이터
f2 = lambda d : d["q2"]==1 # 두번째 질문에 1로 답한 데이터
f3 = lambda d : d["q3"]==1 # 세번째 질문에 1로 답한 데이터
f4 = lambda d : d["q2"]==2 # 두번째 질문에 2로 답한 데이터
f5 = lambda d : d["q3"]==2 # 세번째 질문에 2로 답한 데이터
f6 = lambda d : d["q1"]==2

# 곡별 순위카운트 딕셔너리를 리턴한다.
def createMusicCountDic(list):
    dic = {}
    for data in list:
        countRank(dic, data["q4"])
    return dic

# 데이터리스트에 필터를 적용한 후 곡별 순위카운트 딕셔너리를 구한다.
filteredList = [d for d in filter(f6, datalist)]
musicDic = createMusicCountDic(filteredList)
totalRanks = getTotalRanks(musicDic)
totalDic = { id: (rank,name,point) for rank,id,name,point in totalRanks }

# 총점 기준으로 순위를 계산하여 출력
print("데이터 갯수 : ","%3d/%3d" % (len(filteredList),len(datalist)))
for rank in  totalRanks:
    print(rank)

#출력부
printRank2()