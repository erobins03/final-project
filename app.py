
import urllib.parse, urllib.request, urllib.error, json
import pprint
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

def get_dog_photo(breed):
    baseurl = "https://dog.ceo/api/breed/"
    endpoint = "/images/random"

    if len(breed.split()) == 2:
        dog = breed.split()[1]
        dog += '/'
        dog += breed.split()[0]
    else:
        dog = breed

    url = baseurl + dog + endpoint
    return get_url(url)

def print_data(image_data):
    if image_data and image_data["status"] == "success":
        image_url = image_data["message"]
        print("Random dog image url: ", image_url)
    else:
        print("Failed to get a random dog image.")

dog_breeds = ["corgi", "husky", "golden retriever", "chesapeake retriever", "french bulldog"]

for breed in dog_breeds:
    image_data = get_dog_photo(breed)
    print_data(image_data)

    dog_info = "https://en.wikipedia.org/wiki/"
    dog_info += breed.replace(" ", "_")
    print("Here is some information about the dog: " + dog_info + "\n")




