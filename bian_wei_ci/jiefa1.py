#变位词判断问题

#解法1 ： 逐字检查

#解法思路
#将词1中的字符逐个到词2中检查是否存在，存在就打勾标记，防止重复检查
#如果每个字符都能找到，则两个词是变位词，否则不是

#程序设计技巧：
# 由于字符串是不可变类型，需要先复制到列表中。
# 打勾标记的实现：将词2中对应字符设置为None。

def anagramSolution1(s1,s2):
    alist = list(s2)
    pos1 = 0
    still0k = True
    while pos1 < len(s1) and still0k:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 +1
        if found:
            alist[pos2] = None
        else:
            still0k = False
        pos1 = pos1 + 1
    return still0k

print(anagramSolution1('abcd','dcba'))
print(anagramSolution1('zhangjiapeng','zhangjiaxuan'))

#算法分析
#问题规模:词中包含的字符个数n
#主要部分在于两遍循环，其复杂度为O(n的平方)
