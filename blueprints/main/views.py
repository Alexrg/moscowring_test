from flask import Blueprint, render_template, request, redirect
from blueprints.main.distance_form import CoordinatesForm
import geocoder
from blueprints.main.calculate_distance import calculate_distance

main = Blueprint('main', __name__, template_folder="templates")

@main.route("/", methods=['POST','GET'])
def index():
    """
    The main view of the aplication. This will show a form so the user can
    input a coordinate.
    """
    form = CoordinatesForm()

    if request.method == 'GET':
        return render_template("main/home.html", form=form)
    elif request.method == 'POST':
        geocode_url = "https://geocode-maps.yandex.ru/1.x/?"
        apikey = "7fd9f29c-8db8-4589-b53b-226d7b0cf4a1"
        response = redirect("{}apikey={}&format=json&geocode={},{}&lang=en-US".format(geocode_url,apikey,form.latitude.data,form.longitud.data))

        distance = calculate_distance(37.834605,55.675945, form.latitude.data,form.longitud.data)
        print("The distance is {} km".format(distance))

        return redirect ("{}apikey={}&format=json&geocode={},{}&lang=en-US".format(geocode_url,apikey,form.latitude.data,form.longitud.data))