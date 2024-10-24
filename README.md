## Prérequis

Pour installer les dépendances, exécute la commande suivante dans ton terminal à la racine du projet :


pip install -r requirements.txt

# Vivre aux Lilas - Générateur de Pages HTML


Ce projet génère un site web statique pour l'association "Vivre aux Lilas", qui inclut des pages pour les actualités, les membres du bureau, ainsi que des articles individuels basés sur des fichiers Markdown et CSV.

## Fonctionnalités

- Génération d'une page d'accueil avec un aperçu des actualités.
- Génération d'une page listant toutes les actualités.
- Création de pages d'articles individuels à partir de fichiers Markdown.
- Génération d'une page pour les membres du bureau avec photos et informations.
- Structure basée sur des templates HTML utilisant [Jinja2](https://jinja.palletsprojects.com/) pour le rendu des données.
- Utilisation de [Tailwind CSS](https://tailwindcss.com/) pour le style des pages.

## Structure du Projet

.
├── assets/
│   ├── membres-bureau-association.csv    # Fichier CSV contenant les membres du bureau de l'association
│   ├── 2025-01-18-evenement-1.md         # Exemple de fichier Markdown pour une actualité
│   ├── logo.png                          # Logo de l'association utilisé sur le site
├── templates/
│   ├── index_template.html               # Template HTML pour la page d'accueil
│   ├── actualites_template.html          # Template HTML pour les pages d'articles individuels
│   ├── actualites_list_template.html     # Template HTML pour la page listant toutes les actualités
│   ├── membres_template.html             # Template HTML pour la page des membres du bureau
├── output/
│   ├── index.html                        # Page d'accueil générée (contenu HTML)
│   ├── actualites.html                   # Page listant toutes les actualités générée
│   ├── actualite-1.html                  # Page générée pour un article spécifique
│   ├── membres.html                      # Page des membres du bureau générée
├── generate.py                           # Script principal pour générer toutes les pages HTML
└── README.md                             # Documentation du projet
└── requirements.txt                      #liste des dépendances à installer

