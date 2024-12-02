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

ft.app(target=main)