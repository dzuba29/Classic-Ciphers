alph='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
decode_string='ЙЧСЦЮЬЪЩЩМЛЫЪРЫФЭИЭЪЪНЕСЩФЛРЪЦМУЗОМСЮГЮЪЪЮЫЬМОФЮСЧСШНЗЧРСХЭЮОФЮСЧИЩЪЭЪУРМЮСЧИЭЪЪНЕСЩФЛ'
answer=[alph[((alph.find(string)+20)%len(alph))] for string in decode_string] # shift =20 
print(''.join(answer))

