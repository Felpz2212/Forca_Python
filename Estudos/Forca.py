from random import choice

lista_palavras = ["banana", "pera", "uva", "abacaxi", "abacate", "amora", "goiaba", "mexerica", "maçã", "romã", "jabuticaba", "manga",
                  "limão", "laranja", "kiwi", "mamão", "malão", "melancia", "lichia", "damasco", "gabiroba", "pessego", "graviola", "maracuja",
                  "caju", "coco", "figo", "franboesa", "carambola", "groselha", "jaca", "morango", "pitaia", "nectarina", "açai", "acerola", "cacau", "caqui",
                  "cereja", "joãobolão", "pitanga", "siriguela", "tomate", "castanha", "nozes"]
palavra_secreta = choice(lista_palavras)
acertou = False
enforcou = False
erros = 0

print('*********************************')
print('Bem	vindo	ao	jogo	da	Forca!')
print('*********************************')
num = len(palavra_secreta)
letras_acertadas = []
i=0
for i in range(num):
    letras_acertadas.append("_")

print("****Dica: Fruta****'")
print(letras_acertadas)


while(not acertou and not enforcou):
    print("Jogando")
    chute = input("Qual a letra:")
    if(chute.lower() in palavra_secreta):
        if(chute.lower() == palavra_secreta.lower()):
            print("Você venceu!")
            print("A palavra secreta era: " + palavra_secreta)
            acertou = True
        posicao = 0
        for letra in palavra_secreta:
            if(chute.lower() == letra.lower()):
                letras_acertadas[posicao] = letra
            posicao = posicao + 1
        print(letras_acertadas)
        if(not "_" in letras_acertadas):
            print("Você venceu!")
            print("A palavra secreta era: " + palavra_secreta)
            acertou = True
    else:
        print("A palavra secreta não contém essa letra")
        erros += 1
        if(erros == 6):
            print("Enforcou, você Perdeu!")
            print("A palavra secreta era: " + palavra_secreta)
            enforcou = True

print(letras_acertadas)
print("fim do jogo")
