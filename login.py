import tkinter as tk
from tkinter import messagebox
import mysql.connector
import subprocess

def login():
    email = entry_email.get()
    password = entry_password.get()

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cinephoria"
        )
        cursor = conn.cursor()
        query = "SELECT * FROM employer WHERE email = %s AND mot_de_passe = %s"
        cursor.execute(query, (email, password))
        print("email ",email)
        print("mot de passe ",password)
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Succès", "Connexion réussie !")
            root.destroy()
            subprocess.run(["python", "app1.py"])
        else:
            messagebox.showerror("Erreur", "Email ou mot de passe incorrect.")
    except mysql.connector.Error as err:
        messagebox.showerror("Erreur", f"Erreur de base de données : {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Interface Tkinter
root = tk.Tk()
root.title("Connexion")
root.geometry("300x200")

label_email = tk.Label(root, text="Email")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

label_password = tk.Label(root, text="Mot de passe")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

btn_login = tk.Button(root, text="Se connecter", command=login)
btn_login.pack(pady=10)

root.mainloop()
