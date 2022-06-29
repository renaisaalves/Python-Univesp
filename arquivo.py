#Como manipular um arquivo usando Python. 
# 1 Abrir um arquivo para leitura ou escrita -> open('example.txt', 'r')
    # O primeiro argumento é o caminho para o arquivo ('example.text') e o segundo é o modo de abertura ('r')
# 2. Ler os dados do arquivo ou escrever nele
# 3. Fechar o arquivo

def readFile(filename):
    infile = open(filename, 'r') #abre o arquivo no modo leitura
    content = infile.read() #lê os dados do arquivo em modo leitura
    infile.close() #fecha o arquivo 
    wordList = content.split() #split é uma função que vai separar cada palavra do arquivo
    print(wordList) #exibe todas as palavras do texto
    return len(wordList), len(content) #o retorno será a quantidade de palavras e caracteres
n_words, n_chars = readFile('testo.txt')
print(n_words, n_chars) #vai exibir na tela a quantidade de palavras e a quantidade de caracteres.