def Anagram_Checker(s1,s2):
  if len(s1)!=len(s2):
    return False
  d={}
  for i in s1:
    if i not in d:
      d[i]=1
    else:
      d[i]+=1

  for i in s2:
    if i in d:
      d[i]-=1
      if d[i]<0:
        return False
    else:
        return False

  for v in d.values():
    if v!=0:
      return False
  return True


s1="anagram"
s2="nagaram"
ans=Anagram_Checker(s1,s2)
print(ans)
