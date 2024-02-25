#Префикс-функция
'''
def prefix_function(text):
    n=len(text)
    pi=[0]*n
    for i in range(1,n):
        j=pi[i-1]
        while j>0 and text[i]!=text[j]:
            j=pi[j-1]
        if text[i]==text[j]:
            j+=1
        pi[i]=j
    return pi

text="123124735123124"
print(prefix_function(text))


def max_element(list_1):
    a=max(list_1)
    c=list_1.remove(a)
    b=list_1
    f=max(list_1)
    l=list_1.remove(f)
    h=list_1
    m=max(h)

    return a*f*m

list_1=[4,5,8,4,5,6,77,5,5,5,]
print(max_element(list_1))

#Алгоритм Кнута-Морриса_Прата

a = input()
l = ""
for i in range(len(a)):
    j = a[i:]
    for k in range(len(j), 0, -1):
        l += j[:k]

for i in sorted(list(set(a))):
    print("{}: {}".format(i, l.count(i)))

from math import inf


def two_functions(nums1, nums2):
    first1=0
    first2=0
    new_seq=[0]*(len(nums1)+len(nums2))
    nums1.append(inf)
    nums2.append(inf)
    for k in range(len(nums1)+len(nums2)-2):
        if nums1[first1]<nums2[first2]:
            new_seq[k]=nums1[first1]
            first1+=1
        else:
            new_seq[k]=nums2[first2]
            first2+=1
    return new_seq

nums1=[1,2,3,4]
nums2=[2,8,9]
print(two_functions(nums1, nums2))

def best_sum(players):
    bestsum=0
    nowsum=0
    last=0
    for first in range(len(players)):
        while last<len(players) and (last==first or players[first]+players[first+1]>=players[last]):
            nowsum+=players[last]
            last+=1
        bestsum=max(bestsum, nowsum)
        nowsum-=players[first]
    return bestsum


n=[1,2,3,4,5,5,55,5,6]
print(two_functions(n))
'
def lengthOfLIS(nums):
    n=0
    r=len(nums)-1
    k=0
    while n<= r:
        m=(n+r)//2
        if nums[m]<nums[m-1]:
            n=m+1
        else:
            k+=1
            r=m-1

    return k

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))




