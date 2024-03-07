from flask import Flask, render_template, request
from function import *

app = Flask (__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "POST":
        breed = request.form["breed"].lower()
        image_data = get_dog_photo(breed)
        if image_data is None:
            random_image_data = get_url("https://dog.ceo/api/breeds/image/random")
            return render_template("results.html", breed=breed, image_data=random_image_data, success=False)
        dog_info_url = get_dog_info_url(breed)
        return render_template("results.html", breed=breed, image_data=image_data, dog_info_url=dog_info_url, success=True)


    if request.method == "GET":
        return index()

if __name__ == "__main__":
    app.run(debug=True)