#NUMERO PRIMO FOR:
#X=int(input( ))
#soma=0
#for a in range(1,X+1):
#  if X%a==0:
#    soma+=1
#if soma<=2:
#  print("%d eh primo"%X)
#else:
#  print("%d nao eh primo"%X)

x=int(input( ))
soma=0
y=1
while x>=y:
  if x%y==0 and x%x==0 and x%2==0 or x%3==0:
    soma+=1
  if soma==1:
    print("%d eh primo"%x)
  else:
    print("%d nao eh primo"%x)
  break;

#TABUADA FOR:
#x=int(input( ))
#n=1
#i=1
#for i in range(1,11):
#  if x>0 and x<20:
#    n=x*i
#    print("%d x %d = %d"% (i, x, n))

#TABUADA WHILE:
#x=int(input( ))
#n=1
#i=1
#while i<11:
#  if x>0:
#    n=x*i
#    print("%d x %d = %d"%(i, x, n))
#    i+=1
