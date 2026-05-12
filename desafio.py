from datetime import datetime


def Saudacao():
    agora = datetime.now()
    hora = agora.hour

    if 6 <= hora < 12:
        return "Bom dia!"
    elif 12 <= hora < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

print(f"Olá! {Saudacao()}")