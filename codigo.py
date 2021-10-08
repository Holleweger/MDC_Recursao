def calculaMDC(v1,v2):
  global mdc
  mdc = v1
  if v1 % mdc != 0 or v2 % mdc != 0:
    mdc = calculaMDC(v1 - 1,v2)
  else:
    return(0)
    

n = int(input("Digite o primeiro valor : "))
m = int(input("Digite o segundo valor : "))
o = int(input("Digite o terceiro valor : "))
mdc = 0

#Comece sempre pelo menor
calculaMDC(n,m)
calculaMDC(mdc,o)
print("Seu MDC é : ",mdc)

