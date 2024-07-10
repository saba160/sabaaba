from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField, BooleanField, PasswordField, FloatField, URLField, \
    SelectField, EmailField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, Length, EqualTo

class RegisterUser(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, message="Password min length is 8")])
    repeat_password = PasswordField("Repeat password", validators=[DataRequired(), Length(min=8),
                                                                   EqualTo('password', message='Passwords do not match')])
    phone_number = IntegerField("Phone Number", validators=[DataRequired()])
    submit = SubmitField("Submit")

class LoginUser(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, message="Password min length is 8")])
    submit = SubmitField("Submit")

class AddProduct(FlaskForm):
    name = StringField("Product name", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired()])
    type = StringField("Text", validators=[DataRequired()])
    place_of_origin = StringField("Place Of Origin", validators=[DataRequired()])
    main_ingredients = StringField("Main Ingredients", validators=[DataRequired()])
    category_id = IntegerField("Category ID", validators=[DataRequired()])
    image_url = URLField("Product picture", validators=[DataRequired()])
    submit = SubmitField("Submit")

class AddProductCategory(FlaskForm):
    category_name = StringField("Category name", validators=[DataRequired()])
    id = IntegerField("ID", validators=[DataRequired()])
    submit = SubmitField("Submit")