x = input();

# Question 1 :-

x=int(x);
ans =0;
while x>0 :
    ans+=x%10;
    x/=10;
    x=int(x);
    if(x==0 and ans>=10) :
      x=ans;
      print(ans);
      ans=0;
print(ans);