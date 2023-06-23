#!/usr/bin/python3
import sqlite3
import random
from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS

noms = ['Hameg', 'Zidelmal', 'El Kechai', 'Kechih']
prenoms = ['Said', 'Rayan', 'Amel', 'Sarah', 'yacine']

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS utilisateurs(nom TEXT, prenom TEXT, date_naissance TEXT)')
conn.commit()
conn.close()

app = Flask(__name__)
CORS(app)


@app.route('/<nb_rows>')
def index(nb_rows):
    sqlw(nb_rows)
    return jsonify({"message": "Requête effectuée avec succès"})


def sqlw(rows):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    for _ in range(int(rows)):
        nom = random.choice(noms)
        prenom = random.choice(prenoms)
        date_naissance = random_date(1995, 2022)  
        cur.execute('INSERT INTO utilisateurs VALUES(?, ?, ?)', (nom, prenom, date_naissance))
    conn.commit()
    conn.close()
    return 'ok', 200


@app.route('/select')
def sqlr():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT nom, prenom, date_naissance FROM utilisateurs")
    rows = cur.fetchall()
    utilisateurs = []
    for row in rows:
        nom, prenom, date_naissance = row
        age = calculate_age(date_naissance)
        utilisateur = {"nom": nom, "prenom": prenom, "date_naissance": date_naissance, "age": age}
        utilisateurs.append(utilisateur)
    conn.close()
    return jsonify({"utilisateurs": utilisateurs})


def random_date(start_year, end_year):
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  
    date = datetime(year, month, day)
    return date.strftime('%Y-%m-%d')


def calculate_age(date_naissance):
    birth_date = datetime.strptime(date_naissance, '%Y-%m-%d')
    current_date = datetime.now()
    age = current_date.year - birth_date.year
    if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
        age -= 1
    return age

@app.route('/clear', methods=['DELETE'])
def clear_database():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM utilisateurs')
    conn.commit()
    conn.close()
    return 'Database cleared', 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8800)
