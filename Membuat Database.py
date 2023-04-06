#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector 

# menghubungkan mysql
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

# Create a cursor object
cursorObject = dataBase.cursor()

# membuat database dengan nama d3_ti_2023
cursorObject.execute("CREATE DATABASE d3_ti_2023")


# In[8]:


import mysql.connector 

# Hubungkan ke database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="d3_ti_2023"
)

# 
cursorObject = dataBase.cursor()

# Buat Table Mahasiswa
cursorObject.execute("CREATE TABLE mahasiswa (    NIM VARCHAR(10) PRIMARY KEY,     Nama VARCHAR(30),     Alamat VARCHAR(255),     Matkul VARCHAR(10),     Jenis_Kelamin VARCHAR(50) )")

# Buat Table Dosen
cursorObject.execute("CREATE TABLE dosen (    NIP VARCHAR(20) PRIMARY KEY,     Nama_Dosen VARCHAR(50),     Matkul VARCHAR(50),     Jenis_Kelamin VARCHAR(50) )")

# Buat Table Matkul
cursorObject.execute("CREATE TABLE matakuliah (    Kode_Matkul VARCHAR(10) PRIMARY KEY,     Nama_Matkul VARCHAR(50),     Waktu DATE,     Ruangan VARCHAR(10),     SKS INT(1) )")

# Close the cursor and database connection
cursorObject.close()
dataBase.close()


# In[6]:


import mysql.connector 

# Hubungkan ke database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="d3_ti_2023"
)

cursorObject = dataBase.cursor()

#memasukkan data mahasiswa
sql = "INSERT INTO mahasiswa (NIM, Nama, Alamat, Matkul, Jenis_Kelamin) VALUES (%s, %s, %s, %s, %s)"
val = [
    ("V3922011", "Catur Yudha Prasetya", "Jl. Batanghari No.69", "PBO", "Laki - Laki"),
    ("V3922012", "Clariva Meydieta Widagdo", "Jl. Pahlawan No.45", "MIKRO", "Perempuan"),
    ("V3922013", "Chantika", "Jl. Kenangan No.1", "PSO", "Perempuan"),
    ("V3922014", "Muhammad Farhan", "Jl. jalanan No.420", "PEMWEB", "Laki - Laki"),
    ("V3922015", "Tirta air subanyu", "Jl. Panglima Sudirman No.13", "EVP", "Perempuan")
]

cursorObject.executemany(sql,val)

dataBase.commit()

cursorObject.close()
dataBase.close()


# In[10]:


import mysql.connector 

# Hubungkan ke database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="d3_ti_2023"
)

cursorObject = dataBase.cursor()

#memasukkan data mahasiswa
sql = "INSERT INTO dosen (NIP, Nama_Dosen, Matkul, Jenis_Kelamin) VALUES (%s, %s, %s, %s)"
val = [
    ("154238369", "Nabilla Diaz", "PBO", "Perempuan"),
    ("154239360", "Alim Mustain", "MIKRO", "Laki - Laki"),
    ("154239771", "Sri Handayani", "PSO", "Perempuan"),
    ("154239983", "Sumono", "PEMWEB", "Laki - Laki"),
    ("154232064", "Muhhammad Abidin", "EVP", "Laki - Laki")
]

cursorObject.executemany(sql,val)

dataBase.commit()

cursorObject.close()
dataBase.close()


# In[16]:


import mysql.connector 

# Hubungkan ke database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="d3_ti_2023"
)

cursorObject = dataBase.cursor()

#memasukkan data mahasiswa
sql = "INSERT INTO matakuliah (Kode_Matkul, Nama_Matkul, Waktu, Ruangan, SKS) VALUES (%s, %s, %s, %s, %s)"
val = [
    ("PBO", "Pemrograman Berorientasi Objek", "2022-07-13", "L2R2", "1"),
    ("MIKRO", "Mikro Kontroler ", "2022-07-14", "LAB MIKRO", "2"),
    ("PSO", "Praktik Sistem Operasi ", "2022-07-05", "L2R2", "2"),
    ("PEMWEB", "Pemrograman Web", "2022-07-19", "L2R3", "4"),
    ("EVP", "English for Vocational Purposes", "2022-07-23", "L2R3", "4")
]

cursorObject.executemany(sql,val)

dataBase.commit()

cursorObject.close()
dataBase.close()


# In[17]:


import mysql.connector 

# Connect to MySQL server
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="d3_ti_2023"
)

# Create a cursor object
cursorObject = dataBase.cursor()

# Execute the SELECT query
sql = "SELECT mahasiswa.NIM, mahasiswa.Nama, mataKuliah.Nama_Matkul, dosen.Nama_Dosen        FROM mahasiswa        JOIN mataKuliah ON mahasiswa.Matkul = mataKuliah.Kode_Matkul        JOIN Dosen ON MataKuliah.Kode_Matkul = Dosen.Matkul"

cursorObject.execute(sql)

# Fetch all the rows
result = cursorObject.fetchall()

# Print the result
for row in result:
    print("---------------------------")
    print("NIM             : ", row[0])
    print("NAMA            : ", row[1])
    print("MataKuliah      : ", row[2])
    print("Dosen Pengajar  : ", row[3])
    print("---------------------------")

# Close the cursor and database connection
cursorObject.close()
dataBase.close()


# In[ ]:




