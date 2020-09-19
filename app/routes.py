from flask import Flask, render_template, url_for, redirect, request
from app import app, mongo
from app.forms import RecipeForm

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route("/add_recipe", methods=['GET', 'POST'])
def add_recipe():
    return render_template("add_recipe.html")

@app.route("/insert_recipe", methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipe_title = request.form['title']

    recipe_form= {
        "title": recipe_title
    }

    recipes.insert_one(recipe_form)
    return redirect(url_for('home'))
