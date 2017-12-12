import operator

# 데이터 문자열 한 라인을 설문답변 데이터 딕셔너리를 만든다.
def lineToDic(line):
    cols = line.replace("\n", "").split(",")
    dic = {"q1": timeDic[(cols[1])], "q2": int(cols[2]), "q3": int(cols[3]), "q4": rankDic(cols[4])}
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
    return [(k+1, v[0], nameDic[v[0]], v[1]) for k, v in enumerate(ranks)]

# input : id  output : print (8회) (입덕시기, (순위, 곡이름, 점수), 인원수)
def printRank1():
    print("")
    id = ""
    while id != "Q":
        id = input(">>")
        if id != "Q":
            for i in timeDic.values():
                flst = [d for d in filter(lambda d: d["q1"] == i, datalist)]
                msdic = createMusicCountDic(flst)
                if id in msdic.keys():
                    totranks = getTotalRanks(msdic)
                    totdic = {id: (rank, name, point) for rank, id, name, point in totranks}
                    print("{}입덕 {}명 : 순위={}, 곡={}, 점수={}".format(i, len(flst), *totdic[id]))
                else:
                    print("곡아이디를 찾을 수 없습니다.")
# input : id  output : print  (입덕시기, (순위, 곡이름, 점수), 인원수)
def printRank2():
    print("")
    id = ""
    while id != "Q":
        id = input(">>")
        if id != "Q":
            if id in musicDic.keys():
                print(totalDic[id], "\n", musicDic[id])
            else:
                print("곡아이디를 찾을 수 없습니다.")
# input : albumName output : print (앨범이름 : 총합)
def printRank3():
    print(" ")
    id = ""
    while id != "Q":
        id = input(">>")
        if id != "Q":
            if id in albumDic.keys():
                print("{} : {}".format(id, getAlbumPoint(totalRanks, id)))
            else:
                print("앨범아이디를 찾을 수 없습니다")
# input : albumName output : print(x8) (앨범이름,입덕시기:순위)
def printRank4():
    print(" ")
    id = ""
    while id != "Q":
        id = input(">>")
        if id != "Q":
            if id in albumDic.keys():
                for i in timeDic.values():
                    flst = [d for d in filter(lambda d: d["q1"] == i, datalist)]
                    msdic = createMusicCountDic(flst)
                    totranks = getTotalRanks(msdic)
                    totAlbumDic = getAlbumPoint(totranks, id)
                    print("{} 입덕 : {}x{}명".format(i, int(totAlbumDic[id]/len(flst)), len(flst)))
            else:
                print("앨범아이디를 찾을 수 없습니다")
# input : 입덕 시기 output : print (앨범이름 : 점수)
def printRank5():
    print(" ")
    i = ""
    while i != "Q":
        i = input(">>")
        if i != "Q":
            if i in timeDic.values():
                flst = [d for d in filter(lambda d: d["q1"] == i, datalist)]
                msdic = createMusicCountDic(flst)
                totranks = getTotalRanks(msdic)
                for name in albumDic.keys():
                    totAlbumDic = getAlbumPoint(totranks, name)
                    print("{}입덕 {}명 : {} 앨범 점수 {}점".format(i, len(flst), name, int(totAlbumDic[name]/len(flst))))
            elif i == "전체":
                msdic = createMusicCountDic(datalist)
                totranks = getTotalRanks(msdic)
                for name in albumDic.keys():
                    totAlbumDic = getAlbumPoint(totranks, name)
                    print("전체 {}명 : {} 앨범 점수 {}점".format(len(datalist), name, int(totAlbumDic[name] / len(datalist))))
            else:
                print("입덕시기를 찾을 수 없습니다")
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
#입덕시기와 앨범을 매치하는 딕셔너리
timeDic={
    "1": "걸인베",
    '2': "1집리팩",
    '3': "럽8",
    '4': "LVLNS",
    '5': "뉴트릴",
    '6': "RUR",
    '7': "2집리팩",
    '8': "폴인럽"
}
#곡아이디와 앨범을 매치하는 딕셔너리
albumDic = {
    "걸인베": ('11', '12', '13', '14'),
    "1집리팩": ('11', '12', '13', '14', '15', '16'),
    "럽8": ('21', '22', '23', '24', '25', '26'),
    "LVLNS": ('31', '32', '33'),
    "뉴트릴": ('41', '42', '43', '44', '45', '46'),
    "RUR": ('53', '54', '55', '56', '57', '58', '59'),
    "2집리팩": ('51', '52', '53', '54', '55', '56', '57', '58', '59'),
    "폴인럽": ('61', '62', '63', '64', '65', '66')
}

# 결과 파일을 읽어서 딕셔너리의 리스트로 만든다...
with open('result.txt', 'r') as f:
    lines = f.readlines()
    rawdata = list(map(lineToDic, lines))



# 데이터 필터들을 정의한다.
f0 = lambda d : True # 모든 투표 데이터
f1 = lambda d : len(d["q4"])==37 # 모든 순위를 결정한 투표 데이터
f2 = lambda d : d["q2"]==1 # 두번째 질문에 1로 답한 데이터
f3 = lambda d : d["q3"]==1 # 세번째 질문에 1로 답한 데이터
f4 = lambda d : d["q2"]==2 # 두번째 질문에 2로 답한 데이터
f5 = lambda d : d["q3"]==2 # 세번째 질문에 2로 답한 데이터

# 곡별 순위카운트 딕셔너리를 리턴한다.
def createMusicCountDic(list):
    dic = {}
    for data in list:
        countRank(dic, data["q4"])
    return dic

# input list [(rank,id,name,points)],id(str)
# output dict {albumID:points.avg}
# 앨범 별 총점을 계산한다
def getAlbumPoint(data,name):
    dic = {}
    for _,id,_,point in data:
        if id in albumDic[name]:
                if name in dic.keys():
                    dic[name]+=point
                else:
                    dic[name]=point
    return dic

# 데이터리스트에 필터를 적용한 후 곡별 순위카운트 딕셔너리를 구한다.
datalist = [d for d in filter(f1, rawdata)]
musicDic = createMusicCountDic(datalist)
totalRanks = getTotalRanks(musicDic)
totalDic = { id: (rank, name, point) for rank, id, name, point in totalRanks }

#출력부
for rank in totalRanks:
    print(rank)

printRank5()