import re
p = re.compile(r'(Peter) (\w+)')
p1 = re.compile(r'(Peter \w+)')
text = "Peter Hansen was meeting up with Jacob Fransen for a quick lunch, but first he had to go by Peter Beier to pick up some chokolate for his wife. Meanwhile Pastor Peter Jensen was going to church to give his sermon for the same 3 people in his parish. Those were Peter Kold and Henrik Halberg plus a third person who had recently moved here from Norway called Peter Harold"
m = p.search(text)
m1 = p1.findall(text)

print(m1)

address_entry = """

A Henning Gamborg Møller
Klostergade 28
6760 Ribe
61 69 03 76

A K Møller
Bregnerødvej 75, st. 0002
3460 Birkerød
75 50 75 14

A Møller
Violvej 3
Ø. Bjerregrav
8920 Randers NV
86 45 44 36

A Møller
Hyrdevej 16A
7000 Fredericia
76 42 00 81

A Møller
Brammersgade 45
8000 Aarhus C
86 13 22 99

A Møller
Dalstræde 11
Heltborg
7760 Hurup Thy
97 95 20 01
"""

# p_names = re.compile(r'(\s{2}) (\w+)') // not working
# p_names = re.compile(r'[\n{2}] \w+') // not working
# p_names = re.compile(r'\n\n((\w+ ) +\w+)\n') // not working
p_names = re.compile(r'\n\n(.+)')
p_tele = re.compile(r'\d{2} \d{2} \d{2} \d{2}')
p_zip = re.compile(r'\d{4}.+')
# p_street = re.compile(r'.+\D+ \w+.+') // not working

m_address = p_names.findall(address_entry)
m_tele = p_tele.findall(address_entry)
m_zip = p_zip.findall(address_entry)
# m_street = p_street.findall(address_entry)

print('-add')
print(m_address)
print('-tele')
print(m_tele)
print('-zip')
print(m_zip)
# print('-street')
# print(m_street)