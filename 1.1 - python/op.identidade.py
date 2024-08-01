# is: compara se são o mesmo objeto;
# is not: compara se não são o mesmo objeto;

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
# True, porque b é uma referência para o mesmo objeto que a

print(a is c)
# False, porque c é um objeto diferente que contém os mesmos valores

x = 42
y = 42
z = 43

print(x is not y)
# False, porque x e y apontam para o mesmo objeto imutável 42

print(x is not z)
# True, porque x e z são objetos diferentes
