def calculaMDC(v1,v2):
  mdc = v1
  if v1 % mdc != 0 or v2 % mdc != 0:
    mdc = calculaMDC(v1 - 1,v2)
  else:
    print("Seu MDC é : ", mdc)
    

n = int(input("Digite o primeiro valor : "))
m = int(input("Digite o segundo valor : "))

calculaMDC(n,m)
