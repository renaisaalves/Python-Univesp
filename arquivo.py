#Como manipular um arquivo usando Python. 
# 1 Abrir um arquivo para leitura ou escrita -> open('example.txt', 'r')
    # O primeiro argumento é o caminho para o arquivo ('example.text') e o segundo é o modo de abertura ('r')
# 2. Ler os dados do arquivo ou escrever nele
# 3. Fechar o arquivo

def readFile(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordList = content.split()
    print(wordList)
    return len(wordList), len(content)
n_words, n_chars = readFile('teste.txt')