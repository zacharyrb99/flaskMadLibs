from flask import Flask, request, render_template
from stories import stories

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', stories = stories.values())

@app.route('/form')
def get_prompts():
    id = request.args["id"]
    story = stories[id]

    prompts = story.prompts
    
    return render_template('form.html', id = id, title = story.title, prompts = prompts)

@app.route('/story')
def make_story():
    id = request.args["id"]
    story = stories[id]

    story_text = story.generate(request.args)
    return render_template("story.html", title = story.title, story_text=story_text)