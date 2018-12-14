#FIBONACCI
#n=int(input( ))
#ant=0
#prox=0
#while(prox<n):
#  print(prox,end=" ")
#  prox= prox+ant
#  ant=prox-ant
#  if(prox==0):
#    prox=prox+1
#print("")

#Figura1
#n=int(input( ))
#for x in range(n):
#  for y in range(x):
#    print("*", end=" ")
#  print("")
#for x in range(n,0,-1):
#  for y in range(x):
#    print("*", end=" ")
#  print("")

#Triangulo
#n=int(input( ))
#for x in range(1,n+1):
#  esp=n-x
#  print(" "*esp+"* "*x)

#Metades De Triangulos
#n=int(input( ))
#for x in range(n+1):
#  print("*"*x)
#for x in range(n+1):
#  esp=n-x
#  print(" "*esp+"*"*x)
#n=int(input( ))
#for esp in range(n):
#  x=n-esp
#  print(" "*esp+"*"*x)

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

#TABUADA FOR:
#x=int(input( ))
#n=1
#for i in range(1,11):
#  if x>0:
#    n=x*i
#    print("%d x %d = %d"% (i, x, n))

#Q coisa linda
#n=int(input( ))
#for x in range(1,n+1):
#  esp=n-x
#  print(" "*esp+"* "*x)
#n-=1
#for x in range(n,0,-1):
#  esp=n-x
#  print(" "*esp+" *"*x)

#Fatorial
#n=int(input("Fatorial:"))
#y=1
#for x in range(2,n+1):
#  y=y*x
#print("Resultado:%d" %y)
