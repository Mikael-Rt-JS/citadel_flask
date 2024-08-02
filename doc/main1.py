from flask import Flask,render_template,request,make_response,session,redirect,jsonify
import os
# БЕЗОПАСНОСТЬ ФАЙЛОВОЙ СИСТЕМЫ
# from werkzeug.utils import secure_filename
# https://www.youtube.com/watch?v=oSNc_ZRWNzI
from citadel.sessioner import Session

UPLOAD_FOLDER = "./static/upload/images/"
#/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

main=Flask(__name__)
main.config['SECRET_KEY']='3e807657127214ede4618d938d613d64083ea834'
main.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@main.route('/',methods=['POST','GET'])
@main.route('/home',methods=['POST','GET'])
@main.route('/index',methods=['POST','GET'])
def home():
    if request.method=='POST':
        title=request.form['name']
        
        print(title)
        # ввидке любое название ключа для передачи в шаблок можешь и массив
        return render_template('home.html',name=title)
    else:
        return render_template('home.html')

@main.route('/upload_file',methods=['POST','GET'])
def upload_file():
    if request.method == 'POST':
        if 'files' not in request.files:
            return 'Have not files.'
            # https://myrusakov.ru/python-flask-file-upload.html
            # https://django.fun/docs/flask/2.2/patterns/fileuploads/

        #ОБЕЗОПАСИМ ФАЙЛОВУЮ СИСТЕМУ С ПОМОЩЬЮ secure_filename
        # загрузка одной картинки
        # file = request.files['files']
        # path = os.path.join(main.config['UPLOAD_FOLDER'], file.filename)
        # file.save(path)

        # return render_template('home.html')

        uploaded_files = request.files.getlist("files")
        for uploaded_file in uploaded_files:
            filename = uploaded_file.filename
            file_path = os.path.join(main.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(file_path)
        return render_template('home.html')

if __name__=="__main__":
    main.run(debug=True)

    # https://flask.palletsprojects.com/en/2.3.x/patterns/javascript/
