import regex

wt_pattern = regex.compile('(([a-z]okkie(\s)*)|[12345](\s)*)+', regex.IGNORECASE)
trans_pattern = regex.compile('(?<=(wat is)|(vertaal)|(hoe zeg je)|(wat betekent)\s)\w*', regex.IGNORECASE)
quotes_pattern = regex.compile("([\"'])(?:(?=(\\\\?))\\2.)*?\\1", regex.IGNORECASE)
bored_pattern = regex.compile('(ik verveel me)|(wij vervelen ons)|((vervelen|verveelt) zich)', regex.IGNORECASE)

# Find the pattern elements of a string
def match(input, pattern):
    x = regex.search(pattern, input)
    if x is None:
        return ''
    else:
        return x.group(0)