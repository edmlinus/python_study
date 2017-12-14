import operator
import math
from lovely_dictionaries import nameDic, albumDic, timeDic
import math

# 데이터 문자열 한 라인을 설문답변 데이터 딕셔너리를 만든다.
def lineToDic(line):
    cols = line.replace("\n", "").split(",")
    dic = {"q1": timeDic[(cols[1])], "q2": int(cols[2]), "q3": int(cols[3]), "q4": rankDic(cols[4])}
    return dic


# 순위 스트링을 받아 순위 딕셔너리(곡아이디:순위)를 만든다
def rankDic(rankStr):
    rank_list = rankStr.split(":")
    if rank_list[0] == "99":
        rank_list.remove("99")
        rank_list.append("99")
    list2 = rank_list[0:rank_list.index("99")]
    return {k: v + 1 for v, k in enumerate(list2)}

def albumCounts(dic):
    abdic = {}
    data = dic["q4"]
    for msname,rank in data.items():
        for abname in albumDic.keys():
            if msname in albumDic[abname]:
                if abname in abdic.keys():
                    abdic[abname].append(37-rank)
                else:
                    abdic[abname] = [37-rank]
    for abname in abdic.keys():
        abdic[abname] = int(sum(abdic[abname])/len(abdic[abname]))
    return abdic

##
def countAlbumRank(abdic,data):
    for abname, point in data.items():
        if abname in abdic.keys():
            abdic[abname].append(point)
        else:
            abdic[abname]=[point]

##
def createAlbumCountDic(lst):
    abdic = {}
    for data in lst:
        countAlbumRank(abdic, data)
    for abname in abdic.keys():
        total = sum(abdic[abname])
        total2 = sum(list(map(lambda d: d**2, abdic[abname])))
        avg = total/len(abdic[abname])
        avg2 = total2/len(abdic[abname])
        dev = avg2 - (avg**2)
        std = math.sqrt(dev)
        abdic[abname] = (total, int(avg), int(std))
    return abdic

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
        total, _, _ = getStats(it)
        res[it[0]] = total
    ranks = sorted(res.items(), key=operator.itemgetter(1))
    ranks.reverse()
    return [(k + 1, v[0], nameDic[v[0]], v[1]) for k, v in enumerate(ranks)]


def getStats(it):
    total = sum([(37 - k) * v for k, v in it[1].items()])
    total2 = sum([(37 - k) ** 2 * v for k, v in it[1].items()])
    avg = total / sum(it[1].values())
    avg2 = total2 / sum(it[1].values())
    variance = avg2 - avg ** 2
    return total, int(avg), int(math.sqrt(variance))


# 곡별 순위카운트 딕셔너리를 리턴한다.
def createMusicCountDic(rank_list):
    msdic = {}
    for data in rank_list:
        countRank(msdic, data["q4"])
    for music_name in msdic.keys():
        mslist = sorted(msdic[music_name].items(), key=operator.itemgetter(1))
        mslist.reverse()
        msdic[music_name] = {pair[0]: pair[1] for pair in mslist}
    return msdic


# input list [(rank,id,name,points)],name(str)
# output dict {albumID:points.avg}
# 앨범 별 총점을 계산한다
def getAlbumPoint(data, name):
    total_point = 0
    for _, music_id, _, point in data:
        if music_id in albumDic[name]:
            total_point += point
    return total_point

