from enum import Enum
import random

trans_templates = ["Dat is ", "Dat betekent ", ""]
dunno_templates = ["Doar krijg 'k geen chocola van maakt.", "Kind toch!", "Skitterend mooi!"]
conf_templates = ["Dat klopt helemaal!", "'t Is makkelijk, je weet al hoe het moet!", "Jaaahoor!", "Dat is helemaal gokkie 4 2 dokkie!"]
bad_word_en_template = ["Mijn Engels is niet zo goed, maar volgens mij betekent dat iets geks!", "Dat woord ken ik niet, duus!"]
bad_word_nl_template = ["Hou je me voor het lapje? Dat kan ik toch niet zeggen?", "Wat een skrikkelijk woord."]
too_long_template = ["Dat is toch een veeeel te lang wooord!", "Ik heb helemaal geen tijd om zo'n lang woord te vertalen, ik moet werken!"]
bored_template = ["Ohhh, maar ik heb geen tijd, ik moet weeerken! Dááárom.", "Ik heb skrikkelijk weinig tijd!"]

Template = Enum('Template', 'dunno translation confirmation bad_nl bad_en too_long bored')
Word = Enum('Word', 'bad_en bad_nl normal')

def random_url():
    with open('data/urls.txt') as f:
        lines = f.readlines()
        return random.choice(lines)


# Generates a sentence based on the templates above.
def generate(type, trans = ""):
    if type == Template.dunno:
        return random.choice(dunno_templates)

    if type == Template.confirmation:
        return random.choice(conf_templates)

    if type == Template.translation:
        return (random.choice(trans_templates) + trans + '!').capitalize()
    
    if type == Template.bad_en:
        return random.choice(bad_word_en_template)
    
    if type == Template.bad_nl:
        return random.choice(bad_word_nl_template)

    if type == Template.too_long:
        return random.choice(too_long_template)

    if type == Template.bored:
        return random.choice(bored_template) + ' Misskien kan dit filmpje je bekoren ' + random_url()
    

# Checks if the user tries to get Siemen to say bad words
def isBad(input):
    with open('data/bad-words-nl.txt') as file:
      for line in file:
        if line[:-1] == input:
            return Word.bad_nl
    with open('data/bad-words-en.txt') as file:
      for line in file:
          if line[:-1] == input:
              return Word.bad_en
    return Word.normal