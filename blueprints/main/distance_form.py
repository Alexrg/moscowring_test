from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired

class CoordinatesForm(FlaskForm):
	"""
	Creates a form of two input fields so the user can enter a coordinate.
	"""
    longitud = FloatField('longitud', validators=[DataRequired()])
    latitude = FloatField('latitude', validators=[DataRequired()])
    submit = SubmitField('Submit')