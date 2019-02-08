def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':

    dic = {}

    for i in J:

        dic[i] = S.count(i)



    return sum(dic.values())