import csv
import markdown
from jinja2 import Template
import os
import glob

# Définir le répertoire de base et de sortie
base_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(base_dir)  # Change le répertoire de travail
output_dir = os.path.join(base_dir, 'wwwroot')
os.makedirs(output_dir, exist_ok=True)  # Créer le répertoire s'il n'existe pas

# Lire un fichier .md et le convertir en HTML
def md_to_html(md_file):
    if not os.path.exists(md_file):
        print(f"Erreur : Le fichier {md_file} est introuvable.")
        exit(1)
    with open(md_file, 'r', encoding='utf-8') as f:
        text = f.read()
    return markdown.markdown(text)

# Lire un fichier CSV et retourner une liste de dictionnaires
def read_csv(csv_file):
    if not os.path.exists(csv_file):
        print(f"Erreur : Le fichier {csv_file} est introuvable.")
        exit(1)
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

# Générer une page HTML à partir d'un template et de données
def generate_page(template_file, output_file, context):
    with open(template_file, 'r', encoding='utf-8') as f:
        template = Template(f.read())
    html_content = template.render(context)

    output_path = os.path.join(output_dir, output_file)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Créer les sous-dossiers nécessaires
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

# Génération de la homepage (avec actualité)
def generate_index(md_file, csv_file):
    actualites_html = md_to_html(md_file)
    actualites = read_csv(csv_file)

    context = {
        'actualite_html': actualites_html,
        'actualites': actualites
    }
    generate_page('templates/index_template.html', 'index.html', context)

# Générer la page des membres du bureau avec image
def generate_membres(csv_file):
    membres = read_csv(csv_file)
    context = {
        'membres': membres
    }
    generate_page('templates/membres_template.html', 'membres.html', context)
    print(f"Généré : {os.path.join(output_dir, 'membres.html')}")

# Génération de la page de détail d'une actualité
def generate_actualite(md_file):
    actualite_html = md_to_html(md_file)
    context = {
        'actualite_html': actualite_html
    }
    generate_page('templates/actualites_template.html', 'actualite.html', context)

# Fonction pour générer les pages d'actualité pour chaque fichier Markdown trouvé
def generate_all_actualites(md_directory):
    md_files = glob.glob(os.path.join(md_directory, '*.md'))
    for md_file in md_files:
        actualite_html = md_to_html(md_file)
        output_filename = os.path.basename(md_file).replace('.md', '.html')
        context = {
            'actualite_html': actualite_html
        }
        generate_page('templates/actualites_template.html', f'actualites/{output_filename}', context)
        print(f"Généré : {os.path.join(output_dir, f'actualites/{output_filename}')}")

# Génération de la page des événements listant chaque actualité
def generate_actualites_list(md_directory):
    md_files = glob.glob(os.path.join(md_directory, '*.md'))
    actualites = []

    for md_file in md_files:
        filename = os.path.basename(md_file)
        title = filename.replace('-', ' ').replace('.md', '').capitalize()
        link = f"actualites/{filename.replace('.md', '.html')}"
        actualites.append({
            'title': title,
            'link': link
        })

    context = {
        'actualites': actualites
    }
    generate_page('templates/actualites_list_template.html', 'actualites.html', context)
    print(f"Généré : {os.path.join(output_dir, 'actualites.html')}")

if __name__ == "__main__":
    # Chemins vers les répertoires de fichiers Markdown et CSV
    md_directory = './asset'  # Répertoire contenant les fichiers .md
    membres_csv = './asset/membres-bureau-association.csv'

    # Générer les différentes pages
    generate_index(os.path.join(md_directory, '2025-01-18-evenement-1.md'), membres_csv)
    generate_membres(membres_csv)
    generate_all_actualites(md_directory)
    generate_actualites_list(md_directory)
