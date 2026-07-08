import requests
from ddgs import DDGS
from textReader import readText


def wikiAPI(debug, target, attempt):
    print("TARGET:   " + target)
    #Generic API request setup
    S = requests.Session()
    S.headers.update({
        'User-Agent': 'SimpleHelp/1.0 (andrew.doubrava0311@gmail.com)'
    })
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "titles": target,
        "format": "json",
        "prop": "extracts",
        "explaintext": "true",
        "exintro": "true",
        "redirects": "5",
    }

    #Attempt to retrieve information from the WikiAPI and handle Errors
    try:
        R = S.get(url=URL, params=PARAMS)
        data = R.json()
    except requests.exceptions.RequestException as e:
        print(e)
    except requests.exceptions.Timeout as e:
        print(e)
    except requests.exceptions.ConnectionError as e:
        print(e)
    except requests.exceptions.TooManyRedirects as e:
        print(e)
    except requests.exceptions.RequestException as e:
        print(e)

    #Convert Request into JSON (data) and handle Errors
    try:
        data = R.json()
    except ValueError:
        print("Value Error")
        return ""

    #Print Debug Information
    if (debug):
        print("Wiki API Debug Info:\n")
        print(R.url)
        print(R.history)
        print(R.status_code)
        print(R.headers.get("Content-Type"))
        print(R.text[:500])

    #Locate and return extract from JSON and handle Error if not found
    try:
        page = next(iter(data['query']['pages'].values()))
        if debug: print(page)
        return page['extract']
    except KeyError:
        if debug: print("Wiki FAILURE\nAttempting DDG Search")
        try:
            with DDGS() as ddgs:
                if attempt > 3: return ""
                result = ddgs.text(f'site:wikipedia.org {target}')
                result = result[0]['href']
                attempt = attempt + 1
                return wikiAPI(debug, result[30:].replace('_'," "), attempt)
        except StopIteration:
            print("No Results")
        print("KeyError")
        return ""
