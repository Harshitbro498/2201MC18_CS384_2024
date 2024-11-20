def main():
  Int =set(map(int,input().split()))
  Sym =set(['@','!','#'])
  file= open("Passwords.txt","r")
  file.seek(0)
  Passwords= file.readlines()
  print("Passwords are : ", Passwords)
  for x in Passwords :
    # x=x.strip()1
    x=x.replace("\n","")
    # x=x[:-2]
    if len(x)<8 :
        print("Its too Short")
    a,A,d,s=[],[],[],[]
    f=True
    for i in x:
      if i.isupper() : 
        A.append(i)
      elif i.islower() : 
        a.append(i)
      elif i.isdigit() :
        d.append(int(i))
        if int(i) not in Int : 
          f=False
          print(f"Can't use Number {i}")
      else :
        s.append(i)
        if i not in Sym :
          f=False
          print(f"Can't use Symbol {i}")
    if len(a)==0:
      print("add Lowercase")
      f=False
    if len(A)==0:
      print("add Uppercase")
      f=False
    if len(d)==0:
      print("add Numbers")
      f=False
    if len(s)==0:
      print("add Symbols")
      f=False
    if f:
      print(f"Your password {x} is valid ")
    else :
      print(f"No your password {x} is Invalid")
    x= file.readline()  
  file.close()
if __name__== "__main__": main()
