from random import choice

capital = "Kisumu"
bird = "Western Meadowlark"
flower = "Sunflower"
song = "Home on the Range"

def randomfunfact():
    funfacts = [ "Nairobi got its name, meaning cool water, from the Maasai phrase Enkare Nairobi.",
        "Known as The Green City in the Sun, Nairobi is famous for its lush and lively atmosphere.",
        "Established in 1899 as a rail depot, Nairobi has a significant history connected to the Uganda - Kenya Railway."]

    index = choice("0123")

    print(funfacts[int(index)])

if __name__ == "__name__":
    randomfunfact()

# Linked to modules.py