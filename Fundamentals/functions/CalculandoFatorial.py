# Escreva uma função que calcule o fatorial de um número
# recebido como parâmetro e retorne o seu resultado.
# - Faça uma validação dos dados por meio de uma outra função,
# permitindo que somente valores positivos sejam aceitos
# - Crie o help da sua função 

def validateInt(question, min, max):
   x = int(input(question))
   while((x < min) or (x > max)):
        x = int(input(question))
   return x     
    

def  calcFactorial(n):
   """
   Calcula a fatorial
   :param n:
   :return:
   """
   fat = 1
   if n == 0 or n == 1:
        return fat
   for i in range(1, n+1, 1):
        fat *= i #fat = fat * i
   return fat
        
x = validateInt("Fatorial De: ", 0, 99999 )         
print("{}! = {}".format(x,calcFactorial(x)))


