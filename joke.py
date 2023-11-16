import pyjokes

def generate_joke():
    joke = pyjokes.get_joke(language='en', category='all')
    print(joke)

# Generate a joke
generate_joke()