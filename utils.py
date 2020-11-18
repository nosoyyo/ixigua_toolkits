def clean(raw: str) -> list:
    material = raw.split('\n')
    material = [i for i in material if '次观看' in i]
    return [i.split('次观看')[0] for i in material]

def count(s:str) -> int:
    if '万' in s:
        s = s.replace('万','')
        result = int(float(s)*10000)
    else:
        result = int(s)
    return result

def summary(raw: str) -> str:
    material = clean(raw)
    material = [count(i) for i in material]
    s = sum(material)
    avr = int(s / len(material))
    print(f'总播放： {s} 平均播放： {avr}')