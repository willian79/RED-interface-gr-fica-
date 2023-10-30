import tkinter as tk
import sqlite3

# Função para salvar os dados no banco de dados
def salvar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    cidade = entry_cidade.get()
    estado = entry_estado.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    experiencia = text_experiencia.get("1.0", "end")
    empregabilidade = text_empregabilidade.get("1.0", "end")
    
    # Conectar ao banco de dados (ou criar um novo)
    conn = sqlite3.connect("dados_devs.db")
    cursor = conn.cursor()
    
    # Criar tabela (caso não exista)
    cursor.execute('''CREATE TABLE IF NOT EXISTS desenvolvedores
                      (nome text, idade integer, cidade text, estado text,
                       telefone text, email text, experiencia text, empregabilidade text)'')

    # Inserir os dados na tabela
    cursor.execute("INSERT INTO desenvolvedores VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (nome, idade, cidade, estado, telefone, email, experiencia, empregabilidade))
    
    # Commit e fechar a conexão
    conn.commit()
    conn.close()

    # Limpar os campos após a submissão
    entry_nome.delete(0, "end")
    entry_idade.delete(0, "end")
    entry_cidade.delete(0, "end")
    entry_estado.delete(0, "end")
    entry_telefone.delete(0, "end")
    entry_email.delete(0, "end")
    text_experiencia.delete("1.0", "end")
    text_empregabilidade.delete("1.0", "end")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Formulário de Cadastro")

# Campos de entrada de dados
label_nome = tk.Label(root, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

label_idade = tk.Label(root, text="Idade:")
label_idade.pack()
entry_idade = tk.Entry(root)
entry_idade.pack()

label_cidade = tk.Label(root, text="Cidade:")
label_cidade.pack()
entry_cidade = tk.Entry(root)
entry_cidade.pack()

label_estado = tk.Label(root, text="Estado:")
label_estado.pack()
entry_estado = tk.Entry(root)
entry_estado.pack()

label_telefone = tk.Label(root, text="Telefone:")
label_telefone.pack()
entry_telefone = tk.Entry(root)
entry_telefone.pack()

label_email = tk.Label(root, text="E-mail:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

label_experiencia = tk.Label(root, text="Experiência:")
label_experiencia.pack()
text_experiencia = tk.Text(root, height=5, width=30)
text_experiencia.pack()

label_empregabilidade = tk.Label(root, text="Empregabilidade:")
label_empregabilidade.pack()
text_empregabilidade = tk.Text(root, height=5, width=30)
text_empregabilidade.pack()

# Botão de submissão
button_salvar = tk.Button(root, text="Salvar", command=salvar_dados)
button_salvar.pack()

root.mainloop()
