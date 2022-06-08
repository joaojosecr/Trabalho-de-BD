# py-3  -m venv venv
# .\venv\Scripts\activate
# caso não tenha instalado pip install flask
# $env:FLASK_APP="bdbus"

#caso queria criar novamente as tabelas script em python -m init_db

import os
from pickle import TRUE
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

def get_db_connection():
    conn =  psycopg2.connect(
    user="postgres",
    password="0349",
    host="127.0.0.1",
    port="3333",
    database="bdbus")
    return conn


@app.route('/')
def index():
    
    return render_template('index.html')



# @app.route('/create/', methods=('GET', 'POST'))
# def create():
#     if request.method == 'POST':
#         title = request.form['title']
#         author = request.form['author']
#         pages_num = int(request.form['pages_num'])
#         review = request.form['review']

#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute('INSERT INTO books (title, author, pages_num, review)'
#                     'VALUES (%s, %s, %s, %s)',
#                     (title, author, pages_num, review))
#         conn.commit()
#         cur.close()
#         conn.close()
#         return redirect(url_for('index'))

#     return render_template('create.html')




#   ONIBUS
@app.route('/onibus/')
def onibus():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM onibus;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('onibus/onibus.html', books=books)

@app.route('/cadastraonibus/',methods=('GET', 'POST'))
def cadastraonibus():
    if request.method == 'POST':
        placa = request.form['placa']
        chassi = request.form['chassi']
        ano=request.form['ano']
        modelo= request.form['modelo']
        data_compra=request.form['data_compra']
        valor_compra=request.form['valor_compra']
        eficiencia=request.form['eficiencia']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO onibus (placa, chassi, ano, modelo, data_compra, valor_compra,eficiencia)'
                    'VALUES (%s, %s, %s,%s, %s, %s,%s)',
                    (placa, chassi, ano, modelo, data_compra, valor_compra,eficiencia))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('onibus'))
    return render_template('onibus/cadastraonibus.html')

@app.route('/attonibus/',methods=('GET', 'POST'))
def attonibus():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM onibus')
    placa = cur.fetchall()

    if request.method == 'POST':
        placa = request.form['placa']
        ano=request.form['ano']
        modelo= request.form['modelo']
        data_compra=request.form['data_compra']
        valor_compra=request.form['valor_compra']
        eficiencia=request.form['eficiencia']
        if ano != '':
            cur.execute('UPDATE onibus SET ano = %s WHERE placa=%s', (ano,placa,))
        if modelo != '':
            cur.execute('UPDATE onibus SET modelo = %s WHERE placa=%s', (modelo,placa,))
        if valor_compra != '':
            cur.execute('UPDATE onibus SET valor_compra = %s WHERE placa=%s', (valor_compra,placa,))
        if eficiencia != '':
            cur.execute('UPDATE onibus SET eficiencia = %s WHERE placa=%s', (eficiencia,placa,))
        if data_compra != '':
            cur.execute('UPDATE onibus SET data_compra = %s WHERE placa=%s', (data_compra,placa,))
        

        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('attmotoristas'))

    conn.commit()
    cur.close()
    conn.close()
    return render_template('onibus/attonibus.html',placa=placa)


@app.route('/removeronibus/',methods=('GET', 'POST'))
def removeonibus():
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM onibus')
    placa = cur.fetchall()


    if request.method == 'POST':
        placadel=request.form['placadel']
        print(placadel)
        
        cur.execute('DELETE FROM onibus WHERE placa = %s', (placadel,))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('onibus'))

    conn.commit()
    cur.close()
    conn.close()
    return render_template('onibus/removeronibus.html',placa=placa)



# INTINERARIO 2

@app.route('/intinerario2/')
def intinerario2():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM intinerario2 natural join onibus;')
    books = cur.fetchall()
    print(books)
    cur.close()
    conn.close()
    return render_template('intinerario2/intinerario2.html', books=books)

@app.route('/cadastraintinerario2/',methods=('GET', 'POST'))
def cadastraintinerario2():
    if request.method == 'POST':
        placa = request.form['placa']
        chassi = request.form['chassi']
        ano=request.form['ano']
        modelo= request.form['modelo']
        data_compra=request.form['data_compra']
        valor_compra=request.form['valor_compra']
        eficiencia=request.form['eficiencia']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO onibus (placa, chassi, ano, modelo, data_compra, valor_compra,eficiencia)'
                    'VALUES (%s, %s, %s,%s, %s, %s,%s)',
                    (placa, chassi, ano, modelo, data_compra, valor_compra,eficiencia))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('intinerario1'))
    return render_template('intinerario1/cadastraintinerario1.html')

@app.route('/attintinerario2/',methods=('GET', 'POST'))
def attintinerario2():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM onibus')
    placa = cur.fetchall()

    if request.method == 'POST':
        placa = request.form['placa']
        ano=request.form['ano']
        modelo= request.form['modelo']
        data_compra=request.form['data_compra']
        valor_compra=request.form['valor_compra']
        eficiencia=request.form['eficiencia']
        if ano != '':
            cur.execute('UPDATE onibus SET ano = %s WHERE placa=%s', (ano,placa,))
        if modelo != '':
            cur.execute('UPDATE onibus SET modelo = %s WHERE placa=%s', (modelo,placa,))
        if valor_compra != '':
            cur.execute('UPDATE onibus SET valor_compra = %s WHERE placa=%s', (valor_compra,placa,))
        if eficiencia != '':
            cur.execute('UPDATE onibus SET eficiencia = %s WHERE placa=%s', (eficiencia,placa,))
        if data_compra != '':
            cur.execute('UPDATE onibus SET data_compra = %s WHERE placa=%s', (data_compra,placa,))
        

        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('attmotoristas'))

    conn.commit()
    cur.close()
    conn.close()
    return render_template('intinerario1/attintinerario1.html',placa=placa)

@app.route('/removerintinerario2/',methods=('GET', 'POST'))
def removeintinerario2():
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM onibus')
    placa = cur.fetchall()


    if request.method == 'POST':
        placadel=request.form['placadel']
        print(placadel)
        cur.execute('DELETE FROM onibus WHERE placa = %s', (placadel,))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('intinerario2'))

    conn.commit()
    cur.close()
    conn.close()
    return render_template('intinerario2/removerintinerario2.html',placa=placa)

# INTINERARIO 1

@app.route('/intinerario1/',methods=('GET', 'POST'))
def intinerario1():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('select * from intinerario1 natural join linha')
    books = cur.fetchall()
    cur.close()
    conn.close()

    if request.method == 'POST':
        nid=request.form['nid']
        print(nid)
        return intinerario2(nid)
        #return redirect(url_for('intinerario2'))

    return render_template('intinerario1/intinerario1.html', books=books)

@app.route('/cadastraintinerario1/',methods=('GET', 'POST'))
def cadastraintinerario1():
    if request.method == 'POST':
        placa = request.form['placa']
        chassi = request.form['chassi']
        ano=request.form['ano']
        modelo= request.form['modelo']
        data_compra=request.form['data_compra']
        valor_compra=request.form['valor_compra']
        eficiencia=request.form['eficiencia']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO onibus (placa, chassi, ano, modelo, data_compra, valor_compra,eficiencia)'
                    'VALUES (%s, %s, %s,%s, %s, %s,%s)',
                    (placa, chassi, ano, modelo, data_compra, valor_compra,eficiencia))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('intinerario1'))
    return render_template('intinerario1/cadastraintinerario1.html')

@app.route('/attintinerario1/',methods=('GET', 'POST'))
def attintinerario1():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM onibus')
    placa = cur.fetchall()

    if request.method == 'POST':
        placa = request.form['placa']
        ano=request.form['ano']
        modelo= request.form['modelo']
        data_compra=request.form['data_compra']
        valor_compra=request.form['valor_compra']
        eficiencia=request.form['eficiencia']
        if ano != '':
            cur.execute('UPDATE onibus SET ano = %s WHERE placa=%s', (ano,placa,))
        if modelo != '':
            cur.execute('UPDATE onibus SET modelo = %s WHERE placa=%s', (modelo,placa,))
        if valor_compra != '':
            cur.execute('UPDATE onibus SET valor_compra = %s WHERE placa=%s', (valor_compra,placa,))
        if eficiencia != '':
            cur.execute('UPDATE onibus SET eficiencia = %s WHERE placa=%s', (eficiencia,placa,))
        if data_compra != '':
            cur.execute('UPDATE onibus SET data_compra = %s WHERE placa=%s', (data_compra,placa,))
        

        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('attmotoristas'))

    conn.commit()
    cur.close()
    conn.close()
    return render_template('intinerario1/attintinerario1.html',placa=placa)

@app.route('/removerintinerario1/',methods=('GET', 'POST'))
def removeintinerario1():
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM onibus')
    placa = cur.fetchall()


    if request.method == 'POST':
        placadel=request.form['placadel']
        print(placadel)
        cur.execute('DELETE FROM onibus WHERE placa = %s', (placadel,))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('intinerario1'))

    conn.commit()
    cur.close()
    conn.close()
    return render_template('intinerario1/removerintinerario1.html',placa=placa)




#   LINHA
@app.route('/linha/')
def linha():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM linha;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('linha/linha.html', books=books)

@app.route('/cadastralinha/',methods=('GET', 'POST'))
def cadastralinha():
    if request.method == 'POST':
        lcodigo = request.form['lcodigo']
        nome = request.form['nome']
        destino = request.form['destino']
        saida = request.form['saida']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO LINHA (lcodigo, nome, destino, saida)'
                    'VALUES (%s, %s, %s, %s)',
                    (lcodigo,nome,destino, saida))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('linha'))
    return render_template('linha/cadastralinha.html')

@app.route('/attlinha/',methods=('GET', 'POST'))
def attlinha():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM linha')
    cpf = cur.fetchall()
    cur.execute('SELECT * FROM LINHA')
    lcodigo= cur.fetchall()

    if request.method == 'POST':
        lcodigo = request.form['lcodigo']
        nome = request.form['nome']
        destino =request.form['destino']
        saida = request.form['saida']
        if nome != '':
            cur.execute('UPDATE linha SET nome = %s WHERE lcodigo=%s', (nome,lcodigo,))
        if destino != '':
            cur.execute('UPDATE linha SET destino = %s WHERE lcodigo=%s', (destino,lcodigo,))
        
        if saida != '':
            cur.execute('UPDATE linha SET saida = %s WHERE cpf=%s', (saida,lcodigo,))
        
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('attlinha'))

    conn.commit()
    cur.close()
    conn.close()
    return render_template('linha/attlinha.html',cpf=cpf,lcodigo=lcodigo)

@app.route('/descadastralinha/',methods=('GET', 'POST'))
def descadastralinha():
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM linha')
    lcodigo = cur.fetchall()


    if request.method == 'POST':
        linhadel=request.form['linhadel']
        print(linhadel)
        cur.execute('DELETE FROM linha WHERE lcodigo=%s', (linhadel,))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('linha'))

    conn.commit()
    cur.close()
    conn.close()
    return render_template('linha/descadastralinha.html',lcodigo=lcodigo)



#   MANUTENCAO
@app.route('/manutencao/',methods=('GET', 'POST'))
def manutencao():

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM manutencao natural join onibus;')
    bus = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('manutencoes/manutencao.html',bus=bus)

@app.route('/cadastramanutencoes/',methods=('GET', 'POST'))
def cadastramanutencoes():

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT placa FROM ONIBUS where disponibilidade=TRUE;')
    bus = cur.fetchall()
    
    if request.method == 'POST':
        motivo=request.form['motivo']
        data_entrada=request.form['data_entrada']
        placa=request.form['placa']
        
        cur.execute('INSERT INTO MANUTENCAO (motivo,data_entrada,placa)'
                'VALUES (%s, %s, %s)',
                (motivo,data_entrada,placa)
        )

        cur.execute('UPDATE ONIBUS SET disponibilidade=FALSE WHERE placa=%s',(placa,))
        conn.commit()
        return redirect(url_for('manutencao'))
    cur.close()
    conn.close()
    return render_template('manutencoes/cadastramanutencoes.html',bus=bus)

@app.route('/finalmanutencoes/',methods=('GET', 'POST'))
def finalmanutencoes():
    print("FINAL MANUTENCAAAOO")
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM manutencao where finalizado=FALSE')
    manut = cur.fetchall()
    print(manut)


    if request.method == 'POST':
        ords=request.form['ords']
        data_saida=request.form['data_saida']
        valor=request.form['valor']
        cur.execute('UPDATE MANUTENCAO SET valor = %s WHERE ordem_servico=%s', (valor ,ords,))   
        cur.execute('UPDATE MANUTENCAO SET finalizado = TRUE WHERE ordem_servico=%s', (ords,))   
        cur.execute('UPDATE MANUTENCAO SET data_saida = %s WHERE ordem_servico=%s', (data_saida ,ords,)) 

        #ajustar onibus
        cur.execute('SELECT placa FROM manutencao WHERE ordem_servico=%s',(ords,))
        placa = cur.fetchall()
        placaa=placa[0][0]
        print("\n\n\n", placa ,placaa, "\n\n\n")
        cur.execute('UPDATE ONIBUS SET disponibilidade = TRUE where placa = %s', (placa))
        
        
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('finalmanutencoes'))
    conn.commit()
    cur.close()
    conn.close()
    
    return render_template('manutencoes/finalmanutencao.html',manut=manut)

@app.route('/descmanutencao/',methods=('GET', 'POST'))
def descmanutencao():
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM manutencao')
    ords = cur.fetchall()


    if request.method == 'POST':
        ords=request.form['ords']
        

        
        #ajustar onibus
        cur.execute('SELECT placa FROM manutencao WHERE ordem_servico=%s',(ords,))
        placa = cur.fetchall()
        placaa=placa[0][0]
        print("\n\n\n", placa ,placaa, "\n\n\n")
        cur.execute('UPDATE ONIBUS SET disponibilidade = TRUE where placa = %s', (placa))
       

        cur.execute('DELETE FROM manutencao WHERE ordem_servico=%s', (ords,))

        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('descmanutencao'))

    conn.commit()
    cur.close()
    conn.close()
    return render_template('manutencoes/descmanutencao.html',ords=ords)




#   MOTORISTA
@app.route('/motoristas/')
def motoristas():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM motorista;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('motoristas/motoristas.html', books=books)

@app.route('/cadastramotoristas/',methods=('GET', 'POST'))
def cadastramotoristas():
    if request.method == 'POST':
        cpf = request.form['cpf']
        nome = request.form['nome']
        cnh= request.form['cnh']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO MOTORISTA (cpf, nome, cnh)'
                    'VALUES (%s, %s, %s)',
                    (cpf,nome,cnh))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('motoristas'))
    return render_template('motoristas/cadastramotoristas.html')

@app.route('/attmotoristas/',methods=('GET', 'POST'))
def attmotoristas():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM motorista')
    cpf = cur.fetchall()
    cur.execute('SELECT * FROM LINHA')
    lcodigo= cur.fetchall()

    if request.method == 'POST':
        cpfdel=request.form['cpfdel']
        nome=request.form['nome']
        cnh=request.form['cnh']
        lcodigo=request.form['lcodigo']
        if nome != '':
            cur.execute('UPDATE MOTORISTA SET nome = %s WHERE cpf=%s', (nome,cpfdel,))
        if cnh != '':
            cur.execute('UPDATE MOTORISTA SET cnh = %s WHERE cpf=%s', (cnh,cpfdel,))
        
        if lcodigo != '':
            cur.execute('UPDATE MOTORISTA SET lcodigo = %s WHERE cpf=%s', (lcodigo,cpfdel,))
        
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('attmotoristas'))

    conn.commit()
    cur.close()
    conn.close()
    return render_template('motoristas/attmotoristas.html',cpf=cpf,lcodigo=lcodigo)

@app.route('/descadastramotoristas/',methods=('GET', 'POST'))
def descadastramotoristas():
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM motorista')
    cpf = cur.fetchall()


    if request.method == 'POST':
        cpfdel=request.form['cpfdel']
        print(cpfdel)
        cur.execute('DELETE FROM MOTORISTA WHERE cpf=%s', (cpfdel,))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('motoristas'))

    conn.commit()
    cur.close()
    conn.close()
    return render_template('motoristas/descadastramotoristas.html',cpf=cpf)




#ponto
@app.route('/ponto/')
def ponto():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM ponto;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('ponto/ponto.html', books=books)

@app.route('/cadastraponto/',methods=('GET', 'POST'))
def cadastraponto():
       
    if request.method == 'POST':
        rua = request.form['rua']
        bairro= request.form['bairro']
        numero=request.form['numero']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO ponto (rua, bairro, numero)'
                    'VALUES (%s, %s, %s)',
                    (rua, bairro, numero))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('cadastraponto'))
    return render_template('ponto/cadastraponto.html')

@app.route('/attponto/',methods=('GET', 'POST'))
def attponto():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM ponto')
    ponto = cur.fetchall()
    
    
    if request.method == 'POST':
        pcodigo=request.form['pcodigo']
        rua = request.form['rua']
        bairro= request.form['bairro']
        numero=request.form['numero']
        if rua != '':
            cur.execute('UPDATE ponto SET rua = %s WHERE pcodigo=%s', (rua,pcodigo,))
        if bairro != '':
            cur.execute('UPDATE ponto SET bairro = %s WHERE pcodigo=%s', (bairro,pcodigo,))
        
        if numero != '':
            cur.execute('UPDATE ponto SET numero = %s WHERE pcodigo=%s', (numero,pcodigo,))
        
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('attponto'))

    conn.commit()
    cur.close()
    conn.close()
    return render_template('ponto/attponto.html',ponto=ponto)

@app.route('/descadastraponto/',methods=('GET', 'POST'))
def descadastraponto():
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM ponto')
    ponto = cur.fetchall()


    if request.method == 'POST':
        pcodigo=request.form['pcodigo']
        print(pcodigo)
        cur.execute('DELETE FROM ponto WHERE pcodigo=%s', (pcodigo,))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('ponto'))

    conn.commit()
    cur.close()
    conn.close()
    return render_template('ponto/descadastraponto.html',ponto=ponto)


#pi
@app.route('/pi/')
def pi():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM possui_int;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('pi/pi.html', books=books)

@app.route('/cadastrapi/',methods=('GET', 'POST'))
def cadastrapi():

    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute('SELECT nid FROM intinerario2;')
    nid = cur.fetchall()

    cur.execute('SELECT pcodigo FROM ponto;')
    pcodigo = cur.fetchall()
    
    if request.method == 'POST':
        nid=request.form['nid']
        pcodigo=request.form['pcodigo']
        ordem=request.form['ordem']
        
        try:
            cur.execute('INSERT INTO possui_int (nid,pcodigo,ordem)'
                    'VALUES (%s, %s, %s)',
                    (nid,pcodigo,ordem)
            )
        
            conn.commit()
            return redirect(url_for('possui_id'))
        except:
            cur.close()
            conn.close()
            return render_template('pi/cadastrapi.html')
     
    cur.close()
    conn.close()
    return render_template('pi/cadastrapi.html',nid=nid,pcodigo=pcodigo)

@app.route('/attpi/',methods=('GET', 'POST'))
def attpi():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM possui_int')
    pi = cur.fetchall()
    
    
    if request.method == 'POST':
        pcodigo=request.form['pcodigo']
        rua = request.form['rua']
        bairro= request.form['bairro']
        numero=request.form['numero']
        if rua != '':
            cur.execute('UPDATE possui_int SET rua = %s WHERE pcodigo=%s', (rua,pcodigo,))
        if bairro != '':
            cur.execute('UPDATE possui_int SET bairro = %s WHERE pcodigo=%s', (bairro,pcodigo,))
        
        if numero != '':
            cur.execute('UPDATE possui_int SET numero = %s WHERE pcodigo=%s', (numero,pcodigo,))
        
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('attpi'))

    conn.commit()
    cur.close()
    conn.close()
    return render_template('pi/attpi.html',pi=pi)

@app.route('/descadastrapi/',methods=('GET', 'POST'))
def descadastrapi():
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM possui_int')
    pi = cur.fetchall()


    if request.method == 'POST':
        pcodigo=request.form['pcodigo']
        print(pcodigo)
        cur.execute('DELETE FROM possui_int WHERE pcodigo=%s', (pcodigo,))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('pi'))

    conn.commit()
    cur.close()
    conn.close()
    return render_template('pi/descadastrapi.html',pi=pi)
