# 🎬 Cinéphoria – Application Bureautique

Bienvenue dans **Cinéphoria Bureautique**, une application de bureau développée en Python avec Tkinter pour la gestion des incidents techniques dans les salles de cinéma.

Cette application est développée en Python en utilisant la bibliothèque Tkinter pour l'interface graphique. Ce document vous guidera à travers les étapes nécessaires pour lancer l'application en local sur votre machine.

## Prérequis

Avant de lancer l'application, assurez-vous d'avoir les éléments suivants installés :

1. **Python 3.x** : Vous pouvez télécharger la dernière version de Python depuis [python.org](https://www.python.org/downloads/).

2. **Bibliothèques Python** : Les bibliothèques nécessaires pour exécuter l'application doivent être installées. Si votre application utilise des bibliothèques supplémentaires autres que Tkinter, assurez-vous de les mentionner dans le fichier `requirements.txt` ou d'inclure des instructions pour les installer.

## Installation

1. **Clonez le dépôt** (si l'application est hébergée sur GitHub) :

   ```bash
   git clone https://github.com/abdoma-git/Cinephoria_bureautique.git
   cd votre-repository

---

## 📌 Présentation de l'application

Cinéphoria Bureautique est une interface conviviale permettant aux employés de :

- Se connecter via leur email et mot de passe,
- Sélectionner une salle de cinéma,
- Décrire un incident rencontré (ex: panne de projecteur, problème de son, etc.),
- Enregistrer l'incident dans une base de données MySQL,
- Visualiser la liste des incidents enregistrés pour chaque salle,
- Revenir à l’écran de connexion à tout moment.


<div style="display:flex; gap:20px;"> 
    <img width=350 src="Capture B1.png">
    <img width=350 src="Capture B2.png">
</div>

<br>

<div style="display:flex; gap:20px;">
    <img width=350 src="Capture B3.png">
    <img width=350 src="Capture B4.png">
</div>



---

## 🧩 Technologies utilisées

- 🐍 Python 3.x
- 🖼️ Tkinter (interface graphique)
- 🗃️ MySQL (base de données)
- 📦 PyInstaller (pour la génération du `.exe`)

---

## 📁 Contenu de l'application

L'application contient les fonctionnalités suivantes :

1. **Connexion sécurisée** à l’aide d’un identifiant (email) et mot de passe depuis la table `employer`.
2. Interface utilisateur propre et intuitive pour :
   - Sélectionner une salle depuis la table `salles`,
   - Enregistrer un incident technique (champ texte),
   - Visualiser les incidents liés à une salle,
   - Naviguer entre les fenêtres.

3. Stockage automatique des incidents dans une table `incidents` :
   - `salle` (id),
   - `description`,
   - `date_incident` (automatique).

---

## 🖥️ Téléchargement du fichier `.exe`

1 - Tu peux télécharger l'application prête à l'emploi ici :

🔗 [Cinéphoria_Bureau.exe](https://github.com/abdoma-git/Cinephoria_bureautique/blob/master/output/Cinephoria_Bureau)

2-  Double clique sur l'application :

<img src="https://github.com/abdoma-git/Cinephoria_bureautique/blob/master/application.png">
---

## ⚙️ Étapes d'installation sur Windows

### 📥 1. Télécharger l'exécutable

Clique sur le lien ci-dessus pour télécharger le fichier `Cinephoria.exe`.

> 💡 Remarque : Si une alerte de sécurité s'affiche (Windows Defender), clique sur **"Informations complémentaires"** puis sur **"Exécuter quand même"**.

---

### 📦 2. Configuration requise

- ✅ Windows 10 ou 11
- ✅ Python **non nécessaire** (inclus dans l'exécutable)
- ✅ Une base de données MySQL fonctionnelle avec la base **`cinephoria`**
  - Tables nécessaires : `employer`, `salles`, `incidents`

---

### 🛠️ 3. Préparation de la base de données

Assure-toi que la base **`cinephoria`** est bien installée et contient au minimum :

```sql
CREATE TABLE employer (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255),
    mot_de_passe VARCHAR(255)
);

CREATE TABLE salles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nbr_places INT,
    qualite_projection VARCHAR(255),
    cinema_id INT
);

CREATE TABLE incidents (
    id INT PRIMARY KEY AUTO_INCREMENT,
    salle VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    date_incident VARCHAR(255) NOT NULL
);
