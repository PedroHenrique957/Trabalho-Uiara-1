import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from PIL import Image, ImageTk


estado_jogo = {
    "Time A": {"gols": 0, "amarelos": 0, "vermelhos": 0},
    "Time B": {"gols": 0, "amarelos": 0, "vermelhos": 0},
}

diretorio_atual = Path(__file__).resolve().parent


def centralizar_janela(janela, largura, altura):
    x = (janela.winfo_screenwidth() - largura) // 2
    y = (janela.winfo_screenheight() - altura) // 2
    janela.geometry(f"{largura}x{altura}+{x}+{y}")


def atualizar_ui():
    label_placar.config(
        text=f"{estado_jogo['Time A']['gols']} x {estado_jogo['Time B']['gols']}"
    )
    label_cartoes_a.config(
        text=(
            f"🟨 {estado_jogo['Time A']['amarelos']}   |   "
            f"🟥 {estado_jogo['Time A']['vermelhos']}"
        )
    )
    label_cartoes_b.config(
        text=(
            f"🟨 {estado_jogo['Time B']['amarelos']}   |   "
            f"🟥 {estado_jogo['Time B']['vermelhos']}"
        )
    )


def registrar_gol(time):
    estado_jogo[time]["gols"] += 1
    atualizar_ui()
    notificar_painel_digital(time, "Gol ⚽")
    messagebox.showinfo(
        "GOOOOL! ⚽",
        f"Gol registrado para o {time}!\nPlacar atualizado na nuvem.",
    )


def registrar_cartao(time, cor):
    if cor == "Amarelo":
        estado_jogo[time]["amarelos"] += 1
        icone = "🟨"
    else:
        estado_jogo[time]["vermelhos"] += 1
        icone = "🟥"

    atualizar_ui()
    notificar_painel_digital(time, f"Cartão {cor}")
    messagebox.showwarning(
        f"Cartão {cor} {icone}",
        f"Cartão {cor} registrado para o {time}!",
    )


def notificar_painel_digital(time, evento):
    label_status.config(
        text=f"Último evento: {evento} para o {time} (Enviado para a Nuvem ☁️)",
        fg="#2ecc71",
    )
    print(f"[POST /api/eventos] -> {evento} registrado para {time}.")


def abrir_painel():
    janela = login
    for widget in janela.winfo_children():
        widget.destroy()

    janela.title("TorcidaNet - Painel do Mesário")
    centralizar_janela(janela, 500, 420)
    janela.configure(bg="#2c3e50")
    janela.resizable(False, False)

    tk.Label(
        janela,
        text="🔴 AO VIVO - TorcidaNet",
        font=("Arial", 16, "bold"),
        fg="white",
        bg="#e74c3c",
        pady=10,
    ).pack(fill=tk.X)

    global label_placar, label_cartoes_a, label_cartoes_b, label_status

    frame_placar = tk.Frame(janela, bg="#2c3e50")
    frame_placar.pack(pady=15)

    tk.Label(
        frame_placar,
        text="Time A (Casa)",
        font=("Arial", 12, "bold"),
        fg="white",
        bg="#2c3e50",
    ).grid(row=0, column=0, padx=20)
    tk.Label(
        frame_placar,
        text="Time B (Fora)",
        font=("Arial", 12, "bold"),
        fg="white",
        bg="#2c3e50",
    ).grid(row=0, column=2, padx=20)

    label_placar = tk.Label(
        frame_placar,
        text="0 x 0",
        font=("Arial", 45, "bold"),
        fg="#f1c40f",
        bg="#2c3e50",
    )
    label_placar.grid(row=1, column=0, columnspan=3, pady=5)

    label_cartoes_a = tk.Label(
        frame_placar,
        text="🟨 0   |   🟥 0",
        font=("Arial", 11),
        fg="#bdc3c7",
        bg="#2c3e50",
    )
    label_cartoes_a.grid(row=2, column=0, pady=5)

    label_cartoes_b = tk.Label(
        frame_placar,
        text="🟨 0   |   🟥 0",
        font=("Arial", 11),
        fg="#bdc3c7",
        bg="#2c3e50",
    )
    label_cartoes_b.grid(row=2, column=2, pady=5)

    frame_controles = tk.Frame(janela, bg="#2c3e50")
    frame_controles.pack(pady=10)

    tk.Button(
        frame_controles, text="⚽ Gol Time A", bg="#27ae60", fg="white",
        font=("Arial", 11, "bold"), width=14,
        command=lambda: registrar_gol("Time A"),
    ).grid(row=0, column=0, padx=15, pady=5)
    tk.Button(
        frame_controles, text="🟨 Amarelo A", bg="#f39c12",
        font=("Arial", 10, "bold"), width=16,
        command=lambda: registrar_cartao("Time A", "Amarelo"),
    ).grid(row=1, column=0, padx=15, pady=3)
    tk.Button(
        frame_controles, text="🟥 Vermelho A", bg="#c0392b", fg="white",
        font=("Arial", 10, "bold"), width=16,
        command=lambda: registrar_cartao("Time A", "Vermelho"),
    ).grid(row=2, column=0, padx=15, pady=3)

    tk.Button(
        frame_controles, text="⚽ Gol Time B", bg="#27ae60", fg="white",
        font=("Arial", 11, "bold"), width=14,
        command=lambda: registrar_gol("Time B"),
    ).grid(row=0, column=1, padx=15, pady=5)
    tk.Button(
        frame_controles, text="🟨 Amarelo B", bg="#f39c12",
        font=("Arial", 10, "bold"), width=16,
        command=lambda: registrar_cartao("Time B", "Amarelo"),
    ).grid(row=1, column=1, padx=15, pady=3)
    tk.Button(
        frame_controles, text="🟥 Vermelho B", bg="#c0392b", fg="white",
        font=("Arial", 10, "bold"), width=16,
        command=lambda: registrar_cartao("Time B", "Vermelho"),
    ).grid(row=2, column=1, padx=15, pady=3)

    label_status = tk.Label(
        janela,
        text="Sistema pronto. Aguardando início do jogo.",
        font=("Arial", 10),
        fg="#95a5a6",
        bg="#2c3e50",
    )
    label_status.pack(side=tk.BOTTOM, pady=15)


def fazer_login(event=None):
    usuario = entrada_usuario.get().strip()
    senha = entrada_senha.get()

    if usuario == "admin" and senha == "1234":
        abrir_painel()
    else:
        messagebox.showerror(
            "Acesso negado",
            "Usuário ou senha incorretos.",
            parent=login,
        )
        entrada_senha.delete(0, tk.END)
        entrada_senha.focus()


login = tk.Tk()
login.title("TorcidaNet - Login")
centralizar_janela(login, 420, 520)
login.configure(bg="#f5f6fa")
login.resizable(False, False)

cartao = tk.Frame(login, bg="white", padx=35, pady=25)
cartao.place(relx=0.5, rely=0.5, anchor="center", width=360, height=500)

try:
    imagem_baixada = Image.open(r"C:\Users\aluno\Downloads\image_63284d71.jpg")
    imagem_baixada.thumbnail((150, 150), Image.Resampling.LANCZOS)
    imagem_login = ImageTk.PhotoImage(imagem_baixada)
    label_imagem = tk.Label(cartao, image=imagem_login, bg="white")
    label_imagem.image = imagem_login
    label_imagem.pack(pady=(0, 8))
    login.iconphoto(True, imagem_login)
except (OSError, tk.TclError):
    tk.Label(
        cartao,
        text="TorcidaNet",
        font=("Arial", 20, "bold"),
        fg="#9a003f",
        bg="white",
    ).pack(pady=(10, 20))

tk.Label(
    cartao,
    text="Acesso do Mesário",
    font=("Arial", 15, "bold"),
    fg="#2c3e50",
    bg="white",
).pack(pady=(0, 18))

tk.Label(
    cartao,
    text="Usuário",
    font=("Arial", 10),
    fg="#636e72",
    bg="white",
).pack(anchor="w")

entrada_usuario = tk.Entry(
    cartao,
    font=("Arial", 11),
    relief="solid",
    borderwidth=1,
)
entrada_usuario.pack(fill=tk.X, ipady=7, pady=(4, 12))

label_senha = tk.Label(
    cartao,
    text="Senha",
    font=("Arial", 10),
    fg="#636e72",
    bg="white",
)
label_senha.pack(anchor="w")

entrada_senha = tk.Entry(
    cartao,
    font=("Arial", 11),
    relief="solid",
    borderwidth=1,
    show="•",
    state="normal",
    takefocus=True,
    exportselection=False,
)
entrada_senha.pack(fill=tk.X, ipady=7, pady=(4, 16))
entrada_senha.bind("<Button-1>", lambda event: entrada_senha.focus_set())
label_senha.bind("<Button-1>", lambda event: entrada_senha.focus_set())

tk.Button(
    cartao,
    text="ENTRAR",
    command=fazer_login,
    font=("Arial", 13, "bold"),
    fg="white",
    bg="#9a003f",
    activebackground="#7b0032",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
).pack(fill=tk.X, ipady=14)

def ir_para_senha(event=None):
    entrada_senha.focus_set()
    return "break"


entrada_usuario.bind("<Return>", ir_para_senha)
entrada_usuario.bind("<Tab>", ir_para_senha)
entrada_senha.bind("<Return>", fazer_login)
login.bind("<Return>", fazer_login)
entrada_usuario.focus()
login.mainloop()
