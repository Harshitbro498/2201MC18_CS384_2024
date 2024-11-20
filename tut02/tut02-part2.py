x = input();
k="";
s=0;
for i in range (0,len(x)-1):
    if(x[i]==x[i+1]) :
      s=s+1;
    else :
      k+=x[i];
      k+=str(s+1);
      s=0;
k+=x[len(x)-1];
k+=str(s+1);

print(k);