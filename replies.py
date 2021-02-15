from enum import Enum
import random

trans_templates = ["Dat is ", "Dat betekent ", ""]
dunno_templates = ["Doar kan ik niks van maaaken hoor!", "Doar krijg 'k geen chocola van maakt."]
conf_templates = ["Dat klopt helemaal!", "'t Is makkelijk, je weet al hoe het moet!", "Jaaahoor!", "Dat is helemaal gokkie 4 2 dokkie!"]

Template = Enum('Template', 'dunno translation confirmation')

# Generates a sentence based on the templates above.
def generate(type, trans = ""):
    if type == Template.dunno:
        return random.choice(dunno_templates)
    elif type == Template.confirmation:
        return random.choice(conf_templates)
    elif type == Template.translation:
        return (random.choice(trans_templates) + trans + '!').capitalize()