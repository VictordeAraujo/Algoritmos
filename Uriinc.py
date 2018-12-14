#Uri exercicio 1
#A=int(input())
#B=int(input())
#X=0
#X=A+B
#print("X =",X)

#Uri exercicio 2
#n=3.14159
#raio=float(input())
#area=0
#area=n*raio**2
#print("A=%.4f"%area)

#Uri exercicio 3
#A=int(input())
#B=int(input())
#SOMA=0
#SOMA=A+B
#print("SOMA =",SOMA)

#Uri exercicio 4
#a=int(input())
#b=int(input())
#PROD=0
#PROD=a*b
#print("PROD =",PROD)

#Uri exercicio 5
#a=float(input())
#b=float(input())
#A=3.5
#B=7.5
#media=((a*A)+(b*B))/11
#print("MEDIA = %.5f"%media)

#Uri exercicio 6
#A=float(input())
#B=float(input())
#C=float(input())
#media=((A*2)+(B*3)+(C*5))/10
#print("MEDIA = %.1f"%media)

#Uri exercicio 7
#A=int(input())
#B=int(input())
#C=int(input())
#D=int(input())
#diferenca=(A*B-C*D)
#print("DIFERENCA =",diferenca)

#Uri exercicio 8
#numF=int(input())
#horT=int(input())
#valH=float(input())
#salario=horT*valH
#print("NUMBER =",numF)
#print("SALARY = U$ %.2f"%salario)

#Uri exercicio 9
#name=input()
#salario=float(input())
#vendasD=float(input())
#total=vendasD*0.15+salario
#print("TOTAL = R$ %.2f"%total)

#Uri exercicio 10
#cod1,num1,valU1=input().split()
#cod2,num2,valU2=input().split()
#cod1=int(cod1)
#num1=int(num1)
#valU1=float(valU1)
#cod2=int(cod1)
#num2=int(num2)
#valU2=float(valU2)
#valP=(num1*valU1)+(num2*valU2)
#print("VALOR A PAGAR: R$ %.2f"%valP)

#Uri exercicio 11
#r=int(input())
#pi=3.14159
#volume=(4/3)*pi*r**3
#print("VOLUME = %.3f"%volume)

#Uri exercicio 12
#A,B,C=input().split()
#a=float(A); b=float(B); c=float(C);
#pi=3.14159
#tri=a*c/2
#cir=pi*c**2
#trap=(a+b)*c/2
#quad=b*b
#retan=a*b
#print("TRIANGULO: %.3f"%tri)
#print("CIRCULO: %.3f"%cir)
#print("TRAPEZIO: %.3f"%trap)
#print("QUADRADO: %.3f"%quad)
#print("RETANGULO: %.3f"%retan)

#Uri exercicio 13
#A,B,C=input().split()
#a=int(A); b=int(B); c=int(C);
#maiorAB=(a+b+abs(a-b))/2
#maiorABC=(maiorAB+c+abs(maiorAB-c))/2
#print("%d eh o maior"%maiorABC)

#Uri exercicio 14
#X=int(input())
#Y=float(input())
#consumo=X/Y
#print("%.3f km/l"%consumo)

#Uri exercicio 15
#import math
#p1,p2=input().split()
#x1=float(p1); x2=float(p2);
#p11,p22=input().split()
#y1=float(p11); y2=float(p22)
#Distancia=math.sqrt((x1-y1)**2+(x2-y2)**2)
#print("%.4f"%Distancia)

#Uri exercicio 16
#v=int(input())
#t=v*2
#print("%d minutos"%t)

#Uri exercicio 17
#tempo=int(input( ))
#vm=int(input( ))
#c=12
#q=(tempo*vm)/c
#print("%.3f"%q)

#Uri exercicio 18
#n= int(input( ))
#for x in range(1,100):
#  print(n)
#  a=n//100
#  n=n%100
#  print("%d nota(s) de R$ 100,00" %a)
#  b=n//50
#  n=n%50
#  print("%d nota(s) de R$ 50,00" %b)
#  c=n//20
#  n=n%20
#  print("%d nota(s) de R$ 20,00" %c)
#  d=n//10
#  n=n%10
#  print("%d nota(s) de R$ 10,00" %d)
#  e=n//5
#  n=n%5
#  print("%d nota(s) de R$ 5,00" %e)
#  f=n//2
#  n=n%2
#  print("%d nota(s) de R$ 2,00" %f)
#  g=n//1
#  n=n%1
#  print("%d nota(s) de R$ 1,00" %g)
#  break;

#Uri exercicio 19
#t=int(input( ))
#hs=(t//60//60)
#ms=((t//60)-(hs*60))
#ss=(t-((hs*60*60)+(ms*60)))
#print("%d:%d:%d"%(hs,ms,ss))

#Uri exerciccio 20
#dias=int(input( ))
#ano=dias//365
#mes=(dias%365)//30
#dia=(dias%365%30)
#print("%d ano(s)"%ano)
#print("%d mes(es)"%mes)
#print("%d dia(s)"%dia)

#Uri exercicio 1178
#Y=float(input( ))
#for i in range(0,100):
#    print("N[%d] = %.4f" %(i,Y))
#    Y/= 2.0

#Uri exercicio 1387
#L=1
#R=1
#while(L!=0)and(R!=0):
#  sl=0
#  sr=0
#  L,R=map(int,input().split())
#  if L!=0 and R!=0:
#    sl+=L
#    sr+=R
#    print(sl+sr)

#Uri exercicio 1180
#N=int(input())
#X=list(map(int,input().split()))
#posicao=0
#menor=X[0]
#count=0
#for v in X:
#  if(v<menor):
#    menor=v
#    posicao=count
#  count+=1
#print("Menor valor: %d"%menor)
#print("Posicao: %d"%posicao)

#Uri exercicio 2670
#A1=int(input( ))
#A2=int(input( ))
#A3=int(input( ))
#Ai1=(A2*2+A3*4)
#Ai2=(A1*2+A3*2)
#Ai3=(A1*4+A2*2)
#if Ai1<=Ai2 and Ai1<=Ai3:
#  print(Ai1)
#elif Ai2<=Ai3:
#  print(Ai2)
#else:
#  print(Ai3)
