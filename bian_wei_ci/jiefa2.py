#解法2：排序比较

#解题思路：将两个字符串都按照字母顺序排好序，再逐个对比字符是否相同
#如果相同则是变位词，有任何不同就不是变位词

def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()
    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches

print(anagramSolution2('abced','badec'))
print(anagramSolution2('zhangjiapeng','zhangjiaxuan'))

#算法分析 本算法运行时间数量级就等于排序过程的数量级0(nlog(n))




