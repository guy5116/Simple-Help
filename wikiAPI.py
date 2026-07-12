import requests
from ddgs import DDGS
from textReader import readText
import os

def PARAMSS(target):
    # Generic API request setup
    S = requests.Session()
    S.headers.update({
        'User-Agent': f'{os.getenv("wiki_api_agent")}'
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
    return S.get(URL, params=PARAMS)

def getData(debug, target):
    try:
        R = PARAMSS(target)
        data = R.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return ""
    except requests.exceptions.Timeout as e:
        print(e)
        return ""
    except requests.exceptions.ConnectionError as e:
        print(e)
        return ""
    except requests.exceptions.TooManyRedirects as e:
        print(e)
        return ""
    except requests.exceptions.RequestException as e:
        print(e)
        return ""

    #Convert Request into JSON (data) and handle Errors
    try:
        data = R.json()
    except ValueError:
        print("Value Error")
        return ""

    if debug: debuger(R)
    return data

def debuger(R):
    print("Wiki API Debug Info:\n")
    print(R.url)
    print(R.history)
    print(R.status_code)
    print(R.headers.get("Content-Type"))
    print(R.text[:500])

def summary(data, debug, attempt, target):
    print("Wiki API Summary:\n")
    try:
        page = next(iter(data['query']['pages'].values()))
        if debug: print(page)
        print(page['extract'])
    except KeyError:
        if debug: print("Wiki FAILURE\nAttempting DDG Search")
        try:
            with DDGS() as ddgs:
                if attempt > 3: return ""
                result = ddgs.text(f'site:wikipedia.org {target}')
                result = result[0]['href']
                attempt = attempt + 1
                wikiAPI(debug, result[30:].replace('_'," "), attempt)
        except StopIteration:
            print("No Results")
        print("KeyError")
        return ""

def wikiAPI(debug, target, attempt):
    print("TARGET:   " + target)
    if debug: print(f"The Action is 'Explain' and the Target is '{target}'")
    #Attempt to retrieve information from the WikiAPI and handle Errors
    data = getData(debug, target)
    try:
        data = getData(debug, target)
    except:
        return
    summary(data, debug, attempt, target)
    return

