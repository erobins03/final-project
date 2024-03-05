# import urllib.parse, urllib.request, urllib.error, json
# import requests
# import pprint
# from flask import Flask, render_template, request
#
#
# # # Create an instance of Flask
# # app = Flask (__name__)
# #
# # # Create a view function for /
# # @app.route("/")
# # def index():
# #     return render_template("index.html")
# #
# # @app.route("/info")
# def get_url(url):
#     try:
#         response = urllib.request.urlopen(url)
#         return json.loads(response.read())
#     except urllib.error.URLError as e:
#         print("Error: Unable to reach the server: ", e)
#         return None
#     except urllib.error.HTTPError as e:
#         print("Error: HTTP error code: ", e.code, e.reason)
#         return None
#     except Exception as e:
#         print("An unexpected error occurred: ", e)
#         return None
#
# def get_dog_photo(breed):
#     baseurl = "https://dog.ceo/api/breed/"
#     endpoint = "/images/random"
#
#     if len(breed.split()) == 2:
#         dog = breed.split()[1]
#         dog += '/'
#         dog += breed.split()[0]
#     else:
#         dog = breed
#
#     url = baseurl + dog + endpoint
#     return get_url(url)
#
# def print_data(image_data):
#     if image_data and image_data["status"] == "success":
#         image_url = image_data["message"]
#         print("Random dog image url: ", image_url)
#     else:
#         print("Failed to get a random dog image.")
#
# dog_breeds = ["fox terrier", "husky", "golden retriever", "chesapeake retriever", "french bulldog"]
#
# for breed in dog_breeds:
#     image_data = get_dog_photo(breed)
#     print_data(image_data)
#
#     dog_info = "https://en.wikipedia.org/wiki/"
#     dog_info += breed.replace(" ", "_")
#
#     name = requests.get(dog_info)
#     # print(name.status_code)
#     if name.status_code == 404:
#         print("This Wikipedia page does not exist" + "\n")
#     elif name.status_code == 200:
#         print("Here is some information about the dog: " + dog_info + "\n")