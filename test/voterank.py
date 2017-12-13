from lovely_vote_func import *


# input : id  output : print (8회) (입덕시기, (순위, 곡이름, 점수), 인원수)
def printRank1():
    print("")
    music_id = ""
    while music_id != "Q":
        music_id = input(">>")
        if music_id != "Q":
            for i in timeDic.values():
                filtered_list = [d for d in filter(lambda d: d["q1"] == i, data_list)]
                msdic = createMusicCountDic(filtered_list)
                if id in msdic.keys():
                    total_ranks = getTotalRanks(msdic)
                    total_dic = {mid: (rank, name, point) for rank, mid, name, point in total_ranks}
                    print("{}입덕 {}명 : 순위={}, 곡={}, 점수={}".format(i, len(filtered_list), *total_dic[music_id]))
                else:
                    print("곡아이디를 찾을 수 없습니다.")


# input : id  output : print  (입덕시기, (순위, 곡이름, 점수), 인원수)
def printRank2():
    print("")
    music_id = ""
    while music_id != "Q":
        music_id = input(">>")
        if music_id != "Q":
            if music_id in musicDic.keys():
                print(totalDic[music_id], "\n", musicDic[music_id])
            else:
                print("곡아이디를 찾을 수 없습니다.")


# input : albumName output : print (앨범이름 : 총합)
def printRank3():
    print(" ")
    album_name = ""
    while album_name != "Q":
        album_name = input(">>")
        if album_name != "Q":
            if album_name in albumDic.keys():
                print("{} : {}".format(album_name, getAlbumPoint(totalRanks, album_name)))
            else:
                print("앨범아이디를 찾을 수 없습니다")


# input : albumName output : print(x8) (앨범이름,입덕시기:순위)
def printRank4():
    print(" ")
    album_name = ""
    while album_name != "Q":
        album_name = input(">>")
        if album_name != "Q":
            if album_name in albumDic.keys():
                for i in timeDic.values():
                    filtered_list = [d for d in filter(lambda d: d["q1"] == i, data_list)]
                    music_dic = createMusicCountDic(filtered_list)
                    total_ranks = getTotalRanks(music_dic)
                    total_album_dic = getAlbumPoint(total_ranks, album_name)
                    num_of_data = len(filtered_list)
                    print("{} 입덕 : {}x{}명".format(i, int(total_album_dic[album_name] / num_of_data), num_of_data))
            else:
                print("앨범아이디를 찾을 수 없습니다")


# input : 입덕 시기 output : print (앨범이름 : 점수)
def printRank5():
    print(" ")
    album_name = ""
    while album_name != "Q":
        album_name = input(">>")
        if album_name != "Q":
            if album_name in timeDic.values():
                filtered_list = [d for d in filter(lambda d: d["q1"] == album_name, data_list)]
                music_dic = createMusicCountDic(filtered_list)
                total_ranks = getTotalRanks(music_dic)
                for name in albumDic.keys():
                    total_album_dic = getAlbumPoint(total_ranks, name)
                    num_of_data = len(filtered_list)
                    print(f"{album_name}입덕 {num_of_data}명 : {name} 앨범 점수 {int(total_album_dic[name] / num_of_data)}점")
            elif album_name == "전체":
                music_dic = createMusicCountDic(data_list)
                total_ranks = getTotalRanks(music_dic)
                for name in albumDic.keys():
                    total_album_dic = getAlbumPoint(total_ranks, name)
                    print(f"전체 {len(data_list)}명 : {name} 앨범 점수 {int(total_album_dic[name] / len(data_list))}점")
            else:
                print("입덕시기를 찾을 수 없습니다")


# 결과 파일을 읽어서 딕셔너리의 리스트로 만든다...
with open('result.txt', 'r') as f:
    lines = f.readlines()
    raw_data = list(map(lineToDic, lines))

# 데이터 필터들을 정의한다.
f0 = lambda d: True  # 모든 투표 데이터
f1 = lambda d: len(d["q4"]) == 37  # 모든 순위를 결정한 투표 데이터
f2 = lambda d: d["q2"] == 1  # 두번째 질문에 1로 답한 데이터
f3 = lambda d: d["q3"] == 1  # 세번째 질문에 1로 답한 데이터
f4 = lambda d: d["q2"] == 2  # 두번째 질문에 2로 답한 데이터
f5 = lambda d: d["q3"] == 2  # 세번째 질문에 2로 답한 데이터

# 데이터리스트에 필터를 적용한 후 곡별 순위카운트 딕셔너리를 구한다.
data_list = [d for d in filter(f1, raw_data)]
musicDic = createMusicCountDic(data_list)
totalRanks = getTotalRanks(musicDic)
totalDic = {music_id: (rank, name, point) for rank, music_id, name, point in totalRanks}

# 출력부
for rank in totalRanks:
    print(rank)

printRank4()
