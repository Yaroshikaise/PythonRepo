#1)	Explicați ce a fost realizat in urmatorul exemplu:
#Se definește o funcție lambda numită greet_user, care primește un parametru name și afișează un mesaj de salut:
greet_user = lambda name : print('Hello My Dear, ', name)#Este o funcție anonimă (lambda) care execută direct print() fără a folosi return.
#Se citește un nume de la utilizator cu input():
user_name = input("What is your name? ")
#Se apelează funcția lambda, folosind numele introdus de utilizator:
greet_user(user_name)
#Programul va afisa textul: Hello My Dear, (numele introdus)

#2
lista = [(3, 11), (1, 7), (7, 8), (16, 88), (23, 15), (5, 3), (8, 42)]
lista_sortata = sorted(lista, key=lambda x: x[1])
print(lista_sortata)



#3
este_par = lambda x: x % 2 == 0
print(este_par(4)) 
print(este_par(7)) 


#4

def salut():
    print("Salut, Alexandru!")

   


def salut_persoana(nume):
    print("Salut, " + nume + "!")
    



def salut_persoana_default(nume="Alexandru"):
    print("Bună ziua, " + nume + "!")




def aduna(a, b):
    return a + b



def afiseaza_suma(a, b):
    print("Suma este:", a+b)


    #5
def calculeaza_suma(a, b):
    return a + b

def afiseaza_suma(suma):
    print("Rezultatul calculat este:", suma)

rez = calculeaza_suma(10, 20)
afiseaza_suma(rez)
