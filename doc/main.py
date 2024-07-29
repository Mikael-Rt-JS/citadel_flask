from flask import Flask,render_template,request,make_response,session,url_for

main=Flask(__name__)


@main.route('/')
@main.route('/home')
@main.route('/index')
def home():
    return render_template('home.html')

if __name__=="__main__":
    main.run(debug=True)