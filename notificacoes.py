def enviar_notificacao(pet):
    if not pet.get("nome") or not pet.get("tipo"):
        print("Erro: Pet inválido. Nome e tipo são obrigatórios.")
        return
    print(f"Novo pet disponível para adoção: {pet['nome']} ({pet['tipo']})")

# Simulação de notificação
novo_pet = {"nome": "Sofia", "tipo": "Cachorro"}
enviar_notificacao(novo_pet)