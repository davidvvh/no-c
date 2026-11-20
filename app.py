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
    {"id": 13, "nombre": "Weedle", "tipo": "Bicho/Veneno", "imagen": "Weedle.png", "poder": 40, "altura": "0.3m", "peso": "3.2kg"},
    {"id": 14, "nombre": "Kakuna", "tipo": "Bicho/Veneno", "imagen": "Kakuna.png", "poder": 45, "altura": "0.6m", "peso": "10.0kg"},
    {"id": 15, "nombre": "Beedrill", "tipo": "Bicho/Veneno", "imagen": "Beedrill.png", "poder": 65, "altura": "1.0m", "peso": "29.5kg"},
    {"id": 16, "nombre": "Pidgey", "tipo": "Normal/Volador", "imagen": "Pidgey.png", "poder": 40, "altura": "0.3m", "peso": "1.8kg"},
    {"id": 17, "nombre": "Pidgeotto", "tipo": "Normal/Volador", "imagen": "Pidgeotto.png", "poder": 63, "altura": "1.1m", "peso": "30.0kg"},
    {"id": 18, "nombre": "Pidgeot", "tipo": "Normal/Volador", "imagen": "Pidgeot.png", "poder": 83, "altura": "1.5m", "peso": "39.5kg"},
    {"id": 19, "nombre": "Rattata", "tipo": "Normal", "imagen": "Rattata.png", "poder": 30, "altura": "0.3m", "peso": "3.5kg"},
    {"id": 20, "nombre": "Raticate", "tipo": "Normal", "imagen": "Raticate.png", "poder": 55, "altura": "0.7m", "peso": "18.5kg"},
    {"id": 21, "nombre": "Spearow", "tipo": "Normal/Volador", "imagen": "Spearow.png", "poder": 40, "altura": "0.3m", "peso": "2.0kg"},
    {"id": 22, "nombre": "Fearow", "tipo": "Normal/Volador", "imagen": "Fearow.png", "poder": 65, "altura": "1.2m", "peso": "38.0kg"},
    {"id": 23, "nombre": "Ekans", "tipo": "Veneno", "imagen": "Ekans.png", "poder": 35, "altura": "2.0m", "peso": "6.9kg"},
    {"id": 24, "nombre": "Arbok", "tipo": "Veneno", "imagen": "Arbok.png", "poder": 60, "altura": "3.5m", "peso": "65.0kg"},
    {"id": 25, "nombre": "Pikachu", "tipo": "Electrico", "imagen": "Pikachu.png", "poder": 35, "altura": "0.4m", "peso": "6.0kg"},
    {"id": 26, "nombre": "Raichu", "tipo": "Electrico", "imagen": "Raichu.png", "poder": 60, "altura": "0.8m", "peso": "30.0kg"},
    {"id": 27, "nombre": "Sandshrew", "tipo": "Tierra", "imagen": "Sandshrew.png", "poder": 50, "altura": "0.6m", "peso": "12.0kg"},
    {"id": 28, "nombre": "Sandslash", "tipo": "Tierra", "imagen": "Sandslash.png", "poder": 75, "altura": "1.0m", "peso": "29.5kg"},
    {"id": 29, "nombre": "Nidoran♀", "tipo": "Veneno", "imagen": "Nidoran♀.png", "poder": 55, "altura": "0.4m", "peso": "7.0kg"},
    {"id": 30, "nombre": "Nidorina", "tipo": "Veneno", "imagen": "Nidorina.png", "poder": 70, "altura": "0.8m", "peso": "20.0kg"},
    {"id": 31, "nombre": "Nidoqueen", "tipo": "Veneno/Tierra", "imagen": "Nidoqueen.png", "poder": 90, "altura": "1.3m", "peso": "60.0kg"},
    {"id": 32, "nombre": "Nidoran♂", "tipo": "Veneno", "imagen": "Nidoran♂.png", "poder": 46, "altura": "0.5m", "peso": "9.0kg"},
    {"id": 33, "nombre": "Nidorino", "tipo": "Veneno", "imagen": "Nidorino.png", "poder": 61, "altura": "0.9m", "peso": "19.5kg"},
    {"id": 34, "nombre": "Nidoking", "tipo": "Veneno/Tierra", "imagen": "Nidoking.png", "poder": 81, "altura": "1.4m", "peso": "62.0kg"},
    {"id": 35, "nombre": "Clefairy", "tipo": "Normal", "imagen": "Clefairy.png", "poder": 70, "altura": "0.6m", "peso": "7.5kg"},
    {"id": 36, "nombre": "Clefable", "tipo": "normal", "imagen": "Clefable.png", "poder": 95, "altura": "1.3m", "peso": "40.0kg"},
    {"id": 37, "nombre": "Vulpix", "tipo": "Fuego", "imagen": "Vulpix.png", "poder": 38, "altura": "0.6m", "peso": "9.9kg"},
    {"id": 38, "nombre": "Ninetales", "tipo": "Fuego", "imagen": "Ninetales.png", "poder": 73, "altura": "1.1m", "peso": "19.9kg"},
    {"id": 39, "nombre": "Jigglypuff", "tipo": "Normal", "imagen": "Jigglypuff.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"},
    {"id": 40, "nombre": "Wigglytuff", "tipo": "Normal", "imagen": "Wigglytuff.png", "poder": 140, "altura": "1.0m", "peso": "12.0kg"},
    {"id": 41, "nombre": "Zubat", "tipo": "Veneno/Volador", "imagen": "Zubat.png", "poder": 40, "altura": "0.8m", "peso": "7.5kg"},
    {"id": 42, "nombre": "Golbat", "tipo": "Veneno/Volador", "imagen": "Golbat.png", "poder": 75, "altura": "1.6m", "peso": "55.0kg"},
    {"id": 43, "nombre": "Oddish", "tipo": "Planta/Veneno", "imagen": "Oddish.png", "poder": 45, "altura": "0.5m", "peso": "5.4kg"},
    {"id": 44, "nombre": "Gloom", "tipo": "Planta/Veneno", "imagen": "Gloom.png", "poder": 60, "altura": "0.8m", "peso": "8.6kg"},
    {"id": 45, "nombre": "Vileplume", "tipo": "Planta/Veneno", "imagen": "Vileplume.png", "poder": 75, "altura": "1.2m", "peso": "18.6kg"},
    {"id": 46, "nombre": "Paras", "tipo": "Bicho/Planta", "imagen": "Paras.png", "poder": 35, "altura": "0.3m", "peso": "5.4kg"},
    {"id": 47, "nombre": "Parasect", "tipo": "Bicho/Planta", "imagen": "Parasect.png", "poder": 60, "altura": "1.0m", "peso": "29.5kg"},
    {"id": 48, "nombre": "Venonat", "tipo": "Bicho/Veneno", "imagen": "Venonat.png", "poder": 60, "altura": "1.0m", "peso": "30.0kg"},
    {"id": 49, "nombre": "Venomoth", "tipo": "Bicho/Veneno", "imagen": "Venomoth.png", "poder": 70, "altura": "1.5m", "peso": "12.5kg"},
    {"id": 50, "nombre": "Diglett", "tipo": "Tierra", "imagen": "Diglett.png", "poder": 10, "altura": "0,2m", "peso": "0,8kg"},
    {"id": 51, "nombre": "Dugtrio", "tipo": "Tierra", "imagen": "Dugtrio.png", "poder": 35, "altura": "0,7m", "peso": "33,3kg"},
    {"id": 52, "nombre": "Meowth", "tipo": "Normal", "imagen": "Meowth.png", "poder": 40, "altura": "0.4m", "peso": "4.2kg"},
    {"id": 53, "nombre": "Persian", "tipo": "Normal", "imagen": "Persian.png", "poder": 65, "altura": "1,0m", "peso": "32,0kg"},
    {"id": 54, "nombre": "Psyduck", "tipo": "Agua", "imagen": "Psyduck.png", "poder": 50, "altura": "0.8m", "peso": "19.6kg"},
    {"id": 55, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 56, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 57, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 58, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 59, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 60, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 61, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 62, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 63, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 64, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 65, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 66, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 67, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 68, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 69, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 70, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 71, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 72, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 73, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 74, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 75, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 76, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 77, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 78, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 79, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 80, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 81, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 82, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 83, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 84, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 85, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 86, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 87, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 88, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 89, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 90, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 91, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 92, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 93, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 94, "nombre": "Gengar", "tipo": "Fantasma/Veneno", "imagen": "Gengar.png", "poder": 60, "altura": "1.5m", "peso": "40.5kg"},
    {"id": 95, "nombre": "Onix", "tipo": "Roca/Tierra", "imagen": "Onix.png", "poder": 35, "altura": "8.8m", "peso": "210.0kg"},
    {"id": 96, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 97, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 98, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 99, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 100, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 101, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 102, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 103, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 104, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 105, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 106, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 107, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 108, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 109, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 110, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 111, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 112, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 113, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 114, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 115, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 116, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 117, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 118, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 119, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 120, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 121, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 122, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 123, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 124, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 125, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 126, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 127, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 128, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 129, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 130, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 131, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 132, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 133, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 134, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 135, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 136, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 137, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 138, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 139, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 140, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 141, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 142, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 143, "nombre": "Snorlax", "tipo": "Normal", "imagen": "Snorlax.png", "poder": 45, "altura": "2.1m", "peso": "460.0kg"},
    {"id": 144, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 145, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 146, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 147, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 148, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 149, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 150, "nombre": "", "tipo": "", "imagen": "", "poder": , "altura": "", "peso": ""},
    {"id": 151, "nombre": "Mew", "tipo": "Psiquico", "imagen": "Mew.png", "poder": 100, "altura": "0.4m", "peso": "4.0kg"}
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