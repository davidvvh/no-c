from flask import Flask, render_template
app = Flask(__name__)

pokedex = [
    {"id": 1, "nombre": "Bulbasaur", "tipo": "Planta/Veneno", "imagen": "Bulbasaur.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"}, #Datos de bulbasaur
    {"id": 2, "nombre": "Ivysaur", "tipo": "Planta/Veneno", "imagen": "Ivysaur.png", "poder": 60, "altura": "1.0m", "peso": "13.0kg"}, #Datos de ivysaur
    {"id": 3, "nombre": "Venusaur", "tipo": "Planta/Veneno", "imagen": "Venusaur.png", "poder": 80, "altura": "2.0m", "peso": "100.0kg"}, #Datos de venusaur
    {"id": 4, "nombre": "Charmander", "tipo": "Fuego", "imagen": "Charmander.png", "poder": 39, "altura": "0.6m", "peso": "8.5kg"}, #Datos de charmander
    {"id": 5, "nombre": "Charmeleon", "tipo": "Fuego", "imagen": "Charmeleon.png", "poder": 58, "altura": "1.1m", "peso": "19.0kg"}, #Datos de charmeleon
    {"id": 6, "nombre": "Charizard", "tipo": "Fuego/Volador", "imagen": "Charizard.png", "poder": 78, "altura": "1.7m", "peso": "90.5kg"}, #Datos de charizard
    {"id": 7, "nombre": "Squirtle", "tipo": "Agua", "imagen": "Squirtle.png", "poder": 44, "altura": "0.5m", "peso": "9.0kg"}, #Datos de squirtle
    {"id": 8, "nombre": "Wartortle", "tipo": "Agua", "imagen": "Wartortle.png", "poder": 59, "altura": "1.0m", "peso": "22.5kg"}, #Datos de wartortle
    {"id": 9, "nombre": "Blastoise", "tipo": "Agua", "imagen": "Blastoise.png", "poder": 79, "altura": "1.6m", "peso": "85.5kg"}, #Datos de blastoise
    {"id": 25, "nombre": "Pikachu", "tipo": "Electrico", "imagen": "Pikachu.png", "poder": 35, "altura": "0.4m", "peso": "6.0kg"}, #Datos de pikachu
    {"id": 39, "nombre": "Jigglypuff", "tipo": "Normal", "imagen": "Jigglypuff.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"}, #Datos de jigglypuff
    {"id": 52, "nombre": "Meowth", "tipo": "Normal", "imagen": "Meowth.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"}, #Datos de meowth
    {"id": 54, "nombre": "Psyduck", "tipo": "Agua", "imagen": "Psyduck.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"}, #Datos de psyduck
    {"id": 94, "nombre": "Gengar", "tipo": "Fantasma/Veneno", "imagen": "Gengar.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"}, #Datos de gengar
    {"id": 95, "nombre": "Onix", "tipo": "Roca/Tierra", "imagen": "Onix.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"}, #Datos de onix
    {"id": 143, "nombre": "Snorlax", "tipo": "Normal", "imagen": "Snorlax.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"}, #Datos de snorlax
]

@app.route('/')
def mostrar_todos():
    return render_template("index.html", pokemones=pokedex)

@app.route('/primeros/<int:cantidad>')
def mostrar_primeros(cantidad):
    if cantidad <= 0:
        return render_template("404.html", mensaje="La cantidad debe ser mayor a 0")
    primeros = pokedex[:cantidad]
    return render_template("index.html", pokemones=primeros)

@app.route('/pokemon/<int:id>')
def mostrar_pokemon_por_id(id):
    for pokemon in pokedex:
        if pokemon["id"] == id:
            return render_template("detalle.html", pokemon=pokemon)
    return render_template("404.html", mensaje=f"Pokémon con ID {id} no encontrado")

if __name__ == "__main__":
    app.run(debug=True)