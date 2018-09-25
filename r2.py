
name = ['Stanley', 'Mindy']
lines = []
def read_file(filename) :
    with open (filename, 'r', encoding = 'utf-8-sig') as f :
        for line in f :
            lines.append(line.strip())
        return lines

def convert(lines) :
    new = []
    name = None
    stanley_word_count = 0
    stanley_stic_count = 0
    stanley_photo_count = 0
    mindy_word_count = 0
    mindy_stic_count = 0
    mindy_photo_count = 0

    for line in lines :
        s = line.split(' ')
        print(s)
        time = s[0]
        name = s[1]
        #print(s)
       
        if name == 'Stanley' :
            if s[2] == '[貼圖]':
                stanley_stic_count += 1
            elif s[2] == '[照片]':
                stanley_photo_count += 1
            else :
                for m in s[2:]:
                    stanley_word_count += len(m)
        elif name == 'Mindy' :
            if s[2] == '[貼圖]':
                mindy_stic_count += 1
            elif s[2] == '[照片]':
                mindy_photo_count += 1
            else :
                for m in s[2:]:
                    mindy_word_count += len(m)
    
    print('Stanley 共說了 ', stanley_word_count, '個字')
    print('Stanley 共傳了 ', stanley_stic_count, '個貼圖')
    print('Stanley 共傳了 ', stanley_photo_count, '張照片')
    print('Mindy 共說了 ', mindy_word_count, '個字')
    print('Mindy 共傳了 ', mindy_stic_count, '個貼圖')
    print('Mindy 共傳了 ', mindy_photo_count, '張照片')
            


def write_file(filename, lines):
    with open(filename, 'w') as f :
        for line in liness :
            f.write(line + '\n')

def main() :  
    lines = read_file('line_stanley.txt')
    lines = convert(lines)
    #write_file('output.txt', lines)

main()     
