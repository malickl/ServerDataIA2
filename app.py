from flask import Flask, request, render_template

app = Flask(__name__)

# Base de données de livres
books = [
   {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
   {"id": 2, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
   {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949},
   {"id": 4, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
   {"id": 5, "title": "A Promised Land", "author": "Barack Obama", "year": 2020}
]

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/search', methods=['GET'])
def search():

   autorFromSearch = request.args.get('author')
   exist = False
   # Recherche d'un livre via le nom de l'auteur
   for livre in books:
      # verification du nom de l'auteur
      if livre['author'] == autorFromSearch:
         exist = True
         return f'Livre : {livre["title"]}, Auteur : {livre["author"]}, Année : {livre["year"]}'

   if exist == False:
       return "Aucun livre trouvé!"


@app.route('/add_book', methods=['POST'])
def addBook():
     
   # Recuperation des paramètres
   titre = request.form.get('title')
   auteur = request.form.get('author')
   annee = request.form.get('year')

   books.append(
       {"id": len(books)+1, "title": titre, "author": auteur, "year": annee}
   )
     
   return f'titre: {titre} | auteur : {auteur} | annee : {annee}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)