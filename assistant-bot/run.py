from flask import Flask, request, redirect
import twilio.twiml
import os
import urllib
import zipfile
import string
import random
import aiml

# Start of chatbot codes

# dictionary = zipfile.ZipFile("./dictionary.zip", "r").open("./dictionary.txt", "r")
#dictionary = zipfile.ZipFile("./dictionary.zip", "r").open("./dictionary.txt", "r")

dictionary = open("./assistant-bot/dictionary.txt")

# dictionary = zipfile.ZipFile("./dictionary.zip", "r").open("./dictionary.txt", "r")

#dictionary = zipfile.ZipFile("./dictionary.zip", "r").open("./dictionary.txt", "r")
#dictionary = open("dictionary.txt", "r")
#   Dictionary format:
#   "English", word, type, "#", Definition

greeting = ["Hey", "Hi", "Hello", "Whats up", "Yo"]
farewell = ["Goodbye", "Bye", "See you later", "Farewell"]
thanks = ["Thanks", "Thank you", "Thanks a lot"]
questions = ["What do you think about {0}?", "I don't really like {0}. Do you?", "I like {0}, don't you?", "Why do you say {0}?"]

topic = "Nothing"

k = aiml.Kernel()
k.learn("./aiml2.xml")

def talk(a):

    a = a.capitalize()
    wordList = a.split(" ")

    if a in greeting:
        return greeting[random.randint(0,4)]

    elif a in farewell:
        endConversation()

    elif a in thanks:
        return "No problem"

    elif a == "What are you thinking about":
        return topic

    elif (wordList[0] == "What") and (wordList[1] == "are" or "is") and (wordList[2] != "your"):
        wordDefinition(wordList[-1])

    elif "weather" in wordList:
        discussWeather()

    elif "i think" in a.lower():
        return "Why do you think that?"

    elif a.lower().split(" ")[0] == "yes":
        return "That's good"

    elif a.lower().split(" ")[0] == "no":
        return "Really?"

    elif isStatement(a):
        return questions[random.randint(0, 3)].format(getNoun(a))

    elif a.endswith("?"):
        if a.lower().startswith("why"):
            return "I don't know, how{0}".format(getWhyQuestionChunk(a.lower()))
        elif "are you a" in a.lower():
            return ["yes", "no"][random.randint(0, 1)]
        else:
            return "I don't know, {0}".format(a.lower())

    else:
        b = a.upper()
        k.respond(b)
        return k.respond(a)


        #print ["yep", "really?"][random.randint(0, 1)]

    talk(raw_input())

def getWhyQuestionChunk(s):
    chunk = s.lower()

    if chunk.startswith("why"):
        chunk = chunk.replace("why", "", 1)

    if chunk.startswith("do"):
        chunk = chunk.replace("do", "", 1)

    if chunk.startswith("are"):
        chunk = chunk.replace("are", "", 1)
        return "hit"
    return chunk

def isStatement(s):
    first = s.split(" ")[0].lower()

    a = first != "what" and first != "how" and first != "why" and first != "who" and first != "where" and not s.endswith("?")
    #print a
    return a

def getNoun(s):
    words = s.split(" ")

    #get the first noun in the sentence
    for word in words:
        lower = word.lower()
        if lower != "a" and lower != "an" and lower != "the" and lower != "i" and lower != "he" and lower != "you" and lower != "she" and lower != "we":
            for line in dictionary:
                defList = line.split()
                if(lower == defList[1].lower() and (defList[2] == "Noun" or defList[2] == "Proper")): return word #"Proper Noun"s are also nouns
    return "that"

def endConversation():
    return farewell[random.randint(0,3)]
    exit()

def wordDefinition(b):
    answer = "I don't know"
    for line in dictionary:
        defList = line.split()
        if (b == defList[1]) and (defList[2] == "Noun"):
            s = str(defList[4:])    #puts everything from the 4th line onward into a string
            answer = "Its " + "".join(c for c in s if c.isalnum() or c.isspace())  #Removes symbols
            topic = b
            break
    return answer

def discussWeather():
    weatherData = urllib.urlopen("http://rss.wunderground.com/auto/rss_full/MD/Frederick.xml?units=english")
    for line in weatherData:
        if "Current Conditions" in line:
            conditions = line.split(":")
            conditions = conditions[1].split("-")
            return "Its pretty nice. Its " + conditions[0]

# end of chatbot code

app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+19799857131": "Audi",
    "+19799857132": "Atif",
    "+19799857169": "Alok",
}

@app.route("/", methods=['GET', 'POST'])
def communicator():
    """Respond and greet the caller by name."""

    from_number = request.values.get('From', None)
    message_body = request.values.get('Body', "")

    if from_number in callers:
        message = callers[from_number] + ", thanks for the message:" + message_body + "!"
    else:
        message = "Buddy, thanks for the message!" + message_body


    message = talk(message_body)


    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(debug=True)
