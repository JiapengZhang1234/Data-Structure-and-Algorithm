#解法4：技术比较

#解题思路：对比两个词中每个字符的出现次数
#如果26个字母出现的次数都相同的话，这两个
#字符串就一定是变位词

#具体做法：为每个词设置一个26位的计数器，先检查
#每个词，在计数器中设定好每个字母的出现次数
#计数完成后，进入比较阶段，看两个字符串的计数器是否相同
#如果相同则输出是变位词的结论

def anagramsolution4(s1,s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    still0k = True
    while j < 26 and still0k:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still0k = False
    return still0k

print(anagramsolution4('apple','pleap'))
print(anagramsolution4('zhangjiapeng','zhangjiaxuan'))

#算法分析  三个循环迭代，总操作次数是T(n) = 2n + 26,其数量级为O(n)
#这是一个线性数量级的算法，是四个变位词判断算法中最优的
