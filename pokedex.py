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
ft.app(target=main)