import operator
counts={'99':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'21':0,'22':0,'23':0,'24':0,'25':0,'26':0,'31':0,'32':0,'33':0,'41':0,'42':0,'43':0,'44':0,'45':0,'46':0,'50':0,'51':0,'52':0,'53':0,'54':0,'55':0,'56':0,'57':0,'58':0,'59':0,'61':0,'62':0,'63':0,'64':0,'65':0,'66':0}
with open('C:/Users/HANJUN/PycharmProjects/test/result.txt', 'r') as f:
    while 1 :
        content = f.readline().splitlines()
        if not content : break
        raw = content[0]
        data = raw.split(",")
        q1 = int(data[1])
        q2 = int(data[2])
        q3 = int(data[3])
        rank = data[4].split(":")
        print("q1={},q2={},q3={},rank={}".format(q1, q2, q3, rank))

        def countrank(n) :
            counts[n]=counts[n]+rank.index(n)+1

        for i in rank :
           countrank(i)

        print(counts)

    for r in counts.keys():
        counts[r] = counts[r] / 180
    print (counts)
    sortedcounts = sorted(counts.items(), key=operator.itemgetter(1))
    print (sortedcounts)