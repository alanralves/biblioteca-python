# Importando as bibliotecas
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from banco import Banco

# Métodos

# Método para popular a tabela usuarios
def popular_usuarios():
    
    banco = Banco() # Cria instacia da classe banco
    tree_usuarios.delete(*tree_usuarios.get_children()) # Limpa as linhas da treeview usuarios
    pesquisa = "SELECT * FROM usuarios ORDER BY id" # Define a pesquisa a ser feita no banco de dados
    linhas = banco.select(pesquisa) # Variavel com o resultado da busca feita com método select da classe banco
    for i in linhas: # Itera sobre as linhas do resultado da pesquisa
        tree_usuarios.insert('','end',values= i) # Insere as linhas na treeview usuarios

# Método para popular a tabela livros
def popular_livros():
    
    banco = Banco() # Cria instacia da classe banco
    tree_livros.delete(*tree_livros.get_children()) # Limpa as linhas da treeview livros
    pesquisa = "SELECT * FROM livros ORDER BY titulo" # Define a pesquisa a ser feita no banco de dados
    linhas = banco.select(pesquisa) # Variavel com o resultado da busca feita com método select da classe banco
    for i in linhas: # Itera sobre as linhas do resultado da pesquisa
        tree_livros.insert('','end',values= i) # Insere as linhas na treeview livros

# Método para inserir usuários
def inserir_usuario():

    banco = Banco() # Cria instacia da classe banco
    if txt_nome.get() == "" or txt_telefone.get() == "" or txt_email.get() == "": # Verifica se algum dos campos está vazio
        messagebox.showinfo(title="ERRO", message="Digite todos os dados") # Mensagem caso algum campo esteja vazio
        return
    try: # Inicia o tratamento de erro
        pesquisa = "INSERT INTO usuarios (nome, telefone, email) VALUES ('"+txt_nome.get()+"','"+txt_telefone.get()+"','"+txt_email.get()+"')" # Define a pesquisa a ser feita no banco de dados
        banco.change(pesquisa) # Chama o método change da classe banco
    except: # Trecho chamado em caso de erro
        messagebox.showinfo(title="ERRO", message="Erro ao inserir os dados") # Mensagem em caso de erro
        return
    popular_usuarios() # Chama o método para popular a tabela usuarios
    txt_nome.delete(0,tk.END) # Deleta os dados no campo
    txt_telefone.delete(0,tk.END) # Deleta os dados no campo
    txt_email.delete(0,tk.END) # Deleta os dados no campo

# Método para inserir livros no banco de dados
def inserir_livro():

    banco = Banco() # Cria instacia da classe banco
    if txt_titulo.get() == "" or txt_autor.get() == "" or txt_ano.get() == "" or txt_quantidade.get() == "": # Verifica se algum dos campos está vazio
        messagebox.showinfo(title="ERRO", message="Digite todos os dados") # Mensagem caso algum campo esteja vazio
        return
    try: # Inicia o tratamento de erro
        pesquisa = "INSERT INTO livros (titulo, autor, ano, quantidade) VALUES ('"+txt_titulo.get()+"','"+txt_autor.get()+"','"+txt_ano.get()+"','"+txt_quantidade.get()+"')" # Define a pesquisa a ser feita no banco de dados
        banco.change(pesquisa) # Chama o método change da classe banco
    except: # Trecho chamado em caso de erro
        messagebox.showinfo(title="ERRO", message="Erro ao inserir os dados") # Mensagem em caso de erro
        return
    popular_livros() # Chama o método para popular a tabela livros
    txt_titulo.delete(0,tk.END) # Deleta os dados no campo
    txt_autor.delete(0,tk.END) # Deleta os dados no campo
    txt_ano.delete(0,tk.END) # Deleta os dados no campo
    txt_quantidade.delete(0,tk.END) # Deleta os dados no campo

# Método para pesquisar usuarios no banco de dados
def pesquisar_usuario():
   
        banco = Banco() # Cria instacia da classe banco
        tree_usuarios.delete(*tree_usuarios.get_children()) # Limpa as linhas da treeview usuarios
        pesquisa = "SELECT * FROM usuarios WHERE nome LIKE '%"+txt_pesquisa_nome.get()+"%'" # Define a pesquisa a ser feita no banco de dados
        linhas = banco.select(pesquisa) # Variavel com o resultado da busca feita com método select da classe banco
        for i in linhas: # Itera sobre as linhas do resultado da pesquisa
            tree_usuarios.insert('','end',values= i) # Insere as linhas na treeview usuarios

        txt_pesquisa_nome.delete(0,tk.END) # Deleta os dados no campo


# Método para pesquisar livros no banco de dados
def pesquisar_livro():
    
    banco = Banco() # Cria instacia da classe banco
    tree_livros.delete(*tree_livros.get_children()) # Limpa as linhas da treeview usuarios

    if txt_pesquisa_titulo.get() != "": # Verifica se o campo tem alguma informação
        pesquisa = "SELECT * FROM livros WHERE titulo LIKE '%"+txt_pesquisa_titulo.get()+"%'" # Define a pesquisa a ser feita no banco de dados
    elif txt_pesquisa_autor.get() != "": # Verifica se o campo tem alguma informação
        pesquisa = "SELECT * FROM livros WHERE autor LIKE '%"+txt_pesquisa_autor.get()+"%'" # Define a pesquisa a ser feita no banco de dados
    else: # Trecho chamado caso nenhum dos dois campos anteriores tenha alguma informação
        pesquisa = "SELECT * FROM livros WHERE ano LIKE '%"+txt_pesquisa_ano.get()+"%'" # Define a pesquisa a ser feita no banco de dados
    
    linhas = banco.select(pesquisa) # Variavel com o resultado da busca feita com método select da classe banco
    for i in linhas: # Itera sobre as linhas do resultado da pesquisa
        tree_livros.insert('','end',values= i) # Insere as linhas na treeview livros
    
    txt_pesquisa_titulo.delete(0,tk.END) # Deleta os dados no campo
    txt_pesquisa_autor.delete(0,tk.END) # Deleta os dados no campo
    txt_pesquisa_ano.delete(0,tk.END) # Deleta os dados no campo


# Método para emprestar livros
def emprestar_livro():

    banco = Banco() # Cria instacia da classe banco
    if txt_empresta_titulo.get() == "": # Verifica se o campo está vazio
        messagebox.showinfo(title="ERRO", message="Digite o título do livro") # Mensagem caso o campo esteja vazio
        return
    try: # Inicia o tratamento de erro
        pesquisa = "SELECT quantidade FROM livros WHERE titulo = '"+txt_empresta_titulo.get()+"'" # Define a pesquisa a ser feita no banco de dados
        retorno_pesquisa = banco.selectUpdate(pesquisa) # Variavel com o resultado da busca feita com método selectupdate da classe banco  
        quantidade = retorno_pesquisa[0] -1 # Diminuido 1 da quantidade retornada na pesquisa
        atualiza = "UPDATE livros SET quantidade = '"+str(quantidade)+"' WHERE titulo = '"+txt_empresta_titulo.get()+"'" # Define a alteração a ser feita no banco de dados
        banco.change(atualiza) # Chama o método change da classe banco
    except: # Trecho chamado em caso de erro
        messagebox.showinfo(title="ERRO", message="Livro não encontraro") # Mensagem em caso de erro
        return
    popular_livros() # Chama o método para popular a tabela livros
    txt_empresta_titulo.delete(0,tk.END) # Deleta os dados no campo
    messagebox.showinfo(title="Mensagem", message="Livro retirado") # Mensagem final


# Método para devolver livros (comandos iguais os do método para emprestar_livros, porém adiciona 1 unidade na quantidade em vez de retirar)
def devolver_livro():

    banco = Banco() # Cria instacia da classe banco
    if txt_empresta_titulo.get() == "":
        messagebox.showinfo(title="ERRO", message="Digite o título do livro")
        return
    try:
        pesquisa = "SELECT quantidade FROM livros WHERE titulo = '"+txt_empresta_titulo.get()+"'"
        retorno_pesquisa = banco.selectUpdate(pesquisa)        
        quantidade = retorno_pesquisa[0] +1
        atualiza = "UPDATE livros SET quantidade = '"+str(quantidade)+"' WHERE titulo = '"+txt_empresta_titulo.get()+"'"
        banco.change(atualiza)
    except:
        messagebox.showinfo(title="ERRO", message="Livro não encontrado")
        return
    popular_livros()
    txt_empresta_titulo.delete(0,tk.END)
    messagebox.showinfo(title="Mensagem", message="Livro devolvido")

def verificar_disponibilidade():

    banco = Banco() # Cria instacia da classe banco
    
    try:
        pesquisa = "SELECT quantidade FROM livros WHERE titulo = '"+txt_empresta_titulo.get()+"'"
        retorno_pesquisa = banco.selectUpdate(pesquisa)
        quantidade = retorno_pesquisa[0]

        if quantidade > 0: # Verifica se a quantidade é zero
            messagebox.showinfo(title="Mensagem", message=f"Livro {txt_empresta_titulo.get()} com {quantidade} unidades disponiveis") # Mensagem em caso de livro disponivel
        else:
            messagebox.showinfo(title="Mensagem", message=f"Livro {txt_empresta_titulo.get()} indisponivel") # Mensagem em caso de livro indisponivel
            
        txt_empresta_titulo.delete(0,tk.END)
    except Exception as e:
        messagebox.showinfo(title="Mensagem", message=f"Livro não encontrado") # Mensagem em caso de erro

    


# Inicia a criação da interface gráfica _____________________________________

app = tk.Tk() # Cria a tela do sistema
app.title("Lib System") # Titulo da janela do sistema
app.geometry("1000x600") # Tamanho da janela
app.configure(background="#F2F2F2")

container_usuarios = tk.Frame(app,width=300,height=550) # Cria container para todas interações com a base de usuarios
container_usuarios.pack(side=tk.LEFT,anchor=tk.N) # Apresenta container na tela
container_usuarios.configure(background="#F2F2F2")

container_livros = tk.Frame(app,width=300,height=550) # Cria container para todas interações com a base de livros
container_livros.pack(side=tk.LEFT,anchor=tk.N) # Apresenta container na tela
container_livros.configure(background="#F2F2F2")


# Inicia a definição dos componentes do quadro usuario ____________________________________________

quadro_usuarios = tk.LabelFrame(container_usuarios,text='Base de usuários') # Cria quadro para todas interações com a base de usuarios
quadro_usuarios.pack(fill="both",expand="yes",padx=8,pady=8,ipady=5) # Apresenta quadro na tela
quadro_usuarios.configure(background="#F2F2F2")

quadro_tabela_usuarios = tk.LabelFrame(quadro_usuarios,text='Usuários') # Quadro para a tabela da base de usuarios
quadro_tabela_usuarios.pack(fill="both",expand="yes",padx=8,pady=8,ipady=5) # Apresenta quadro na tela
quadro_tabela_usuarios.configure(background="#F2F2F2")

tree_usuarios = ttk.Treeview(quadro_tabela_usuarios,columns=('id','nome','telefone','email'),show='headings') # Cria a tabela usuarios
tree_usuarios.column('id',minwidth=25,width=25) # Cria coluna na tabela
tree_usuarios.column('nome',minwidth=90,width=90)
tree_usuarios.column('telefone',minwidth=80,width=80)
tree_usuarios.column('email',minwidth=100,width=100)
tree_usuarios.heading('id',text='ID') # Define nome da coluna
tree_usuarios.heading('nome',text='Nome')
tree_usuarios.heading('telefone',text='Telefone')
tree_usuarios.heading('email',text='Email')
tree_usuarios.pack(fill='both',expand='yes')
popular_usuarios() # Carrega os dados na tabela


# Inicia a definição dos componentes do quadro para cadastro de usuario ____________________________________________

quadro_cadastrar = tk.LabelFrame(quadro_usuarios,text='Cadastrar')
quadro_cadastrar.pack(fill="both",expand="yes",padx=8,pady=8,ipady=5)
quadro_cadastrar.configure(background="#F2F2F2")

container_cadastrar_usuarios = tk.Frame(quadro_cadastrar,width=300)
container_cadastrar_usuarios.pack()
container_cadastrar_usuarios.configure(background="#F2F2F2")

lbl_nome = tk.Label(container_cadastrar_usuarios,text="Nome:") # Cria o texto "Nome" ao lado da caixa de pesquisa
lbl_nome.pack(side=tk.LEFT)
lbl_nome.configure(background="#F2F2F2")

txt_nome = tk.Entry(container_cadastrar_usuarios,width=12) # Cria a caixa de texto nome
txt_nome.pack(padx=10,side=tk.LEFT) 

lbl_telefone = tk.Label(container_cadastrar_usuarios,text="Telefone:") # Cria o texto "Telefone" ao lado da caixa de pesquisa
lbl_telefone.pack(side=tk.LEFT)
lbl_telefone.configure(background="#F2F2F2")

txt_telefone = tk.Entry(container_cadastrar_usuarios,width=12) # Cria a caixa de texto telefone
txt_telefone.pack(padx=10,side=tk.LEFT)

lbl_email = tk.Label(container_cadastrar_usuarios,text="Email:") # Cria o texto "Email" ao lado da caixa de pesquisa
lbl_email.pack(side=tk.LEFT)
lbl_email.configure(background="#F2F2F2")

txt_email = tk.Entry(container_cadastrar_usuarios,width=12) # Cria a caixa de texto email
txt_email.pack(padx=10,side=tk.LEFT)

btn_inserir_usuario = tk.Button(quadro_cadastrar,text="Cadastrar",width=10,command=inserir_usuario) # Cria o botão inserir
btn_inserir_usuario.pack(padx=10,pady=2,side=tk.LEFT)
btn_inserir_usuario.configure(background="#4682B4", foreground="#F8F8FF",border=0)

# Inicia a definição dos componentes do quadro para pesquisa de usuario ____________________________________________

quadro_pesquisar_usuarios = tk.LabelFrame(quadro_usuarios,text='Pesquisar')
quadro_pesquisar_usuarios.pack(fill="both",expand="yes",padx=8,pady=8,ipady=5)
quadro_pesquisar_usuarios.configure(background="#F2F2F2")

container_pesquisar_usuarios = tk.Frame(quadro_pesquisar_usuarios,width=300)
container_pesquisar_usuarios.pack(anchor=tk.W)
container_pesquisar_usuarios.configure(background="#F2F2F2")

lbl_pesquisa_nome = tk.Label(container_pesquisar_usuarios,text="Nome:") # Cria o texto "Nome" ao lado da caixa de pesquisa
lbl_pesquisa_nome.pack(side=tk.LEFT)
lbl_pesquisa_nome.configure(background="#F2F2F2")

txt_pesquisa_nome = tk.Entry(container_pesquisar_usuarios,width=30) # Cria a caixa de texto nome
txt_pesquisa_nome.pack(padx=10,pady=5,side=tk.LEFT)

btn_pesquisar_usuario = tk.Button(quadro_pesquisar_usuarios,text="Pesquisar",width=10,command=pesquisar_usuario) # Cria o botão pesquisar e chama o método pesquisar_usuario ao clicar
btn_pesquisar_usuario.pack(padx=10,pady=2,side=tk.LEFT)
btn_pesquisar_usuario.configure(background="#4682B4",foreground="#F8F8FF",border=0)

btn_restaurar_usuario = tk.Button(quadro_pesquisar_usuarios,text="Restaurar tabela",width=15,command=popular_usuarios) # Cria o botão inserir e chama o método popular_usuario ao clicar
btn_restaurar_usuario.pack(padx=10,pady=2,side=tk.LEFT)
btn_restaurar_usuario.configure(background="#4682B4",foreground="#F8F8FF",border=0)

##################################


# Inicia a definição dos componentes do quadro livros ____________________________________________

quadro_livros = tk.LabelFrame(container_livros,text='Base de livros') # Cria quadro para todas interações com a base de usuarios
quadro_livros.pack(fill="both",expand="yes",padx=8,pady=8,ipady=5)
quadro_livros.configure(background="#F2F2F2")

quadro_tabela_livros = tk.LabelFrame(quadro_livros,text='Livros') # Cria quadro para a tabela de livros
quadro_tabela_livros.pack(fill="both",expand="yes",padx=8,pady=8,ipady=5)
quadro_tabela_livros.configure(background="#F2F2F2")

tree_livros = ttk.Treeview(quadro_tabela_livros,columns=('titulo','autor','ano','quantidade'),show='headings') # Cria a tabela livros
tree_livros.column('titulo',minwidth=100,width=100) # Cria coluna na tabela
tree_livros.column('autor',minwidth=100,width=100)
tree_livros.column('ano',minwidth=35,width=35)
tree_livros.column('quantidade',minwidth=25,width=25)
tree_livros.heading('titulo',text='Título') # Define nome da coluna
tree_livros.heading('autor',text='Autor')
tree_livros.heading('ano',text='Ano de pub.')
tree_livros.heading('quantidade',text='Quantidade')
tree_livros.pack(fill='both',expand='yes')
popular_livros() # Carrega os dados na tabela


# Inicia a definição dos componentes do quadro para inserir livros ____________________________________________

quadro_inserir = tk.LabelFrame(quadro_livros,text='Inserir')
quadro_inserir.pack(fill="both",expand="yes",padx=8,pady=8,ipady=5)
quadro_inserir.configure(background="#F2F2F2")

container_inserir_livros = tk.Frame(quadro_inserir,width=300)
container_inserir_livros.pack()
container_inserir_livros.configure(background="#F2F2F2")

lbl_titulo = tk.Label(container_inserir_livros,text="Título:") # Cria o texto "Nome" ao lado da caixa de pesquisa
lbl_titulo.pack(side=tk.LEFT)
lbl_titulo.configure(background="#F2F2F2")

txt_titulo = tk.Entry(container_inserir_livros,width=12) # Cria a caixa de texto nome
txt_titulo.pack(padx=10,side=tk.LEFT) 

lbl_autor = tk.Label(container_inserir_livros,text="Autor:") # Cria o texto "Telefone" ao lado da caixa de pesquisa
lbl_autor.pack(side=tk.LEFT)
lbl_autor.configure(background="#F2F2F2")

txt_autor = tk.Entry(container_inserir_livros,width=12) # Cria a caixa de texto telefone
txt_autor.pack(padx=10,side=tk.LEFT)

lbl_ano = tk.Label(container_inserir_livros,text="Ano:") # Cria o texto "Email" ao lado da caixa de pesquisa
lbl_ano.pack(side=tk.LEFT)
lbl_ano.configure(background="#F2F2F2")

txt_ano = tk.Entry(container_inserir_livros,width=5) # Cria a caixa de texto email
txt_ano.pack(padx=10,side=tk.LEFT)

lbl_quantidade = tk.Label(container_inserir_livros,text="Quantidade:") # Cria o texto "Email" ao lado da caixa de pesquisa
lbl_quantidade.pack(side=tk.LEFT)
lbl_quantidade.configure(background="#F2F2F2")

txt_quantidade = tk.Entry(container_inserir_livros,width=5) # Cria a caixa de texto email
txt_quantidade.pack(padx=10,side=tk.LEFT)

btn_inserir_livro = tk.Button(quadro_inserir,text="Inserir",width=10,command=inserir_livro) # Cria o botão inserir e chama o método inserir_livro ao clicar
btn_inserir_livro.pack(padx=10,pady=2,side=tk.LEFT)
btn_inserir_livro.configure(background="#4682B4",foreground="#F8F8FF",border=0)


# Inicia a definição dos componentes do quadro para pesquisa de livros ____________________________________________

quadro_pesquisar = tk.LabelFrame(quadro_livros,text='Pesquisar')
quadro_pesquisar.pack(fill="both",expand="yes",padx=8,pady=8,ipady=5)
quadro_pesquisar.configure(background="#F2F2F2")

container_pesquisar_livros = tk.Frame(quadro_pesquisar,width=300)
container_pesquisar_livros.pack()
container_pesquisar_livros.configure(background="#F2F2F2")

lbl_pesquisa_titulo = tk.Label(container_pesquisar_livros,text="Título:") # Cria o texto "Nome" ao lado da caixa de pesquisa
lbl_pesquisa_titulo.pack(side=tk.LEFT)
lbl_pesquisa_titulo.configure(background="#F2F2F2")

txt_pesquisa_titulo = tk.Entry(container_pesquisar_livros) # Cria a caixa de texto nome
txt_pesquisa_titulo.pack(padx=10,pady=5,side=tk.LEFT)

lbl_pesquisa_autor = tk.Label(container_pesquisar_livros,text="Autor:") # Cria o texto "Nome" ao lado da caixa de pesquisa
lbl_pesquisa_autor.pack(side=tk.LEFT)
lbl_pesquisa_autor.configure(background="#F2F2F2")

txt_pesquisa_autor = tk.Entry(container_pesquisar_livros) # Cria a caixa de texto nome
txt_pesquisa_autor.pack(padx=10,pady=5,side=tk.LEFT)

lbl_pesquisa_ano = tk.Label(container_pesquisar_livros,text="Ano:") # Cria o texto "Nome" ao lado da caixa de pesquisa
lbl_pesquisa_ano.pack(side=tk.LEFT)
lbl_pesquisa_ano.configure(background="#F2F2F2")

txt_pesquisa_ano = tk.Entry(container_pesquisar_livros) # Cria a caixa de texto nome
txt_pesquisa_ano.pack(padx=10,pady=5,side=tk.LEFT)

btn_pesquisar_livro = tk.Button(quadro_pesquisar,text="Pesquisar",width=10,command=pesquisar_livro) # Cria o botão pesquisar e chama o método pesquisar_livro ao clicar
btn_pesquisar_livro.pack(padx=10,pady=2,side=tk.LEFT)
btn_pesquisar_livro.configure(background="#4682B4",foreground="#F8F8FF",border=0)

btn_restaurar_livro = tk.Button(quadro_pesquisar,text="Restaurar tabela",width=15,command=popular_livros) # Cria o botão restarar e chama o método popular_livros ao clicar
btn_restaurar_livro.pack(padx=10,pady=2,side=tk.LEFT)
btn_restaurar_livro.configure(background="#4682B4",foreground="#F8F8FF",border=0)

# Inicia a definição dos componentes do quadro para retirar e devolver livros____________________________________________

quadro_emprestar = tk.LabelFrame(quadro_livros,text='Retirar/Devolver')
quadro_emprestar.pack(fill="both",expand="yes",padx=8,pady=8,ipady=5)
quadro_emprestar.configure(background="#F2F2F2")

container_emprestar_livros = tk.Frame(quadro_emprestar,width=300)
container_emprestar_livros.pack(anchor=tk.W)
container_emprestar_livros.configure(background="#F2F2F2")

lbl_empresta_titulo = tk.Label(container_emprestar_livros,text="Título:") # Cria o texto "Nome" ao lado da caixa de pesquisa
lbl_empresta_titulo.pack(side=tk.LEFT)
lbl_empresta_titulo.configure(background="#F2F2F2")

txt_empresta_titulo = tk.Entry(container_emprestar_livros,width=30) # Cria a caixa de texto nome
txt_empresta_titulo.pack(padx=10,pady=5,side=tk.LEFT)

btn_verificar_livro = tk.Button(quadro_emprestar,text="Verificar disponibilidade",width=22,command=verificar_disponibilidade) # Cria o botão inserir
btn_verificar_livro.pack(padx=10,pady=2,side=tk.LEFT)
btn_verificar_livro.configure(background="#4682B4",foreground="#F8F8FF",border=0)

btn_emprestar_livro = tk.Button(quadro_emprestar,text="Retirar",width=10,command=emprestar_livro) # Cria o botão inserir
btn_emprestar_livro.pack(padx=10,pady=2,side=tk.LEFT)
btn_emprestar_livro.configure(background="#4682B4",foreground="#F8F8FF",border=0)

btn_emprestar_livro = tk.Button(quadro_emprestar,text="Devolver",width=10,command=devolver_livro) # Cria o botão inserir
btn_emprestar_livro.pack(padx=10,pady=2,side=tk.LEFT)
btn_emprestar_livro.configure(background="#4682B4",foreground="#F8F8FF",border=0)


app.mainloop() # Confirma a execução e apresenta na tela a janela app