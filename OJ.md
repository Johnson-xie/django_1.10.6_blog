## 递归调用时请在递归调用出也使用return  
```  
def removeDuplicates(S):
    res = []
    if len(S) <= 1:
        return S

    if S[0] != S[1]:
        res.append(S[0])

    for i in range(1, len(S) - 1):
        if S[i - 1] != S[i] and S[i] != S[i + 1]:
            res.append(S[i])
    if S[len(S) - 1] != S[len(S) - 2]:
        res.append(S[-1])
    new_str = ''.join(res)
    if S == new_str:
        return new_str
    else:
        return removeDuplicates(new_str)


ret = removeDuplicates("abbaca")
# ret = removeDuplicates("ac")
print(ret)
```  
