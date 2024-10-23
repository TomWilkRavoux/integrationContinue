import csv 
import markdown
from jinja2 import Template
import os 


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
        'actualites_html': actualites_html,
        'actualites': actualites
    }
    generate_page('templates/index_template.html', 'output/index.html', context)

# Génération de la page des membres du bureau
def generate_membres(csv_file):
    membres = read_csv(csv_file)
    
    context = {
        'membres': membres
    }
    
    generate_page('templates/membres_template.html', 'output/membres.html', context)

# Génération de la page de détail d'une actualité
def generate_actualite(md_file):
    actualite_html = md_to_html(md_file)
    
    context = {
        'actualite_html': actualite_html
    }
    
    generate_page('templates/actualite_template.html', 'output/actualite.html', context)

if __name__ == "__main__":
    # Chemins vers les fichiers Markdown et CSV
    md_file = './asset/2025-01-18-evenement-1.md'
    csv_file = './asset/membres-bureau-association.csv'
    membres_csv = './asset/membres-bureau-association.csv'
    
    # Génération des pages
    generate_index(md_file, csv_file)
    generate_membres(membres_csv)
    generate_actualite(md_file)