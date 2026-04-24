from flask import Flask,render_template,request,redirect

app = Flask(__name__)
messages = []

@app.route('/')
def home():
    skills = [
        "C", "C++", "C#", "Java", "Kotlin",
        "JavaScript", "TypeScript",
        "Python", "Rust", "Go",
        "Ruby", "PHP",
        "HTML", "CSS", "Markdown",
        "SQL", "R",
        "Bash", "Shell",
        "Dart", "Swift"
    ]
    return render_template('index.html', skills=skills, messages=messages)


@app.route('/send', methods=['POST'])
def send():
    skill = request.form.get('skill')
    level = request.form.get('level')
    status = request.form.get('status')

    messages.append(skill + " / " + level + " / " + status)

    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)