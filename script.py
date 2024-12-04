import csv 
import markdown
from jinja2 import Template
import os 
import glob

# Définir le répertoire de sortie global
output_dir = "wwwroot"
os.makedirs(output_dir, exist_ok=True)  # Créer le répertoire s'il n'existe pas

#Lire un fichier .md et le convertir en html 
def md_to_html(md_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        text = f.read()
    return markdown.markdown(text)    

#Lire un fichier csv et retourne une liste de dico
def read_csv(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

# Générer une page html a partir d'un template et de donnée    
def generate_page(template_file, output_file, context):
    with open(template_file,  'r', encoding='utf-8') as f:
        template = Template(f.read())
    html_content = template.render(context)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content) 

#Génération de la homepage (avec actualité)
def generate_index(md_file, csv_file):
    actualites_html = md_to_html(md_file)
    actualites = read_csv(csv_file)

    context = {
        'actualite_html': actualites_html,
        'actualites': actualites
    }
    generate_page('templates/index_template.html', 'output/index.html', context)

# Générer la page des membres du bureau avec image
def generate_membres(csv_file):
    membres = read_csv(csv_file)
    
    # Context pour les membres
    context = {
        'membres': membres
    }
    
    # Générer la page HTML des membres
    generate_page('templates/membres_template.html', 'output/membres.html', context)
    print(f"Généré : output/membres.html")


# Génération de la page de détail d'une actualité
def generate_actualite(md_file):
    actualite_html = md_to_html(md_file)
    
    context = {
        'actualite_html': actualite_html
    }
    
    generate_page('templates/actualites_template.html', 'output/actualite.html', context)

# Fonction pour générer les pages d'actualité pour chaque fichier Markdown trouvé
def generate_all_actualites(md_directory):
    # Utiliser glob pour récupérer tous les fichiers .md dans le répertoire spécifié
    md_files = glob.glob(os.path.join(md_directory, '*.md'))
    
    # Parcourir chaque fichier Markdown
    for md_file in md_files:
        actualite_html = md_to_html(md_file)  # Convertir le fichier .md en HTML
        
        # Extraire un nom de fichier sans l'extension pour la sortie
        output_filename = os.path.basename(md_file).replace('.md', '.html')
        
        context = {
            'actualite_html': actualite_html
        }
        
        # Générer une page HTML pour chaque actualité
        generate_page('templates/actualites_template.html', f'output/{output_filename}', context)
        print(f"Généré : output/{output_filename}")

# Génération de la page des événements listant chaque actualité 
def generate_actualites_list(md_directory):
    md_files = glob.glob(os.path.join(md_directory, '*.md'))
    actualites = []

    for md_file in md_files:
        # Extraire le nom de l'événement à partir du fichier Markdown (on part du principe que le nom du fichier inclut une date et un titre)
        filename = os.path.basename(md_file)
        title = filename.replace('-', ' ').replace('.md', '').capitalize()
        
        # Créer un lien vers le fichier HTML correspondant
        link = filename.replace('.md', '.html')
        
        # Ajouter les informations sur l'événement dans la liste
        actualites.append({
            'title': title,
            'link': link
        })

    # Générer la page HTML à partir d'un template
    context = {
        'actualites': actualites
    }
    
    generate_page('templates/actualites_list_template.html', 'output/actualites.html', context)
    print(f"Généré : output/actualites.html")


if __name__ == "__main__":
    # Chemins vers les répertoires de fichiers Markdown et CSV
    md_directory = './asset'  # Répertoire contenant les fichiers .md
    membres_csv = './asset/membres-bureau-association.csv'
    

    
    generate_index(os.path.join(md_directory, '2025-01-18-evenement-1.md'), membres_csv)
    generate_membres(membres_csv)
    generate_all_actualites(md_directory)  # Traiter tous les fichiers .md
    generate_actualites_list(md_directory)