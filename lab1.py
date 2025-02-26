name = input("Introdu numele: ")
print("Salut " + name)
#/////////////////////////
numar_intreg = 42
numar_real = 8.13
text_scurt = "abcdefg"
text_lung = """TextTextTextTextTextTextTextText
TextTextTextTextTextTextTextTextTextText
TextTextTextTextTextTextTextTextTextText
TextTextTextTextTextTextTextTextTextText"""

#//////////////////////////
print(type(numar_intreg))
print(type(text_scurt))

#////////////////////////////
print(len(text_lung))

#///////////////////////////////
print(text_scurt.upper())

#///////////////////////////////////
subsir = text_scurt[1:4]
print(subsir)

#///////////////////////////////////
print("Numarul ales este: {} si numarul real este: {:.2f}".format(numar_intreg, numar_real))
print(f"Salut {name}, ai ales numarul {numar_intreg}")
