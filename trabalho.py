import tkinter as tk
from tkinter import messagebox  # Importação reativada

# Estado local do jogo (gols e cartões)
estado_jogo = {
    "Time A": {"gols": 0, "amarelos": 0, "vermelhos": 0},
    "Time B": {"gols": 0, "amarelos": 0, "vermelhos": 0}
}

def atualizar_ui():
    label_placar.config(text=f"{estado_jogo['Time A']['gols']} x {estado_jogo['Time B']['gols']}")
    label_cartoes_a.config(text=f"🟨 {estado_jogo['Time A']['amarelos']}   |   🟥 {estado_jogo['Time A']['vermelhos']}")
    label_cartoes_b.config(text=f"🟨 {estado_jogo['Time B']['amarelos']}   |   🟥 {estado_jogo['Time B']['vermelhos']}")

def registrar_gol(time):
    estado_jogo[time]["gols"] += 1
    atualizar_ui()
    notificar_painel_digital(time, "Gol ⚽")
    messagebox.showinfo("GOOOOL! ⚽", f"Gol registrado para o {time}!\nPlacar atualizado na nuvem.")

def registrar_cartao(time, cor):
    if cor == "Amarelo":
        estado_jogo[time]["amarelos"] += 1
        icone = "🟨"
    elif cor == "Vermelho":
        estado_jogo[time]["vermelhos"] += 1
        icone = "🟥"
        
    atualizar_ui()
    notificar_painel_digital(time, f"Cartão {cor}")
    messagebox.showwarning(f"Cartão {cor} {icone}", f"Cartão {cor} registrado para o {time}!")

def notificar_painel_digital(time, evento):
    label_status.config(text=f"Último evento: {evento} para o {time} (Enviado para a Nuvem ☁️)", fg="#2ecc71")
    print(f"[POST /api/eventos] -> {evento} registrado para {time}.")

# 1. Configuração da Janela Principal
janela = tk.Tk()
janela.title("TorcidaNet - Painel do Mesário")
janela.geometry("500x420")
janela.configure(bg="#2c3e50")

# 2. Cabeçalho ao Vivo
tk.Label(
    janela, text="🔴 AO VIVO - TorcidaNet", 
    font=("Arial", 16, "bold"), fg="white", bg="#e74c3c", pady=10
).pack(fill=tk.X)

# 3. Área do Placar e Cartões
frame_placar = tk.Frame(janela, bg="#2c3e50")
frame_placar.pack(pady=15)

tk.Label(frame_placar, text="Time A (Casa)", font=("Arial", 12, "bold"), fg="white", bg="#2c3e50").grid(row=0, column=0, padx=20)
tk.Label(frame_placar, text="Time B (Fora)", font=("Arial", 12, "bold"), fg="white", bg="#2c3e50").grid(row=0, column=2, padx=20)

label_placar = tk.Label(frame_placar, text="0 x 0", font=("Arial", 45, "bold"), fg="#f1c40f", bg="#2c3e50")
label_placar.grid(row=1, column=0, columnspan=3, pady=5)

label_cartoes_a = tk.Label(frame_placar, text="🟨 0   |   🟥 0", font=("Arial", 11), fg="#bdc3c7", bg="#2c3e50")
label_cartoes_a.grid(row=2, column=0, pady=5)

label_cartoes_b = tk.Label(frame_placar, text="🟨 0   |   🟥 0", font=("Arial", 11), fg="#bdc3c7", bg="#2c3e50")
label_cartoes_b.grid(row=2, column=2, pady=5)

# 4. Controles de Eventos (Botões de Ação)
frame_controles = tk.Frame(janela, bg="#2c3e50")
frame_controles.pack(pady=10)

# Botões Time A
tk.Button(frame_controles, text="⚽ Gol Time A", bg="#27ae60", fg="white", font=("Arial", 11, "bold"), width=14, command=lambda: registrar_gol("Time A")).grid(row=0, column=0, padx=15, pady=5)
tk.Button(frame_controles, text="🟨 Amarelo A", bg="#f39c12", font=("Arial", 10, "bold"), width=16, command=lambda: registrar_cartao("Time A", "Amarelo")).grid(row=1, column=0, padx=15, pady=3)
tk.Button(frame_controles, text="🟥 Vermelho A", bg="#c0392b", fg="white", font=("Arial", 10, "bold"), width=16, command=lambda: registrar_cartao("Time A", "Vermelho")).grid(row=2, column=0, padx=15, pady=3)

# Botões Time B
tk.Button(frame_controles, text="⚽ Gol Time B", bg="#27ae60", fg="white", font=("Arial", 11, "bold"), width=14, command=lambda: registrar_gol("Time B")).grid(row=0, column=1, padx=15, pady=5)
tk.Button(frame_controles, text="🟨 Amarelo B", bg="#f39c12", font=("Arial", 10, "bold"), width=16, command=lambda: registrar_cartao("Time B", "Amarelo")).grid(row=1, column=1, padx=15, pady=3)
tk.Button(frame_controles, text="🟥 Vermelho B", bg="#c0392b", fg="white", font=("Arial", 10, "bold"), width=16, command=lambda: registrar_cartao("Time B", "Vermelho")).grid(row=2, column=1, padx=15, pady=3)

# 5. Status de Conexão
label_status = tk.Label(janela, text="Sistema pronto. Aguardando início do jogo.", font=("Arial", 10), fg="#95a5a6", bg="#2c3e50")
label_status.pack(side=tk.BOTTOM, pady=15)

janela.mainloop()