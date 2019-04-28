from flask import Flask, render_template, request, redirect

app_test = Flask(__name__, template_folder='templates') #automatically looks for template in the templates/ directory or specify here.

app_test.vars={}
app_test.questions={}
app_test.questions['How many schools have you attended?']=('<2','2','>2')
app_test.questions['How many meals do you have in a day']=('<2','2','>2')
app_test.nquestions = len(app_test.questions)

#Flask puts the server on port 5000 by default.
@app_test.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        nquestions=app_test.nquestions
        return render_template('userinformation.html', num=nquestions) 
    else:
        app_test.vars['name']=request.form['name']
        app_test.vars['age']=request.form['age']

        f = open('%s_%s.txt'%(app_test.vars['name'], app_test.vars['age']), 'w')
        f.write('name: %s\n'%app_test.vars['name'])
        f.write('age: %s\n'%app_test.vars['age'])
        f.close()

        # return 'Request method was not GET!'
        return redirect('/main')

@app_test.route('/main')
def main_fn():
    if len(app_test.questions)==0:
        return render_template('end.html')
    else:
        return redirect('/next')

@app_test.route('/next', methods=['GET','POST'])
def next():
    if request.method == 'GET':
        n = app_test.nquestions - len(app_test.questions) + 1
        q = list(app_test.questions.keys())[0]
        ans1, ans2, ans3 =  app_test.questions[q]
        print('Answers are: ', ans1, ans2, ans3)
        app_test.currentq = q
        return render_template('layout.html', num=n, question=app_test.currentq, ans1=ans1, ans2=ans2, ans3=ans3)
    if request.method == 'POST':
        f = open('%s_%s.txt'%(app_test.vars['name'], app_test.vars['age']), 'a')
        f.write('Question: %s\n'%(app_test.currentq))
        f.write('Answer: %s\n\n'%(request.form['answer_from_layout']))
        f.close()
        del app_test.questions[app_test.currentq]
        return redirect('/main')

if __name__ == '__main__':
    app_test.run(debug=True)
