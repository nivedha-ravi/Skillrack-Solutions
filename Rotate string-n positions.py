"""
INPUT:
cricket
2
OUTPUT:
etcrick
"""
string=input().strip()
n=int(input())
length=len(string)
print(string[length-n:length+1]+string[0:length-n])