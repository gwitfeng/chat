# chat.py
name = ['Allen', 'Tom']
talks = []
def read_file(filename) :
    with open (filename, 'r', encoding = 'utf-8-sig') as f :
        for line in f :
            talks.append(line.strip() )
        return talks

def convert(talks) :
    say = []
    person = None
    for line in talks :
        if line == 'Allen' :
           person = 'Allen'
           continue
        elif line == 'Tom' :
            person = 'Tom'
            continue
        if person :    
            say.append(person + ':' + line)
    return say  

def write_file(filename, talks):
    with open(filename, 'w') as f :
        for line in talks :
            f.write(line + '\n')

def main() :  
    talks = read_file('input.txt')
    talks = convert(talks)
    write_file('output.txt', talks)

main()    
