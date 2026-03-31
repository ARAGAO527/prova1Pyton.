#--O Game Over--#
resposta = input("Deseja continuar jogando? (sim/nao): ").lower()

while resposta == "sim":
    print("Você ainda está no jogo! 🎮")
    resposta = input("Deseja continuar jogando? (sim/nao): ").lower()

print("Game Over! 💀")