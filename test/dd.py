import random
list=['11','12','13','14','15','21','22','23','24','25','26','31','32','33','41','42','43','44','45','46','51','52','53','54','55','56','57','58','59','61','62','63','64','65','66']


with open('C:/Users/HANJUN/PycharmProjects/test/ans.txt', 'w') as f:
    for i in range(10) :
        data = random.sample(list, k=len(list))
        q1=random.randint(1,8)
        q2=random.randint(1,2)
        q3=random.randint(1,2)
        res='{},{},{},{}\n'.format(q1,q2,q3,":".join(data))
        print(res,end='')
        f.write(res)
