from flask import Flask, render_template, url_for, redirect, request
from app import app, db
from datetime import datetime


# https://flask-recipe-book.s3.eu-central-1.amazonaws.com/{{ recipe.image }}.jpg

@app.route("/", methods=['GET', 'POST'])
def home():
    entry = db.recipes.find_one({"title": "Brownies"})
    return render_template("home.html", entry=entry)

@app.route("/add_recipe", methods=['GET', 'POST'])
def add_recipe():
    return render_template("add_recipe.html", meals=db.meals.find())

@app.route("/insert_recipe", methods=['GET', 'POST'])
def insert_recipe():
    recipe_title = request.form['title']
    recipe_description = request.form['description']
    recipe_method = request.form['method']
    recipe_ingredients = request.form.getlist('ingredient')
    recipe_meal = request.form.get('meal')
    recipe_serves = request.form['serves']
    recipe_cooking_time = request.form['cooking_time']
    recipe_prep_time = request.form['prep_time']
    recipe_image = request.form['image']

    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")

    recipe_form = {
    "title": recipe_title,
    "decription": recipe_description,
    "method": recipe_method,
    "ingredients": recipe_ingredients,
    "meal": recipe_meal,
    "serves": recipe_serves,
    "cooking-time": recipe_cooking_time,
    "prep-time": recipe_prep_time,
    "image": recipe_image,
    "last_modified": current_time
    }

    db.recipes.insert_one(recipe_form)
    return redirect(url_for('home'))