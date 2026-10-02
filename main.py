import random

from flask import Flask

app = Flask(__name__)

facts_list = [
    "Most people suffering from technology addiction experience intense stress when they are outside network coverage areas or unable to use their devices.",
    "According to a 2018 study, more than 50% of people aged 18 to 34 consider themselves dependent on their smartphones.",
    "The study of technology dependence is one of the most significant areas of modern scientific research.",
    "According to a 2019 study, more than 60% of people respond to work-related messages on their smartphones within 15 minutes of leaving work.",
    "One way to combat technology dependence is to seek out activities that provide pleasure and improve mood.",
    "Elon Musk states that social media platforms are designed to keep us engaged, ensuring we spend as much time as possible viewing content.",
    "Elon Musk also advocates for the regulation of social media and the protection of users' personal data. He asserts that social media platforms collect vast amounts of information about us, which can then be used to manipulate our thoughts and behaviors.",
    "Social media has both positive and negative aspects, and we must be aware of both when using these platforms."
]

@app.route("/")
def index():
    return '<h1>Hola, en esta página puedes aprender un par de cosas interesantes sobre las dependencias tecnológicas.</h1><a href="/random_fact">¡Ver un hecho al azar!</a><br><a href="/secret">¡Ir a la página secreta!</a>'

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

# Nueva ruta para la página secreta
@app.route("/secret")
def secret():
    coin_filp = ["Heads", "Tails"]
    resultado = random.choice(coin_filp)
    return f'<h1>Welcome to the secret page!</h1><p>{resultado}</p><a href="/">Back Home</a>'

if __name__ == "__main__":
    app.run(debug=True)