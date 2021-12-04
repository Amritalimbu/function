mainStr="the quick brown fox jumped over the lazy dog.the dog slept over the veranda"
a=mainStr.replace('over','on')
print(a)


mainStr="the quick brown fox jumped over the lazy dog.the dog slept over the veranda"
subStr='over'
replacementStr='on'
a=mainStr.replace(subStr,replacementStr)
print(a)


mainStr="the quick brown fox jumped over the lazy dog.the dog slept over the veranda"
a=mainStr.replace(' ','-')
print(a)


mainStr="the quick brown fox jumped over the lazy dog.the dog slept over the veranda"
i=0
while i<len(mainStr):
    if 'over' in mainStr:
        mainStr=mainStr(replace.('over','on'))