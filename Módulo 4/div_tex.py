text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

div_tex = text.split('. ')



print(div_tex)
#primera parte

palabras = ["average", "temperature", "distance"]

for div_tex in palabras:
    for palabra in palabras:
        if palabra in div_tex:
            print(div_tex)
            break

#segunda parte


for div_tex in palabras:
    for palabra in palabras:
        if palabra in div_tex:
            print(div_tex.replace('C.', 'Celsius'))
            break
