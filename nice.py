from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

DISSES = ['smelly', 'annoying', 'just awful', 'not cool']

@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html><a href=\"/hello\">Hi!</a> This is the home page.<html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="pesron"></label>
          Select a compliment:
            <select name="compliment">
              <option value="smart">Smart</option>
              <option value="radiant">Radiant</option>
              <option value="brave">Brave</option>
            </select>
          <input type="submit">
        </form>
        <form action="/diss">
          <label>What's your name? <input type="text" name="person"></label>
          
          <input type="submit" value="Diss Me">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = choice(DISSES)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A DISS! (You picked it)</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
