import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import mysql.connector

# === Connexion à MySQL ===
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cinephoria"
    )

# === Fonction de connexion ===
def login():
    email = entry_email.get()
    password = entry_password.get()

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM employer WHERE email = %s AND mot_de_passe = %s"
        cursor.execute(query, (email, password))
        result = cursor.fetchone()

        if result:
            root.destroy()
            ouvrir_app()
        else:
            messagebox.showerror("Erreur", "Email ou mot de passe incorrect.")
    except mysql.connector.Error as err:
        messagebox.showerror("Erreur", f"Erreur de base de données : {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# === Application principale ===
def ouvrir_app():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Création de la table incidents si elle n'existe pas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INT AUTO_INCREMENT PRIMARY KEY,
            salle VARCHAR(255) NOT NULL,
            description TEXT NOT NULL,
            date_incident VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()

    # Récupération dynamique des salles
    cursor.execute("SELECT id FROM salles")
    salles = [row[0] for row in cursor.fetchall()]

    # === Fonctions internes ===
    def enregistrer_incident():
        salle = salle_combobox.get()
        description = incident_entry.get("1.0", tk.END).strip()
        date_incident = datetime.now().strftime("%d/%m/%Y %H:%M")

        if not salle:
            messagebox.showwarning("Erreur", "Veuillez sélectionner une salle.")
            return
        if not description:
            messagebox.showwarning("Erreur", "Veuillez entrer une description.")
            return

        cursor.execute(
            "INSERT INTO incidents (salle, description, date_incident) VALUES (%s, %s, %s)",
            (salle, description, date_incident)
        )
        conn.commit()

        messagebox.showinfo("Succès", "Incident enregistré avec succès.")
        incident_entry.delete("1.0", tk.END)
        afficher_incidents()

    def afficher_incidents():
        salle = salle_combobox.get()
        incident_listbox.delete(0, tk.END)

        if salle:
            cursor.execute(
                "SELECT description, date_incident FROM incidents WHERE salle = %s",
                (salle,)
            )
            resultats = cursor.fetchall()
            for desc, date in resultats:
                incident_listbox.insert(tk.END, f"- {desc} ({date})")

    def retour_login():
        fenetre.destroy()
        main_connexion()

    # === Interface graphique ===
    fenetre = tk.Tk()
    fenetre.title("Application Bureautique - Incidents")
    fenetre.geometry("600x550")
    fenetre.configure(bg="#f0f4f8")

    tk.Label(fenetre, text="Gestion des Incidents", font=("Helvetica", 20, "bold"), bg="#f0f4f8", fg="#003366").pack(pady=15)

    frame_selection = tk.Frame(fenetre, bg="#f0f4f8")
    frame_selection.pack(pady=10)

    tk.Label(frame_selection, text="Salle :", font=("Helvetica", 12), bg="#f0f4f8").grid(row=0, column=0, padx=5)
    salle_combobox = ttk.Combobox(frame_selection, values=salles, state="readonly", width=20)
    salle_combobox.grid(row=0, column=1)
    salle_combobox.bind("<<ComboboxSelected>>", lambda e: afficher_incidents())

    frame_incident = tk.Frame(fenetre, bg="#f0f4f8")
    frame_incident.pack(pady=10)

    tk.Label(frame_incident, text="Décrire l'incident :", font=("Helvetica", 12), bg="#f0f4f8").pack(anchor="w")
    incident_entry = tk.Text(frame_incident, height=4, width=60, font=("Helvetica", 10))
    incident_entry.pack()

    tk.Button(fenetre, text="Enregistrer l'incident", font=("Helvetica", 12), bg="#0066cc", fg="white", command=enregistrer_incident).pack(pady=10)

    frame_liste = tk.Frame(fenetre, bg="#f0f4f8")
    frame_liste.pack(pady=10)

    tk.Label(frame_liste, text="Incidents enregistrés :", font=("Helvetica", 12, "bold"), bg="#f0f4f8").pack(anchor="w")
    incident_listbox = tk.Listbox(frame_liste, width=80, height=10, font=("Helvetica", 10))
    incident_listbox.pack()

    tk.Button(fenetre, text="← Retour à la connexion", font=("Helvetica", 10), bg="#cccccc", command=retour_login).pack(pady=15)

    fenetre.mainloop()


# === Fenêtre de connexion ===
def main_connexion():
    global root, entry_email, entry_password
    root = tk.Tk()
    root.title("Connexion")
    root.geometry("300x200")

    tk.Label(root, text="Email").pack()
    entry_email = tk.Entry(root)
    entry_email.pack()

    tk.Label(root, text="Mot de passe").pack()
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    tk.Button(root, text="Se connecter", command=login).pack(pady=10)

    root.mainloop()

# Lancer l'application
main_connexion()
