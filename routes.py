from flask import render_template, redirect
from forms import RegisterUser, AddProduct, AddProductCategory, LoginUser
from extensions import app, db
from models import Product, ProductCategory, User
from flask_login import login_user, logout_user, login_required, current_user



@app.route("/")
def main_page():
    products=Product.query.all()
    return render_template("all.html", products=products)

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginUser()
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
        else:
            print(form.errors)
    return render_template("login.html", form=form)

@app.route("/logout", methods=["POST", "GET"])
def logout():
    logout_user()
    return redirect("/")

@app.route("/singin", methods=["POST", "GET"])
def singin():
    form = RegisterUser()
    if form.validate_on_submit():
        new_user = User(email=form.email.data,
                        password=form.password.data,
                        username=form.username.data,
                        phone_number=form.phone_number.data,
                        role="user")

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect("/")
    else:
        print(form.errors)
    return render_template("singin.html", form=form)

@app.route("/coffe")
def coffe():
    return render_template("coffe.html")

@app.route("/add_product", methods=['GET', 'POST'])
@login_required
def add_product():
    if current_user.role != "admin":
        return redirect("/")
    form = AddProduct()
    if form.validate_on_submit():
        new_product = Product(name=form.name.data,
                              image_url=form.image_url.data,
                              price=form.price.data,
                              type=form.type.data,
                              place_of_origin=form.place_of_origin.data,
                              main_ingredients=form.main_ingredients.data,
                              category_id=form.category_id.data)
        db.session.add(new_product)
        db.session.commit()
        return redirect("/")
    return render_template("add_product.html", form=form, categories=ProductCategory.query.all())

@app.route("/edit_product/<int:id>", methods=["POST", "GET"])
@login_required
def edit_product(id):
    product = Product.query.get(id)
    form = AddProduct(name=product.name, type=product.type, price=product.price, image_url=product.image_url,
                           main_ingredients=product.main_ingredients,place_of_origin=product.place_of_origin, category_id=product.category_id)

    if form.validate_on_submit():
        product.name = form.name.data
        product.text = form.type.data
        product.main_ingredients = form.main_ingredients.data
        product.place_of_origin = form.place_of_origin.data
        product.price = form.price.data
        product.image_url = form.image_url.data
        product.category_id = form.category_id.data

        db.session.commit()
        return redirect("/")
    else:
        print(form.errors)

    return render_template("edit_product.html", form=form)

@app.route("/delete_product/<int:id>", methods=["DELETE", "GET"])
@login_required
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect("/")

@app.route("/product/<int:id>")
def product(id):
    product = Product.query.get(id)
    return render_template("product.html", product=product)

@app.route("/all_products")
def all_products():
    products = Product.query.all()
    return render_template("products.html", products = products)

@app.route("/add_category", methods=['GET', 'POST'])
@login_required
def addCategory():
    form = AddProductCategory()
    if form.validate_on_submit():
        new_category = ProductCategory(name=form.category_name.data,
                                       id=form.id.data)
        db.session.add(new_category)
        db.session.commit()
        return redirect("/")
    else:
        print(form.errors)
    return render_template("add_category.html", form=form)

@app.route("/products/<int:category_id>")
@app.route("/products")
def products(category_id):
    if category_id:
        products = ProductCategory.query.get(category_id).products
    else:
        products = Product.query.all()
    return render_template("products.html", products=products)

@app.route("/search/<string:name>")
def search(name):
    products = Product.query.filter(Product.name.ilike(f"%{name}%")).all()
    return render_template("products.html", products=products)