from flask import Blueprint, render_template, flash, url_for, redirect
from app.models.supabase_client import supabase
from app.controllers.main.services import get_all_products


main_blueprint = Blueprint('main',__name__, url_prefix ='/')

@main_blueprint.route('/')

def index():
    if not supabase:
        flash("Serviço indisponpivel")
        return render_template("main/index.html", products=[])

    supabase_response = get_all_products()

    if supabase_response and supabase_response.data:
        product_list = supabase_response.data

    else:
        flash("warning")
        return render_template("main/index.html", products = supabase_response)
