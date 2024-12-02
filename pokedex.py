import flet as ft
import requests
import base64
from urllib.request import urlopen
from PIL import Image
from io import BytesIO

def main(page):
    page.tittle = "PokeDex App"
    page.window_ico = f"pokeball.ico"
    logo_pokemon = ft.Image(
        src=f"logo.png",
        width=350,
        height=170
    )
    
    nombre = ft.TextField(
        label="Nombre",
        autofocus=True
    )
    
    submit = ft.ElevatedButton("Consultar")
    
    pokemon_imagen = ft.Image(
        src=f"background.png",
        width=350,
        height=350
    )
    def show_snack_bar(message):
        snack_bar = ft.SnackBar(
            content=ft.Text(message),
            action="OK"
        )
        page.overlay.append(snack_bar)  # Añadimos el SnackBar a la lista de overlay
        snack_bar.open = True  # Mostramos el SnackBar
        page.update()

    def btn_click(e):
        api_url_pokemon = f'https://pokeapi.co/api/v2/pokemon/{nombre.value.lower()}'
        result = requests.get(api_url_pokemon)
        if result.status_code == 200:
            pokemon_data = result.json()
            url_image = pokemon_data['sprites']['other']['official-artwork']['front_default']
            if url_image:  # Verifica si la URL de la imagen existe
                im = Image.open(urlopen(url_image))
                buffer = BytesIO()
                im.save(buffer, format="PNG")  # Cambiado a "PNG"
                imagen_base64 = base64.b64encode(buffer.getvalue()).decode()
                pokemon_imagen.src_base64 = imagen_base64
                pokemon_imagen.update()
            else:
                show_snack_bar("Imagen no encontrada")
        else:
            show_snack_bar("Pokémon no encontrado")

    submit.on_click = btn_click
    page.add(
        logo_pokemon,
        nombre,
        submit,
        pokemon_imagen
    )

ft.app(target=main)
