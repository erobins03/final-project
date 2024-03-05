import urllib.parse, urllib.request, urllib.error, json
import requests
import pprint
from flask import Flask, render_template, request
import function

app = Flask (__name__)

def get_url(url):
    try:
        response = urllib.request.urlopen(url)
        return json.loads(response.read())
    except urllib.error.URLError as e:
        print("Error: Unable to reach the server: ", e)
        return None
    except urllib.error.HTTPError as e:
        print("Error: HTTP error code: ", e.code, e.reason)
        return None
    except Exception as e:
        print("An unexpected error occurred: ", e)
        return None

def print_data(image_data):
    if image_data and image_data["status"] == "success":
        image_url = image_data["message"]
        print("Random dog image url: ", image_url)
        return False
    else:
        print("Failed to get a random dog image.")
        return True


def get_dog_photo(breed):
    baseurl = "https://dog.ceo/api/breed/"
    endpoint = "/images/random"

    def make_breed(breed):
        if len(breed.split()) == 2:
            dog = breed.split()[1]
            dog += '/'
            dog += breed.split()[0]
            return dog
        else:
            return breed

    def make_url(dog):
        return baseurl + dog + endpoint

    dog = make_breed(breed)
    output = get_url(make_url(dog))
    failure = print_data(output)
    if failure:
        output = get_url(make_url(breed.replace(' ', '')))
        failure = print_data(output)
    if failure and len(breed.split()) == 2:
        split = breed.split()
        breed = split[1] + ' ' + split[0]
        dog = make_breed(breed)
        url = make_url(dog)
        output = get_url(url)
        print_data(output)
    return output

def get_dog_info_url(breed):
    dog_info_url = "https://en.wikipedia.org/wiki/" + breed.replace(" ", "_")
    return dog_info_url

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "POST":
        breed = request.form["breed"]
        image_data = get_dog_photo(breed)
        # if print_data(image_data):
        #     image_data = get_dog_photo(breed.replace(' ', ''))
        #     print_data(image_data)
        dog_info_url = get_dog_info_url(breed)
        return render_template("results.html", breed=breed, image_data=image_data, dog_info_url=dog_info_url)

    if request.method == "GET":
        return index()

if __name__ == "__main__":
    app.run(debug=True)