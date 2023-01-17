import json

repetidos = [1,2,3,"1","2","3",3,4,5]
r = [1,"5",2,"3"]
d_str = '{"valor":125.3,"codigo":123}'

# Punto 1:Genere una lista con los valores no repetidos de la lista ‘repetidos’.
result_p1=new_list = [*set(map(int, repetidos))]
assert(result_p1==[1, 2, 3, 4, 5])

# Punto 2:Genere una lista con los valores en común entre la lista ‘r’ y ‘repetidos’
result_p2=[*set(map(int, repetidos)).intersection(map(int, r))]
assert(result_p2==[1, 2, 3, 5])

# Punto 3: Transforme ‘d_str’ en un diccionario.
result_p3 = json.loads(d_str)
assert(result_p3=={'valor': 125.3, 'codigo': 123})