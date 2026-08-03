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
    {"id": 10, "nombre": "Caterpie", "tipo": "Bicho", "imagen": "Caterpie.png", "poder": 45, "altura": "0.3m", "peso": "2.9kg"}, #Datos de caterpie
    {"id": 11, "nombre": "Metapod", "tipo": "Bicho", "imagen": "Metapod.png", "poder": 50, "altura": "0.7m", "peso": "9.9kg"}, #Datos de metapod
    {"id": 12, "nombre": "Butterfree", "tipo": "Bicho/volador", "imagen": "Butterfree.png", "poder": 60, "altura": "1.1m", "peso": "32.0kg"}, #Datos de butterfree
    {"id": 13, "nombre": "Weedle", "tipo": "Bicho/Veneno", "imagen": "Weedle.png", "poder": 40, "altura": "0.3m", "peso": "3.2kg"}, #Datos de weedle
    {"id": 14, "nombre": "Kakuna", "tipo": "Bicho/Veneno", "imagen": "Kakuna.png", "poder": 45, "altura": "0.6m", "peso": "10.0kg"}, #Datos de kakuna
    {"id": 15, "nombre": "Beedrill", "tipo": "Bicho/Veneno", "imagen": "Beedrill.png", "poder": 65, "altura": "1.0m", "peso": "29.5kg"}, #Datos de beedrill
    {"id": 16, "nombre": "Pidgey", "tipo": "Normal/Volador", "imagen": "Pidgey.png", "poder": 40, "altura": "0.3m", "peso": "1.8kg"},#Datos de pidgey
    {"id": 17, "nombre": "Pidgeotto", "tipo": "Normal/Volador", "imagen": "Pidgeotto.png", "poder": 63, "altura": "1.1m", "peso": "30.0kg"},#Datos de pidgeotto
    {"id": 18, "nombre": "Pidgeot", "tipo": "Normal/Volador", "imagen": "Pidgeot.png", "poder": 83, "altura": "1.5m", "peso": "39.5kg"},#Datos de pidgeot
    {"id": 19, "nombre": "Rattata", "tipo": "Normal", "imagen": "Rattata.png", "poder": 30, "altura": "0.3m", "peso": "3.5kg"},#Datos de rattata
    {"id": 20, "nombre": "Raticate", "tipo": "Normal", "imagen": "Raticate.png", "poder": 55, "altura": "0.7m", "peso": "18.5kg"},#Datos de raticate
    {"id": 21, "nombre": "Spearow", "tipo": "Normal/Volador", "imagen": "Spearow.png", "poder": 40, "altura": "0.3m", "peso": "2.0kg"},#Datos de spearow
    {"id": 22, "nombre": "Fearow", "tipo": "Normal/Volador", "imagen": "Fearow.png", "poder": 65, "altura": "1.2m", "peso": "38.0kg"},#Datos de fearow
    {"id": 23, "nombre": "Ekans", "tipo": "Veneno", "imagen": "Ekans.png", "poder": 35, "altura": "2.0m", "peso": "6.9kg"},#Datos de ekans
    {"id": 24, "nombre": "Arbok", "tipo": "Veneno", "imagen": "Arbok.png", "poder": 60, "altura": "3.5m", "peso": "65.0kg"},#Datos de arbok
    {"id": 25, "nombre": "Pikachu", "tipo": "Electrico", "imagen": "Pikachu.png", "poder": 35, "altura": "0.4m", "peso": "6.0kg"}, #Datos de pikachu
    {"id": 26, "nombre": "Raichu", "tipo": "Electrico", "imagen": "Raichu.png", "poder": 60, "altura": "0.8m", "peso": "30.0kg"},#Datos de raichu
    {"id": 27, "nombre": "Sandshrew", "tipo": "Tierra", "imagen": "Sandshrew.png", "poder": 50, "altura": "0.6m", "peso": "12.0kg"},#Datos de sandshrew
    {"id": 28, "nombre": "Sandslash", "tipo": "Tierra", "imagen": "Sandslash.png", "poder": 75, "altura": "1.0m", "peso": "29.5kg"},#Datos de sandslash
    {"id": 29, "nombre": "Nidoran♀", "tipo": "Veneno", "imagen": "Nidoran♀.png", "poder": 55, "altura": "0.4m", "peso": "7.0kg"},#Datos de nidoran♀
    {"id": 30, "nombre": "Nidorina", "tipo": "Veneno", "imagen": "Nidorina.png", "poder": 70, "altura": "0.8m", "peso": "20.0kg"},#Datos de nidorina
    {"id": 31, "nombre": "Nidoqueen", "tipo": "Veneno/Tierra", "imagen": "Nidoqueen.png", "poder": 90, "altura": "1.3m", "peso": "60.0kg"},#Datos de nidoqueen
    {"id": 32, "nombre": "Nidoran♂", "tipo": "Veneno", "imagen": "Nidoran♂.png", "poder": 46, "altura": "0.5m", "peso": "9.0kg"},#Datos de nidoran♂
    {"id": 33, "nombre": "Nidorino", "tipo": "Veneno", "imagen": "Nidorino.png", "poder": 61, "altura": "0.9m", "peso": "19.5kg"},#Datos de nidorino
    {"id": 34, "nombre": "Nidoking", "tipo": "Veneno/Tierra", "imagen": "Nidoking.png", "poder": 81, "altura": "1.4m", "peso": "62.0kg"},#Datos de nidoking
    {"id": 35, "nombre": "Clefairy", "tipo": "Normal", "imagen": "Clefairy.png", "poder": 70, "altura": "0.6m", "peso": "7.5kg"},#Datos de clefairy
    {"id": 36, "nombre": "Clefable", "tipo": "normal", "imagen": "Clefable.png", "poder": 95, "altura": "1.3m", "peso": "40.0kg"},#datos de clefable
    {"id": 37, "nombre": "Vulpix", "tipo": "Fuego", "imagen": "Vulpix.png", "poder": 38, "altura": "0.6m", "peso": "9.9kg"},#Datos de vulpix
    {"id": 38, "nombre": "Ninetales", "tipo": "Fuego", "imagen": "Ninetales.png", "poder": 73, "altura": "1.1m", "peso": "19.9kg"},#Datos de ninetales
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