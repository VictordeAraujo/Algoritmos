#NUMERO PRIMO E PAR
#n=int(input( ))
#soma=0
#for x in range(1,n+1):
#  if n%x==0:
#    soma+=1
#  if n%2==0:
#    soma+=1
#if soma<=3:
#  print("Numero primo")
#if soma>3:
#  print("Numero par")

#TRIANGULO COM NUMEROS
#n=3
#a=1
#for x in range(1,n+1):
#  for y in range(x,n+1):
#    print(" ",end=" ")
#  for i in range(1,x+1):
#    print("%d"%i,end=" ")
#  for j in range(1,x):
#    print("%d"%a,end=" ")
#    a+=1
#    if a==3:
#      a=1
#  print(" ")

#NUMEROS
#n=int(input( ))
#for x in range(1,n+1):
#  for y in range(x):
#    print("%d"%x, end=" ")
#  print("")

#FIBONACCI FOR:
#n=int(input( ))
#y1=0
#y2=1
#for x in range(1,n):
#  print("%d %d"%(y1,y2),end=(" "))
#  y1=y1+y2
#  y2=y2+y1
#print(" ")

#n=int(input("Fatorial:"))
#y=1
#for x in range(2,n+1):
#  y=y*x
#print("Resultado:%d" %y)

#NUMERO FORTE
#Número=int(input("Por favor digite qualquer número:"))
#Soma=0
#Temp=Número
#
#while(Temp>0):
#    Fatorial=1
#    Lembrete=Temp%10
#    for i in range(1,Lembrete+1):
#      Fatorial=Fatorial*i
#    print("Fatorial de %d=%d"%(Lembrete,Fatorial))
#    Soma=Soma+Fatorial
#    Temp=Temp//10
#print("Soma dos Fatorias é:%d"%Soma)
#if(Soma==Número):
#    print("%d é um número forte"%Número)
#else:
#    print("%d não é um número forte"%Número)
