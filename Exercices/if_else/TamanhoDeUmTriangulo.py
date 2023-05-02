
# Faça um algoritmo que receba três valores, representando os lados de um triângulo
# fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique como:
# a) Equilátero (três lados iguais)
# b) Isosceles (dois lados iguais)
# c) Escaleno (três lados diferentes)


lado1 = float(input("Dimensão do lado 1 do triangulo: "))
lado2 = float(input("Dimensão do lado 2 do triangulo: "))
lado3 = float(input("Dimensão do lado 3 do triangulo: "))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado2 and lado2 + lado3 > lado2:
   if (lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
      print("Escaleno")
   elif (lado1 == lado2 and lado1 == lado3):
      print("Equilátero")
   else:
      print("Isosceles")
else:
   print("Os valores indicados nao favorecem para a formação de um triangulo")