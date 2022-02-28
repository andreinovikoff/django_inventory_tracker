# Django Delights Inventory Tracker

## Short Overview
This project has me create an app to help a restaurant owner keep track of his inventory and sales.
Counting and aggregating data is a typical use case for Python, and Python has some powerful ways to process and generate visualizations for data. Django allows us to bring that power of Python data processing to the web, and easily store, format, and display that data using Django views. 

## Project Title
Django Delights Inventory Tracker

## Hours to Complete
10

## Project Objectives

- Build an inventory and sales application using Django
- Version control an application with Git and host the repository on GitHub
- Users can log in and log out, and must be logged in to see the views
- Users can create items for the menu
- Users can add ingredients to the restaurant's inventory and update their quantities
- Users can add the different recipe requirements for each menu item
- Users can record purchases of menu items (only the ones that are able to be created with what's in the inventory!)
- Users can view the current inventory, menu items, their ingredients, and a log of all purchases made

## Prerequisites
- HTML
- CSS
- Python
- Django
- Git
- Command Line

## Understand the database models

For this project, we have four models. Add definitions for each of these in `models.py`

### `Ingredient`
This model represents an ingredient that the restaurant has in its inventory.

An ingredient should have the following fields (at least):
- **`name`**: the name of the ingredient (i.e. `flour`)
- **`quantity`**: the quantity of the ingredient available in the inventory (i.e. `4.5`)
- **`unit`**: the unit used for the ingredient (i.e. `tbsp` or `lbs`)
- **`unit_price`**: the price per unit of the ingredient (i.e. `0.05`, for a `tbsp` of `flour`)

### `MenuItem`
This model represents an item on the restaurant's menu.

A menu item should have the following fields (at least):
- **`title`**: the title of the item on the menu (i.e. `Django Juice`)
- **`price`**: the price of the item (i.e. `3.49` for a glass)

### `RecipeRequirement`
This model represents a single ingredient and how much of it is required for an item off the menu.

A recipe requirement should have the following fields (at least):
- **`menu_item`**: a reference to an item on the menu (i.e. a foreign key to the `MenuItem` model)
- **`ingredient`**: a reference to a required ingredient for the associated menu item (i.e. a foreign key to the `Ingredient` model)
- **`quantity`**: the amount of the associated ingredient that is required to create the menu item (i.e. `1.5` ounces of `sugar` to create `Django Djaffa Cake`)


### `Purchase`
This model represents a customer purchase of an item off the menu.

A purchase should have the following fields (at least):
- **`menu_item`**: a reference to an item on the menu (i.e. a foreign key to the `MenuItem` model)
- **`timestamp`**: a timestamp indicating the time that the purchase was recorded (i.e. a `DateTimeField`)

## Creating views and templates
To enable a full suite of CRUD functionality for the inventory app, there is one templates for each of the following:

- a base template for all the other pages to inherit from, with common styling and a navbar linking to the other pages
- a home page
- a page to view all ingredients in the inventory
- a page to view the menu
- a page to view the purchases made at the restaurant
- a page to view the profit and revenue report
- a page to add an item to the menu
- a page to add an ingredient to the inventory
- a page to add the recipe requirements for a menu item
- a page to record a new purchase of a menu item
- a page to update the inventory for an existing ingredient


Create templates appropriately inside `inventory/templates/inventory`, taking care to use all of Django's generics functionality (`ListView`, `CreateView`, `UpdateView`, `TemplateView`).


## Authentication
A log in and log out page for our inventory application.


