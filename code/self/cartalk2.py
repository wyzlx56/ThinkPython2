def is_huiwen(word):
    if word==word[::-1]:
        return True
    return False

for i in range(1000000):
   word1=("%06d" %i)[-4:]
   word2=("%06d" %(i+1))[-5:]
   word3=("%06d" %(i+2))[1:5]
   word4=("%06d" %(i+3))
   #print(word1,word2,word3,word4)
   if is_huiwen(word1) and is_huiwen(word2) and is_huiwen(word3) and is_huiwen(word4):
       print("%06d" %i)
