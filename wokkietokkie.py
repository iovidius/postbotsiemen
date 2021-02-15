import re

# Key of vowels
vowels = {
  'a': '1',
  'e': '2',
  'i': '3',
  'o': '4',
  'u': '5',
  '1':'a',
  '2':'e',
  '3':'i',
  '4':'o',
  '5':'u'
}

# Returns the translation of an input string to 'wokkie tokkie'
def encipher(input): 
    output = ''
    for c in input:
        if (c in vowels):
            output += vowels[c] + ' '
        else:
            output += c +  'okkie ' if c.isalpha() else c
    return output.strip()

# Returns the translation of a 'wokkie tokkie' string to a normal string
# Expects an input in wokkie tokkie format.
def decipher(input):

    # remove spaces
    output = input.replace(' ','')

    # replace all consonants
    output = output.replace('okkie','')

    # replace all numbers
    for c in output:
        if (c in vowels):
            output = output.replace(c,vowels[c])

    return output

pattern = re.compile("(([a-z]okkie(\s)*)|[12345](\s)*)+", re.IGNORECASE)

# Find the wokkie tokkie elements of a string.
def match(input):
    x = re.search(pattern, input)
    if x is None:
        return ''
    else:
        return x.group(0)