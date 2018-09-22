# chating convert

name = ['Stanley', 'Mindy']
lines = []
def read_file(filename) :
    with open (filename, 'r', encoding = 'utf-8-sig') as f :
        for line in f :
            lines.append(line.strip() )
        return lines


def convert(lines) :
    
    person = None
    for line in lines :
        print(line)  
            

def write_file(filename, talks):
    with open(filename, 'w') as f :
        for line in lines :
            f.write(line + '\n')


def main() :  
    lines = read_file('[LINE]Stanley.txt')
    talklines = convert(lines)
    #write_file('output.txt', lines)

main()    
