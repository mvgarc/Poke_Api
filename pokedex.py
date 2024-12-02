import flet as ft
import requests
import base64
from urllib.request import urlopen
from PIL import Image
from io import BytesIO

def main(page):
    logo_pokemon = ft.Image(
        src=f"logo.png",
        width=350,
        height=170)
    
    nombre = ft.TextField(
        label ="Nombre",
        autofocus=True)
    
    submit = ft.ElevatedButton("Consultar")
    
    pokemon_imagen = ft.Image(
        src="background.png",
        width=350,
        height= 350
    )

    def btn_click(e):
        api_url_pokemon = f'https://pokeapi.co/api/v2/{nombre.value}'
        result = requests.get(api_url_pokemon)
        if result.status_code==200:
            pokemon_data = result.json()
            url_image = pokemon_data['sprites']['other']['official-artwork']['front_default']
            im = Image.open(urlopen(url_image))
            buffer = BytesIO()
            im.save(buffer, format="png")
            imagen_base64 = base64.b64encode(buffer.getvalue()).decode()
            pokemon_imagen.src_base64 = imagen_base64
            pokemon_imagen.update()



    submit.on_click = btn_click
    page.add(
        logo_pokemon,
        nombre,
        submit,
        pokemon_imagen
    )

ft.app(target=main)