# ~ Import FLASK Libraries ~
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditor, CKEditorField

# ~ Import SQLALCHEMY Libraries ~
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text

# ~ Import WTFORMS Libraries ~
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

# ~ Import DATETIME Libraries (It's neccesery to get current date) ~
from datetime import date



# ~ SET FLASK ~
app = Flask(__name__)
app.config['SECRET_KEY'] = #? 'Set Your Secret Key Here'

# ~ I'm using the Flask CKEditor to make the Blog Content input in the WTForm ~ 
ckeditor.init_app(app)
Bootstrap5(app)


# ~ CONFIGURE DATABASE ~
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.database'
database = SQLAlchemy(model_class=Base)
database.init_app(app)


# ~ CREATE TABLE ~
class PostToBlog(database.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    url_image: Mapped[str] = mapped_column(String(250), nullable=False)
