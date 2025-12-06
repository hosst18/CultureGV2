# 📚 CultureG Bot — Quiz de Culture Générale (Discord)

**CultureG Bot** est un bot Discord conçu pour proposer des quiz intelligents, amusants et évolutifs.  
Il combine :

- 🎓 **Culture générale sérieuse**
- 🎮 **Modes fun et compétitifs**
- 🧠 **Innovations uniques jamais vues sur Discord**

Ce bot est en développement continu et s'améliore progressivement.

---

# 🚀 Fonctionnalités actuelles (Version 1.0)

La version actuelle propose une base **solide, propre et extensible**.

## ✔️ Commandes hybrides (préfixe + slash)

Toutes les commandes fonctionnent en :

- `!commande`
- `/commande`

Grâce à `@commands.hybrid_command`.

---

## ✔️ `quiz` — Question simple

Le bot pose une question de CultureG :

- choix multiples  
- embed propre  
- anti-répétition  
- timer  
- score +1 si bonne réponse  

**Commandes :**  
`!quiz` ou `/quiz`

---

## ✔️ `profil` — Statistiques du joueur

Affiche :

- score total  
- avatar  
- stats persistantes  

**Commandes :**  
`!profil` ou `/profil`

---

## ✔️ `top` — Classement général

Affiche :

- top 10  
- médailles 🥇🥈🥉  
- classement propre  

**Commandes :**  
`!top` ou `/top`

---

## ✔️ Architecture professionnelle

cultureg/
│── bot.py
│── cogs/
│ ├── quiz.py
│ ├── profile.py
│ └── ranking.py
│── utils/
│ ├── question_manager.py
│ └── score_manager.py
│── data/
│ ├── questions.json
│ └── scores.json
│── config.py



---

# 🔧 Technologies utilisées

- Python 3.10+
- discord.py (version moderne)
- Hybrid Commands
- JSON pour stockage
- asyncio

---

# 🎯 Objectif du projet

Créer **le bot CultureG le plus complet, fun et intelligent de Discord**.

---

# 🧩 Roadmap — Fonctionnalités à venir

## 🟦 Version 1.5 — Modes fun & compétitifs

### 🔥 Mode Survie (`/survie`)
Tu joues jusqu’à te tromper.  
Objectif : faire la meilleure **streak**.

### 🔥 Mode Ascension (`/ascension`)
Difficulté progressive :  
facile → moyen → difficile → expert → impossible.

---

## 🟥 Version 2.0 — Innovations uniques

### ⭐ Mode Battle Royale (`/battle`)
Jusqu’à **100 joueurs** jouent en même temps.  
Chaque question élimine les mauvaises réponses.  
1 survivant = gagnant final.

### ⭐ Mode Conquête des Thèmes (`/conquete`)
Chaque thème a un **Roi**.  
Le serveur devient une **map stratégique**.

### ⭐ Mode Bluff (`/bluff`)
Chaque joueur invente une fausse réponse.  
Le bot mélange tout avec la vraie.

Points :
- +2 → trouver la vraie  
- +1 → quelqu’un tombe dans ta fausse réponse  

### ⭐ Mode Reverse (`/reverse`)
Le bot donne la réponse.  
Tu dois trouver la question correcte.

---

## 🟩 Version 3.0 — Intelligence & personnalisation

### 🎓 Entraînement personnalisé (`/entrainement`)
Le bot analyse tes faiblesses et te propose des exercices.

### 🧠 Stats avancées (`/stats`)
- taux de réussite  
- thèmes forts/faibles  
- progression  
- meilleur streak  

### 👑 Système de niveaux & rangs
Avec titres comme :  
*Débutant, Étudiant, Professeur, Légende…*

### 📅 Saisons mensuelles
Classement saisonnier + récompenses.

---

## 🛠 Version 4.0 — Niveau professionnel

### 🌐 Dashboard Web
Voir les stats et classements via une interface web.

### 🗃 Base SQL (SQLite / PostgreSQL)
Stockage robuste et scalable.

### 🔄 Import automatique des questions
Support des fichiers `.json`, `.csv`, etc.

---

# 🧑‍💻 Développement & Contributions

Le projet évolue progressivement.  
Chaque push ajoute une nouvelle fonctionnalité.

Contributions bienvenues :

- nouvelles questions  
- nouveaux modes  
- idées  
- corrections  

---

# 💡 Auteur

Développé par **Hossam**.  
Objectif : créer une **référence CultureG** sur Discord.

---

# 🎉 Merci d'utiliser CultureG Bot !

De nombreuses fonctionnalités arrivent bientôt 🚀🔥
