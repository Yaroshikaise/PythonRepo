# a) Lista
lista = [10, 20, 30, 40, 50]
print("Prima valoare:", lista[0])
print("A treia valoare:", lista[2])

# Înlocuire valoare
lista[1] = 25
print("Lista după înlocuire:", lista)

# Extracție (tăietură)
sub_lista = lista[1:4]
print("Sub-lista extrasă:", sub_lista)

# Aplicarea unei metode, a două funcții și a trei operatori
lista.append(60)  # Metodă
print("Lista după append:", lista)
lungime = len(lista)  # Funcție
print("Lungimea listei:", lungime)
maxim = max(lista)  # Funcție
print("Valoarea maximă:", maxim)
print("30 este în listă?", 30 in lista)  # Operator "in"
print("10 nu este în listă?", 10 not in lista)  # Operator "not in"
print("Suma elementelor listei:", sum(lista))  # Operator "+" aplicat pe lista

# b) Tuplu
tuplu = (100, 200, 300, 400)
print("Tipul de date:", type(tuplu))
print("Prima valoare:", tuplu[0])
print("Ultima valoare:", tuplu[-1])
sub_tuplu = tuplu[1:3]
print("Sub-tuplu extras:", sub_tuplu)

# Aplicarea a 3 funcții
print("Lungimea tuplului:", len(tuplu))
print("Valoarea minimă din tuplu:", min(tuplu))
print("Valoarea maximă din tuplu:", max(tuplu))

# c) Set
multime = {1, 2, 2, 3, 4, 4, 5}
print("Mulțimea:", multime)  # Elimină duplicatele
multime.add(6)  # Metodă
print("Mulțimea după adăugare:", multime)
print("Lungimea mulțimii:", len(multime))  # Funcție

# d) Dicționar
dict_text = {"nume": "Alice", "oraș": "București"}
dict_numeric = {1: "unu", 2: "doi"}
print("Elemente din dicționarul text:", dict_text["nume"], dict_text["oraș"])
print("Elemente din dicționarul numeric:", dict_numeric[1], dict_numeric[2])

# Aplicarea a 2 metode și 2 funcții
print("Cheile dicționarului text:", dict_text.keys())  # Metodă
print("Valorile dicționarului numeric:", dict_numeric.values())  # Metodă
print("Dimensiunea dicționarului text:", len(dict_text))  # Funcție
print("Dimensiunea dicționarului numeric:", len(dict_numeric))  # Funcție

# e) Conversie între tipuri
tuple_to_list = list(tuplu)
print("Tuplu convertit în listă:", tuple_to_list)
list_to_set = set(lista)
print("Listă convertită în set:", list_to_set)
set_to_tuple = tuple(multime)
print("Set convertit în tuplu:", set_to_tuple)

# Sarcina 2
a) # Crearea listelor
produse = ["Mere", "Pere", "Banane"]
preturi = [5, 7, 3]
info = "{} costă {} lei, {} costă {} lei, {} costă {} lei".format(produse[0], preturi[0], produse[1], preturi[1], produse[2], preturi[2])
print(info)

# b) Introducere vârstă
varsta = int(input("Introduceți vârsta: "))
viitor = varsta + 5
print("În 5 ani veți avea " + str(viitor) + " ani.")

# c) Operator "in" și "not in"
nume_lista = ["Ana", "Maria", "Ion"]
print("Maria este în listă?", "Maria" in nume_lista)
print("George nu este în listă?", "George" not in nume_lista)
