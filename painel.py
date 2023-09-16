import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import csv
from tkinter import filedialog
import matplotlib.pyplot as plt
from dados import inserir_dados

# Função para criar a janela de inserção de dados
def abrir_janela_inserir_dados():
    setor_selecionado = setor_combobox.get()
    if setor_selecionado:
        janela_inserir_dados = tk.Toplevel(root)
        janela_inserir_dados.title(f"Inserir Dados para {setor_selecionado}")

        nome_label = ttk.Label(janela_inserir_dados, text="Nome:")
        nome_entry = ttk.Entry(janela_inserir_dados)

        idade_label = ttk.Label(janela_inserir_dados, text="Idade:")
        idade_entry = ttk.Entry(janela_inserir_dados)

        def salvar_dados():
            nome = nome_entry.get()
            idade = idade_entry.get()

            if nome and idade:
                inserir_dados(setor_selecionado, nome, idade)
                messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
                janela_inserir_dados.destroy()
            else:
                messagebox.showerror("Erro", "Preencha todos os campos!")

        salvar_button = ttk.Button(janela_inserir_dados, text="Salvar", command=salvar_dados)

        nome_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        nome_entry.grid(row=0, column=1, padx=5, pady=5)

        idade_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        idade_entry.grid(row=1, column=1, padx=5, pady=5)

        salvar_button.grid(row=2, columnspan=2, pady=10)

# Função para visualizar os dados da tabela por setor
def visualizar_dados_por_setor():
    setor_selecionado = setor_combobox.get()
    if setor_selecionado:
        try:
            conn = sqlite3.connect('dados.db')
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Dados WHERE Setor=?", (setor_selecionado,))
            rows = cursor.fetchall()

            if rows:
                janela_visualizacao = tk.Toplevel(root)
                janela_visualizacao.title(f"Dados para o Setor {setor_selecionado}")

                tree = ttk.Treeview(janela_visualizacao, columns=("Nome", "Idade"), show="headings")
                tree.heading("Nome", text="Nome")
                tree.heading("Idade", text="Idade")

                for row in rows:
                    tree.insert("", "end", values=(row[2], row[3]))

                tree.pack(fill="both", expand=True)

                conn.close()
            else:
                messagebox.showinfo("Aviso", f"Não há dados para mostrar no setor {setor_selecionado}.")

        except Exception as e:
            print(f"Erro ao visualizar dados: {e}")

# Função para exportar os dados para um arquivo CSV
def exportar_para_csv():
    setor_selecionado = setor_combobox.get()
    if setor_selecionado:
        try:
            conn = sqlite3.connect('dados.db')
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Dados WHERE Setor=?", (setor_selecionado,))
            rows = cursor.fetchall()

            if rows:
                arquivo_csv = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Arquivos CSV", "*.csv")])

                if arquivo_csv:
                    with open(arquivo_csv, 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(["Nome", "Idade"])
                        writer.writerows([(row[2], row[3]) for row in rows])
                    messagebox.showinfo("Sucesso", "Dados exportados para CSV com sucesso!")
            else:
                messagebox.showinfo("Aviso", f"Não há dados para exportar no setor {setor_selecionado}.")

            conn.close()
        except Exception as e:
            print(f"Erro ao exportar dados para CSV: {e}")

root = tk.Tk()
root.title("Painel")

frame = ttk.Frame(root, padding=10)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E))

setor_label = ttk.Label(frame, text="Selecione o setor:")
setor_label.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

setores = ["UTI", "PS", "RETAGUARDA", "ENFERMARIA", "OBSERVACAO", "PEDIATRIA", "PSIQUIATRIA", "MEDICACAO"]
setor_combobox = ttk.Combobox(frame, values=setores)
setor_combobox.grid(column=1, row=0, padx=5, pady=5)

inserir_button = ttk.Button(frame, text="Inserir Dados", command=abrir_janela_inserir_dados)
visualizar_button = ttk.Button(frame, text="Visualizar Dados por Setor", command=visualizar_dados_por_setor)
exportar_button = ttk.Button(frame, text="Exportar para CSV", command=exportar_para_csv)

inserir_button.grid(column=0, row=1, padx=5, pady=5)
visualizar_button.grid(column=1, row=1, padx=5, pady=5)
exportar_button.grid(column=2, row=1, padx=5, pady=5)

# Função para criar gráfico
def criar_grafico():
    setor_selecionado = setor_combobox.get()
    if setor_selecionado:
        try:
            conn = sqlite3.connect('dados.db')
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Dados WHERE Setor=?", (setor_selecionado,))
            rows = cursor.fetchall()

            nomes = [row[2] for row in rows]
            idades = [row[3] for row in rows]

            # Plotar o gráfico de barras
            plt.figure(figsize=(8, 6))  # Tamanho da figura
            plt.bar(nomes, idades)
            plt.xlabel('Nomes')
            plt.ylabel('Idades')
            plt.title(f'Gráfico de Idades no Setor {setor_selecionado}')
            plt.xticks(rotation=45)

            plt.show()
            conn.close()
        except Exception as e:
            print(f"Erro ao criar gráfico: {e}")

# Botão para criar gráfico
criar_grafico_button = ttk.Button(frame, text="Criar Gráfico", command=criar_grafico)
criar_grafico_button.grid(column=3, row=1, padx=5, pady=5)

root.mainloop()
