from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return{
        "name": "홍길동",
        "role": "ㄱㄴ소로ㅓ",
        "status":"ㅗ허ㅓ옥ㄳ",
        "skills": ["Ubuntu","VS Code", "Python", "Flask"]
    }

if __name__ == '__main__':
    app.run(debug=True)