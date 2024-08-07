#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    question1 = request.form.get('question1')
    question2 = request.form.get('question2')
    question3 = request.form.get('question3')
    question4 = request.form.get('question4')
    question5 = request.form.get('question5')
    question6 = request.form.get('question6')
    question7 = request.form.get('question7')
    question8 = request.form.get('question8')
    question9 = request.form.get('question9')
    question10 = request.form.get('question10')

    return render_template('index.html', question1=question1,
                           question2=question2,
                           question3=question3,
                           question4=question4,
                           question5=question5,
                           question6=question6,
                           question7=question7,
                           question8=question8,
                           question9=question9,
                           question10=question10)


if __name__ == "__main__":
    app.run(debug=True)