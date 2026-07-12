import urllib.parse
import webbrowser

def search(debug, target):
    if debug: print(f"The Action is 'Search' and the Target is '{target}'")
    url = f"https://www.google.com/search?q={urllib.parse.quote(target)}"
    webbrowser.open(url)
    return