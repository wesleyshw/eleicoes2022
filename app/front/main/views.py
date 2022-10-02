from urllib import response
from flask import Blueprint, render_template, request, redirect, flash, url_for
import requests
import json

main = Blueprint(
    "main",
    __name__,
    url_prefix="/",
    template_folder="templates",
    static_folder="static",
    static_url_path="/main/static",
)

@main.app_template_filter("to_now")
def format_filter(value):
    return "{0:,}".format(int(value))


@main.get("/")
def index():
    data = requests.get("https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json")
    json_data = json.loads(data.content)
    print(json_data)
    return render_template("index.html", data=json_data)
