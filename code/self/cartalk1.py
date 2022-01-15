def is_three_double(word):
    if len(word) < 6:
        return False
    i = 0
    while i < len(word)-1:
        if word[i] != word[i+1]:
            i = i+1
        else:
            if len(word[i+2:])>=4 and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
                return True
            else:
                i=i+1
    return False

f=open("words.txt")
i=1
for word in f:
    if is_three_double(word.strip()):
        print(word.strip())
