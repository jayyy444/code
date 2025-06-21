text="Jaykumar Chaudhari"
pat="ari"
n=len(text)
m=len(pat)
flag=0

for i in range(n):
    if text[i:m+i]==pat:
        flag=1
        index=i
if flag==1:
    print(f"The {pat} is present in {text} at index {index}")
else:
    print(f"The {pat} is not present in {text}")
