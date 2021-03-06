import os
import psycopg2

conn = psycopg2.connect(
    user="postgres",
    password="0349",
    host="127.0.0.1",
    port="3333",
    database="empdb")


# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table



cur.execute('DROP TABLE IF EXISTS ONIBUS CASCADE;')
cur.execute('CREATE TABLE ONIBUS('
    'placa VARCHAR(8),'
    'chassi VARCHAR(17) NOT NULL,'	
    'id SERIAL NOT NULL,' 
    'disponibilidade BOOLEAN DEFAULT TRUE,'		
    'ano INT,'	
    'modelo VARCHAR(15) ,'	
    'data_compra DATE NOT NULL,	'
    'eficiencia NUMERIC,'
    'valor_compra decimal CHECK' 
        '(Valor_compra > 0) NOT NULL,'
    'PRIMARY KEY (placa)'
');')

cur.execute('INSERT INTO ONIBUS (placa, chassi, modelo, ano, data_compra,valor_compra,eficiencia)'
            'VALUES (%s, %s, %s, %s, %s, %s, %s)',
            ('ABC1234',
             '12345678912345678',
             'Mercedes',
             2010,
             '2020-10-10',
             33000.00,
             15)
            )
cur.execute('INSERT INTO ONIBUS (placa, chassi, modelo, ano, data_compra,valor_compra,eficiencia)'
            'VALUES (%s, %s, %s, %s, %s, %s, %s)',
            ('DEF1234',
             '00000678912345678',
             'Volvo',
             2015,
             '2021-10-10',
             50000.00,
             12)
            )
cur.execute('INSERT INTO ONIBUS (placa, chassi, modelo, ano, data_compra,valor_compra,eficiencia)'
            'VALUES (%s, %s, %s, %s, %s, %s, %s)',
            ('GHI3333',
             '98765432112345678',
             'Mercedes',
             2005,
             '2010-11-1',
             25000.00,
             9)
            )

cur.execute('INSERT INTO ONIBUS (placa, chassi, modelo, ano, data_compra,valor_compra,eficiencia)'
            'VALUES (%s, %s, %s, %s, %s, %s, %s)',
            ('KKK0000',
             '11111111912345678',
             'Volvo',
             2020,
             '2021-2-10',
             97000.00,
             19)
            )


cur.execute('DROP TABLE IF EXISTS MANUTENCAO;')
cur.execute('CREATE TABLE MANUTENCAO('
 	'ordem_servico SERIAL,'
 	'motivo TEXT NULL,'
 	'descricao_servico TEXT NULL,'
 	'valor NUMERIC NULL,'
 	'data_entrada DATE NOT NULL,'
 	'data_saida DATE NULL,'
 	'placa VARCHAR(7) NOT NULL, '
    'finalizado BOOLEAN DEFAULT FALSE,'

 	'PRIMARY KEY (ordem_servico),'
 	'FOREIGN KEY (placa) REFERENCES ONIBUS(placa)'
 		'ON DELETE CASCADE ON UPDATE CASCADE,'
 	'CHECK (valor > 0)'
 ');'
)


cur.execute('DROP TABLE IF EXISTS LINHA CASCADE;')
cur.execute('CREATE TABLE LINHA('	
 	'lcodigo SERIAL,'
 	'nome VARCHAR(25) NOT NULL,'
 	'destino VARCHAR(25) NOT NULL,'
 	'saida VARCHAR(25) NOT NULL,'

 	'PRIMARY KEY (lcodigo)	'
 ');'
)


cur.execute('INSERT INTO linha (nome,destino,saida)'
              'VALUES (%s, %s, %s)',
        (   'RODOVIARIA',             
            'CENTRO EDUCACIONAL',
            'RODOVIARIA',
        )
)

cur.execute('INSERT INTO linha (nome,destino,saida)'
              'VALUES (%s, %s, %s)',
        (   'HOSPITAL',             
            'ARCELOR',
            'MARTMINAS',
        )
)

cur.execute('INSERT INTO linha (nome,destino,saida)'
              'VALUES (%s, %s, %s)',
        (   'UFOP',             
            'SANTA BARBARA',
            'SANTA CECILIA',
        )
)


cur.execute('DROP TABLE IF EXISTS MOTORISTA CASCADE;')
cur.execute('CREATE TABLE MOTORISTA('	
 	'cpf VARCHAR( 14),'
 	'nome VARCHAR(30),'
 	'cnh VARCHAR(12) NOT NULL,'
 	'lCodigo INT,'
 	'PRIMARY KEY (cpf),'
 	'FOREIGN KEY (lCodigo) REFERENCES LINHA(lCodigo)'
 	'ON DELETE SET NULL	ON UPDATE SET NULL'
 ');'
)


cur.execute('INSERT INTO motorista (cpf,nome,cnh)'
              'VALUES (%s, %s, %s)',
        (   '111.222.333-00',             
            'Jo??o',
            111222333444,
        )
)


cur.execute('INSERT INTO motorista (cpf,nome,cnh)'
              'VALUES (%s, %s, %s)',
        (   '444.555.666-77',             
            'Alexsander',
            444555666777,
        )
)

cur.execute('DROP TABLE IF EXISTS intinerario1 CASCADE;')
cur.execute('CREATE TABLE INTINERARIO1('
 	'lcodigo INT NOT NULL,'
        'km NUMERIC ,'
	'placa VARCHAR(8),'
        'hora_partida time,'
 	
         'PRIMARY KEY (lcodigo, hora_partida),'
	
	'FOREIGN KEY (placa) REFERENCES ONIBUS(placa)'
		'ON DELETE cascade ON UPDATE CASCADE,'
 	'FOREIGN KEY (lcodigo) REFERENCES LINHA(lcodigo)'
 	'	ON DELETE cascade ON UPDATE CASCADE'
	
 ');'
 )

# cur.execute('insert into intinerario1(lcodigo,km)'
#         'values(%s,%s)',
#         (   1,
#             15.5,
#         )
# )

# cur.execute('insert into intinerario1(lcodigo,km)'
#         'values(%s,%s)',
#         (   1,
#         10,
#         )
# )
# cur.execute('insert into intinerario1(lcodigo,km)'
#         'values(%s,%s)',
#         (   1,
#         7,
#         )
# )

# cur.execute('insert into intinerario1(lcodigo,km)'
#         'values(%s,%s)',
#         (   2,
#         8,
#         )
# )
# cur.execute('insert into intinerario1(lcodigo,km)'
#         'values(%s,%s)',
#         (   2,
#         10,
#         )
# )

# cur.execute('insert into intinerario1(lcodigo,km)'
#         'values(%s,%s)',
#         (   3,
#         11,
#         )
# )


cur.execute('DROP TABLE IF EXISTS PONTO CASCADE;')
cur.execute('CREATE TABLE PONTO('
	'pcodigo SERIAL,'
	'rua VARCHAR(35) NOT NULL,'
	'bairro VARCHAR(25) NOT NULL,'
	'numero INT NOT NULL,'
	
	'PRIMARY KEY (pcodigo)'
');'
)

# cur.execute('insert into ponto( rua,bairro,numero)' 
# 'values(%s,%s,%s)',('Wilson Avarenga','Carneirinhos', 10,))

# cur.execute('insert into ponto( rua,bairro,numero)' 
# 'values(%s,%s,%s)',('Wilson Avarenga','Carneirinhos', 50,))

# cur.execute('insert into ponto( rua,bairro,numero)' 
# 'values(%s,%s,%s)',('Wilson Avarenga','Carneirinhos', 100,))

# cur.execute('insert into ponto( rua,bairro,numero)' 
# 'values(%s,%s,%s)',('Wilson Avarenga','Carneirinhos', 150,))

# cur.execute('insert into ponto( rua,bairro,numero)' 
# 'values(%s,%s,%s)',('Wilson Avarenga','Carneirinhos', 200,))

# cur.execute('insert into ponto( rua,bairro,numero)' 
# 'values(%s,%s,%s)',('Wilson Avarenga','Carneirinhos', 250,))

# cur.execute('insert into ponto( rua,bairro,numero)' 
# 'values(%s,%s,%s)',('Wilson Avarenga','Carneirinhos', 500,))

# cur.execute('insert into ponto( rua,bairro,numero)' 
# 'values(%s,%s,%s)',('Av. Candido Dias','Belmonte', 50,))


# cur.execute('insert into ponto( rua,bairro,numero)' 
# 'values(%s,%s,%s)',('Av. Candido Dias','Belmonte', 200,))

# cur.execute('insert into ponto( rua,bairro,numero)' 
# 'values(%s,%s,%s)',('Av. Candido Dias','Belmonte', 350,))

# cur.execute('insert into ponto( rua,bairro,numero)' 
# 'values(%s,%s,%s)',('Av. Candido Dias','Belmonte', 512,))



cur.execute('DROP TABLE IF EXISTS POSSUI_INT;')
cur.execute('CREATE TABLE POSSUI_INT('
	'lcodigo ,'
	'pcodigo INT NOT NULL,'
        'hora_partida'
	'ordem INT NOT NULL,'

	'PRIMARY KEY (nid,pcodigo),'
	
	'FOREIGN KEY (pcodigo) REFERENCES PONTO(pcodigo)'	
		'ON DELETE cascade ON UPDATE CASCADE,'
	'FOREIGN KEY (lcodigo) REFERENCES INTINERARIO1(lcodigo)'
		'ON DELETE cascade ON UPDATE CASCADE,'
	'FOREIGN KEY (hora_partida) REFERENCES INTINERARIO1(hora_partida)'
		'ON DELETE cascade ON UPDATE CASCADE'
')'
)




conn.commit()
cur.close()
conn.close()