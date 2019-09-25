import math

def countBits(n):
    ost = 0
    list = []
    while n != 0:
        ost = n%2
        list.append(ost)
        n//=2
    count = 0
    for i in list:
        if(i==1):
            count+=1
    return count

def febonachi(n):
    if(n == 1 or n==2):
        return 1
    return febonachi(n-1)+febonachi(n-2)

def tribonacci(start, n):
    total = []
    if(n == 0 or n ==1 or n ==2):
        for i in range(n):
            total.append(start[i])
        return total
    for i in start:
        total.append(i)

    while len(total)!=n:
        i = len(total)
        total.append(sum(total[-3:]))
    return total

def iq_test(numbers):
    arr = [int(i) for i in numbers.split(' ')]
    listFilter =list(filter(lambda x: x%2==0,arr))
    listFilter2 =list(filter(lambda x: x%2==1,arr))
    if(len(listFilter) == 1):
        return arr.index(listFilter[0])+1
    if(len(listFilter2)==1):
        return arr.index(listFilter2[0])+1

def series_sum(n):
    digit = 4
    total = 1.0
    if(n==1):
        return 1.0
    for i in range(n-1):
        total += 1/digit
        digit +=3
    return str("%.2f"%(total))

def solution(number):
    sum = 0
    for i in range(1,number):
        if(i%3 == 0 or i%5 == 0):
            sum+=i
            continue
    return sum

def validBraces(string):
    listOpen = []
    for i in string:
        if(i=='(' or i=='{' or i=='['):
            listOpen.append(i)
        else:
            if(listOpen.__len__()!=0):
                if(equalBraces(listOpen[len(listOpen)-1],i)==True):
                    listOpen.pop()
    if(len(listOpen)==0):
        return True
    else:
        return False
def equalBraces(brace1,brace2):
    if(brace1=='(' and brace2==')'):
        return True
    if(brace1=='[' and brace2==']'):
        return True
    if(brace1=='{' and brace2=='}'):
        return True
    return False
def validBraces2(string):
    while '[]' in string or '{}' in string or '()' in string:
        string =str(string).replace('()','')
        string =str(string).replace('[]','')
        string =str(string).replace('{}','')
    return string==''

def errorTask():
    a=[10,30,60]
    b = [100,10,2]
    n = 3
    fulVer = 0
    for i in range(n):
        fulVer += a[i]*b[i]
    print(fulVer)
    for i in range(n):
        print((a[i]*b[i])/fulVer)

def autoDop(string):
    sett = set()
    list = str(string).split(" ")
    for i in list:
        sett.add(i)
    print(sett)
    for i in list:
        if i in set:
            pass

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    arr =[]
    summ = 0
    for i in range(a,b+1):

        for k in range(len(valuePart(i))):
            temp = valuePart(i)
            summ += temp[k]**(k+1)
            if summ == i:
                arr.append(i)
        summ=0

    return arr
def digitCount(n):
    count = 0
    while n != 0:
        n//=10
        count+=1
    return count
def valuePart(n):
    arr =[]
    while n != 0:
        ost = n % 10
        n = n//10
        arr.append(ost)
    arr.reverse()
    return arr


def find_uniq(arr):
    sett = set(arr)
    for i in sett:
        if arr.count(i) == 1:
            return i

def spin_words(sentence):
    arr = sentence.split(' ')
    for i in range(len(arr)):
        if len(arr[i]) >= 5:
            arr[i] = arr[i][::-1]
    sentence = " ".join(arr)
    return sentence

def comp(array1, array2):
    if(array1 is None or array2 is None):
        return False
    for i in array1:

        if not(i**2 in array2):
            return False
        else:
            array2.remove(i**2)
    return True

def first_non_repeating_letter(string):
    if string != '':
        for i in string:
            if i != " ":
                if(string.lower().count(i.lower())==1):
                    return i
    return ''

def tower_builder(n):
    arr = []
    for i in range(n):
        string = ' '*i + '*'*(2*(n-i)-1) + ' '*i
        arr.append(string)
        print(string)
    arr.reverse()
    return arr

def expanded_form(num):
    string = str(num)
    arr=[]
    for i in range(len(string)):
        if(string[i]!='0'): arr.append(string[i] + "0"*(len(string)-i-1))
    return " + ".join(arr)

def make_readable(seconds):
    hours = seconds // 3600
    mins =   seconds // 60 -(hours*60)
    seconds = seconds - hours*3600 - mins*60
    if(hours < 10): hours = '0' + str(hours)
    if(mins < 10): mins = '0' + str(mins)
    if(seconds < 10): seconds = '0' + str(seconds)
    return str(hours) + ":" + str(mins) + ":" + str(seconds)
def make_readable2(seconds):
    return '{:02}:{:02}:{:02}'.format(seconds//3600, seconds//60%60, seconds%60)

print(make_readable2(36536))