'''
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.

'''
# note_muzicale = ['Do','RE','MI','FA','SOL','LA','SI','DO']
# print(note_muzicale)
# print(len(note_muzicale))
# note_muzicale1=slice(8,0,-1)
# invers=note_muzicale[note_muzicale1]
# print(invers)
# invers.reverse()
# print(invers)
'''
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găsește 2 variante să le unești într-o singură listă.

'''
# numere1=[3,1,0,2]
# numere2=[6,5,4]
# numere3 = numere1 + numere2
# print(numere3)
# numere2.extend(numere1)
# print(numere2)
'''
5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
● Lista este goală.
● Lista nu este goală.
# '''
# numere1=[3,1,0,2]
# numere2=[6,5,4]
# numere3 = numere1 + numere2
# print(numere3)
# numere2.extend(numere1)
# print(numere2)
# if numere3 == 0:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')

'''
6. Folosește o funcție care să șteargă lista de la exercițiul 3.
'''
# numere1=[3,1,0,2]
# numere2=[6,5,4]
# numere3 = numere1 + numere2
# print(numere3)
# numere2.extend(numere1)
# print(numere2)
# numere3.clear()
# print(numere3)

'''
7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.
'''
# numere1=[3,1,0,2]
# numere2=[6,5,4]
# numere3 = numere1 + numere2
# print(numere3)
# numere2.extend(numere1)
# print(numere2)
# numere3.clear()
# if numere3 == 0:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')

'''
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
'''
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(dict1.keys())

'''
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
'''
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(f'Ana a luat nota:{dict1["Ana"]}')
# print(f'Gigel a luat nota : {dict1["Gigel"]}')
# print(f'Dorel a luat nota : {dict1["Dorel"]}')

'''
10. Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare
'''
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(f'Ana a luat nota:{dict1["Ana"]}')
# print(f'Gigel a luat nota : {dict1["Gigel"]}')
# print(f'Dorel a luat nota : {dict1["Dorel"]}')
# dict1.update({'Dorel':6})
# print(f'Dupa contestatie Dorel a luat nota : {dict1["Dorel"]}')

'''
11. Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi
'''
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(f'Ana a luat nota:{dict1["Ana"]}')
# print(f'Gigel a luat nota : {dict1["Gigel"]}')
# print(f'Dorel a luat nota : {dict1["Dorel"]}')
# dict1.update({'Dorel':6})
# print(f'Dupa contestatie Dorel a luat nota : {dict1["Dorel"]}')
# dict1.pop("Gigel")
# print(dict1)
# dict1.update({"Ionica":9})
# print(dict1)

'''
12.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Adaugă în zilele_sapt ‘luni’
● Afișeaza zile_sapt
'''
# zile_sapt = { 'luni','marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# zile_sapt.add('Luni')
# print(zile_sapt)

'''
13.Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din săptămânii.
● Weekend nu este un subset al zilelor din săptămânii.
'''
# zile_sapt = { 'luni','marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
#
# if set(weekend).issubset(zile_sapt):
#     print('Wekeend este un subset al zilelor saptamanii.')
# else:
#     print('Wekeend nu este un subset')

'''
14. Afișează diferențele dintre aceste 2 seturi.
'''
# zile_sapt = { 'luni','marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# print(zile_sapt.difference(weekend))

'''
15. Afișază intersecția elementelor din aceste 2 seturi.
'''
# zile_sapt = { 'luni','marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# print(zile_sapt.intersection(weekend))

'''
1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:
● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișaza a intra x, a ieșit y, mai ai z schimbări
Dacă jucătorul nu e în teren:
- Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
Testează codul cu diferite valori

'''
jucatori = [1,2,3,4,5]
Schimbari_efectuate =5
Schimbari_max=3
if Schimbari_efectuate >=Schimbari_max :
    print(f'')
elif:
     y=jucatori.extend([Schimbari_efectuate])
     x=jucatori.pop(2)
     z=Schimbari_max-1
     print(f'A iesit jucatorul {x},a intrat jucatorul {Schimbari_efectuate} ,si mai aveti {z} schimbari la dispozitie ')
