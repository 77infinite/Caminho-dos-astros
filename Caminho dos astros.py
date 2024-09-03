import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkinter import font

# Funções para obter os dias astecas
def get_tonalpohualli_day(index):
    tonalpohualli_days = [
        "1 Acatl", "2 Calli", "3 Tochtli", "4 Acatl", "5 Calli", "6 Tochtli", "7 Acatl", "8 Calli", "9 Tochtli",
        "10 Acatl", "11 Calli", "12 Tochtli", "13 Acatl", "1 Calli", "2 Tochtli", "3 Acatl", "4 Calli", "5 Tochtli",
        "6 Acatl", "7 Calli", "8 Tochtli", "9 Acatl", "10 Calli", "11 Tochtli", "12 Acatl", "13 Calli", "1 Tochtli",
        "2 Acatl", "3 Calli", "4 Tochtli", "5 Acatl", "6 Calli", "7 Tochtli", "8 Acatl", "9 Calli", "10 Tochtli",
        "11 Acatl", "12 Calli", "13 Tochtli", "1 Acatl", "2 Calli", "3 Tochtli", "4 Acatl", "5 Calli", "6 Tochtli",
        "7 Acatl", "8 Calli", "9 Tochtli", "10 Acatl", "11 Calli", "12 Tochtli", "13 Acatl", "1 Calli", "2 Tochtli",
        "3 Acatl", "4 Calli", "5 Tochtli", "6 Acatl", "7 Calli", "8 Tochtli", "9 Acatl", "10 Calli", "11 Tochtli",
        "12 Acatl", "13 Calli", "1 Tochtli", "2 Acatl", "3 Calli", "4 Tochtli", "5 Acatl", "6 Calli", "7 Tochtli",
        "8 Acatl", "9 Calli", "10 Tochtli", "11 Acatl", "12 Calli", "13 Tochtli", "1 Acatl", "2 Calli", "3 Tochtli",
        "4 Acatl", "5 Calli", "6 Tochtli", "7 Acatl", "8 Calli", "9 Tochtli", "10 Acatl", "11 Calli", "12 Tochtli",
        "13 Acatl", "1 Calli", "2 Tochtli", "3 Acatl", "4 Calli", "5 Tochtli", "6 Acatl", "7 Calli", "8 Tochtli",
        "9 Acatl", "10 Calli", "11 Tochtli", "12 Acatl", "13 Calli", "1 Tochtli", "2 Acatl", "3 Calli", "4 Tochtli",
        "5 Acatl", "6 Calli", "7 Tochtli", "8 Acatl", "9 Calli", "10 Tochtli", "11 Acatl", "12 Calli", "13 Tochtli"
    ]
    return tonalpohualli_days[index % len(tonalpohualli_days)]

def get_xiuhpohualli_day(index):
    xiuhpohualli_days = [
        "1 Acatl", "2 Acatl", "3 Acatl", "4 Acatl", "5 Acatl", "6 Acatl", "7 Acatl", "8 Acatl", "9 Acatl", "10 Acatl",
        "11 Acatl", "12 Acatl", "13 Acatl", "1 Calli", "2 Calli", "3 Calli", "4 Calli", "5 Calli", "6 Calli", "7 Calli",
        "8 Calli", "9 Calli", "10 Calli", "11 Calli", "12 Calli", "13 Calli", "1 Tochtli", "2 Tochtli", "3 Tochtli",
        "4 Tochtli", "5 Tochtli", "6 Tochtli", "7 Tochtli", "8 Tochtli", "9 Tochtli", "10 Tochtli", "11 Tochtli",
        "12 Tochtli", "13 Tochtli", "1 Acatl", "2 Acatl", "3 Acatl", "4 Acatl", "5 Acatl", "6 Acatl", "7 Acatl",
        "8 Acatl", "9 Acatl", "10 Acatl", "11 Acatl", "12 Acatl", "13 Acatl", "1 Calli", "2 Calli", "3 Calli",
        "4 Calli", "5 Calli", "6 Calli", "7 Calli", "8 Calli", "9 Calli", "10 Calli", "11 Calli", "12 Calli",
        "13 Calli", "1 Tochtli", "2 Tochtli", "3 Tochtli", "4 Tochtli", "5 Tochtli", "6 Tochtli", "7 Tochtli",
        "8 Tochtli", "9 Tochtli", "10 Tochtli", "11 Tochtli", "12 Tochtli", "13 Tochtli"
    ]
    return xiuhpohualli_days[index % len(xiuhpohualli_days)]

def gregorian_to_aztec(date):
    # Definição do ciclo Tonalpohualli (260 dias) e Xiuhpohualli (365 dias)
    tonalpohualli_cycle = 260
    xiuhpohualli_cycle = 365

    # Data base para o calendário asteca (1 de janeiro de 1500 na data gregoriana)
    base_date = datetime(1500, 1, 1)
    
    # Calcula a diferença de dias entre a data base e a data fornecida
    delta_days = (date - base_date).days

    # Determina o dia no ciclo Tonalpohualli e Xiuhpohualli
    tonalpohualli_day_index = delta_days % tonalpohualli_cycle
    xiuhpohualli_day_index = delta_days % xiuhpohualli_cycle

    return get_tonalpohualli_day(tonalpohualli_day_index), get_xiuhpohualli_day(xiuhpohualli_day_index)

def calculate_date():
    try:
        # Obtém a data do campo de entrada
        user_input = date_entry.get()
        user_date = datetime.strptime(user_input, "%d-%m-%Y")
        
        # Converte a data fornecida para o calendário asteca
        tonalpohualli_day, xiuhpohualli_day = gregorian_to_aztec(user_date)
        
        # Obtém o dia da semana, dia e mês
        day_of_week = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"][user_date.weekday()]
        day = user_date.day
        month = user_date.strftime("%B")

        # Atualiza o texto do resultado
        result_label.config(text=f"Data fornecida: {day_of_week}, {day} de {month}\nDia no Tonalpohualli: {tonalpohualli_day}\nDia no Xiuhpohualli: {xiuhpohualli_day}", font=fonte )
    
    except ValueError:
        # Exibe uma mensagem de erro se a data não estiver no formato correto
        messagebox.showerror("Erro", "Formato de data inválido. Certifique-se de usar o formato dia-mês-ano (ex: 15-08-2024).", font=fonte)

# Cria a janela principal
root = tk.Tk()
root.title("Calendário Asteca")
root.geometry("1000x480")
fonte = font.Font(family="Helvetica", size=30)


# Cria e posiciona os widgets
tk.Label(root, text="Digite a data no formato dia-mês-ano (ex: 15-08-2024):", font=fonte).pack(padx=10, pady=5)
date_entry = tk.Entry(root, font=fonte, width=20)
date_entry.pack(padx=10, pady=40)

tk.Button(root, text="Calcular", command=calculate_date, font=fonte,).pack(padx=10, pady=5)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack(padx=10, pady=5)

# Executa o loop principal da interface gráfica
root.mainloop()