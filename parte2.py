import tkinter as tk
import sqlite3

# Função para buscar candidatos com base nos filtros
def buscar_candidatos():
    cidade = entry_cidade.get()
    estado = entry_estado.get()
    expectativa_salarial = entry_expectativa_salarial.get()
    area_trabalho = entry_area_trabalho.get()
    
    # Conectar ao banco de dados
    conn = sqlite3.connect("dados_devs.db")
    cursor = conn.cursor()
    
    # Construir a consulta SQL com base nos filtros
    consulta = "SELECT * FROM desenvolvedores WHERE 1=1"
    if cidade:
        consulta += f" AND cidade = '{cidade}'"
    if estado:
        consulta += f" AND estado = '{estado}'"
    if expectativa_salarial:
        consulta += f" AND expectativa_salarial = '{expectativa_salarial}'"
    if area_trabalho:
        consulta += f" AND area_trabalho = '{area_trabalho}'"
    
    # Executar a consulta
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    
    # Limpar a lista de candidatos e mostrar os resultados
    lista_candidatos.delete(0, tk.END)
    for candidato in resultados:
        lista_candidatos.insert(tk.END, candidato[0])
    
    # Fechar a conexão com o banco
    conn.close()

# Função para exibir detalhes do candidato selecionado
def mostrar_detalhes(event):
    index = lista_candidatos.curselection()[0]
    nome_candidato = lista_candidatos.get(index)
    
    # Conectar ao banco de dados
    conn = sqlite3.connect("dados_devs.db")
    cursor = conn.cursor()
    
    # Selecionar os detalhes do candidato
    cursor.execute("SELECT * FROM desenvolvedores WHERE nome = ?", (nome_candidato,))
    detalhes = cursor.fetchone()
    
    # Exibir detalhes na interface
    label_detalhes.config(text=f"Detalhes de {nome_candidato}:\n\nIdade: {detalhes[1]}\nCidade: {detalhes[2]}\nEstado: {detalhes[3]}\nTelefone: {detalhes[4]}\nE-mail: {detalhes[5]}\nExperiência: {detalhes[6]}\nEmpregabilidade: {detalhes[7]}")
    
    # Fechar a conexão com o banco
    conn.close()

# Configuração da interface gráfica para recrutadores
root_recrutador = tk.Tk()
root_recrutador.title("Painel do Recrutador")

# Campos de filtro
label_cidade = tk.Label(root_recrutador, text="Cidade:")
label_cidade.grid(row=0, column=0)
entry_cidade = tk.Entry(root_recrutador)
entry_cidade.grid(row=0, column=1)

label_estado = tk.Label(root_recrutador, text="Estado:")
label_estado.grid(row=1, column=0)
entry_estado = tk.Entry(root_recrutador)
entry_estado.grid(row=1, column=1)

label_expectativa_salarial = tk.Label(root_recrutador, text="Expectativa Salarial:")
label_expectativa_salarial.grid(row=2, column=0)
entry_expectativa_salarial = tk.Entry(root_recrutador)
entry_expectativa_salarial.grid(row=2, column=1)

label_area_trabalho = tk.Label(root_recrutador, text="Área de Trabalho:")
label_area_trabalho.grid(row=3, column=0)
entry_area_trabalho = tk.Entry(root_recrutador)
entry_area_trabalho.grid(row=3, column=1)

button_buscar = tk.Button(root_recrutador, text="Buscar Candidatos", command=buscar_candidatos)
button_buscar.grid(row=4, columnspan=2)

# Lista de candidatos
lista_candidatos = tk.Listbox(root_recrutador, selectmode=tk.SINGLE)
lista_candidatos.grid(row=5, columnspan=2)
lista_candidatos.bind("<<ListboxSelect>>", mostrar_detalhes)

# Detalhes do candidato
label_detalhes = tk.Label(root_recrutador, text="Detalhes do Candidato:")
label_detalhes.grid(row=6, columnspan=2)

root_recrutador.mainloop()
