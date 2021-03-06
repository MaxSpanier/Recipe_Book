from flask import Flask, render_template, url_for, redirect, request
from app import app, db
from datetime import datetime
from bson.objectid import ObjectId


# https://flask-recipe-book.s3.eu-central-1.amazonaws.com/{{ recipe.image }}.jpg

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route("/add_recipe", methods=['GET', 'POST'])
def add_recipe():
    return render_template("add_recipe.html", meals=db.meals.find())

@app.route("/insert_recipe", methods=['GET', 'POST'])
def insert_recipe():
    recipe_title = request.form['title']
    recipe_description = request.form['description']
    recipe_method = request.form['method'].split(';')
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
        "cooking_time": recipe_cooking_time,
        "prep_time": recipe_prep_time,
        "image": recipe_image,
        "last_modified": current_time
    }

    db.recipes.insert_one(recipe_form)
    return redirect(url_for('home'))

@app.route("/all_recipes")
def all_recipes():
    recipes = db.recipes.find()
    return render_template("all_recipes.html", recipes=recipes)

@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    recipe = db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=recipe)

@app.route("/edit_recipe/<recipe_id>", methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipe = db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe, meals=db.meals.find())

@app.route("/change_recipe/<recipe_id>", methods=['GET', 'POST'])
def change_recipe(recipe_id):

    recipes = db.recipes

    recipe_title = request.form['title']
    recipe_description = request.form['description']
    recipe_method = request.form['method'].split(';')
    recipe_ingredients = request.form.getlist('ingredient')
    for recipe in recipe_ingredients:
        if recipe == "":
            recipe_ingredients.remove(recipe)
    recipe_meal = request.form.get('meal')
    recipe_serves = request.form['serves']
    recipe_cooking_time = request.form['cooking_time']
    recipe_prep_time = request.form['prep_time']
    recipe_image = request.form['image']

    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")

    recipes.update({'_id': ObjectId(recipe_id)},
                   {
        "title": recipe_title,
        "description": recipe_description,
        "method": recipe_method,
        "ingredients": recipe_ingredients,
        "meal": recipe_meal,
        "serves":  recipe_serves,
        "cooking-time": recipe_cooking_time,
        "prep-time": recipe_prep_time,
        "last_modified": current_time
    })
    return redirect(url_for('home'))


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    recipe = db.recipes.find_one({"_id": ObjectId(recipe_id)})
    db.recipes.delete_one(recipe)
    return redirect(url_for('home'))