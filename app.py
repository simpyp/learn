from flask import Flask,render_template,redirect,url_for
import os,os.path,json
app = Flask(__name__)

@app.route('/')
def index():
    path = '/home/shiyanlou/files/'
    filelist = []
    titlelist = [] 
    files = os.listdir(path)
    for file in files:
        if file.endswith('.json'):
            file = path + file
            filelist.append(file)
    if len(filelist) > 0 :
        for file in filelist:
            with open(file,'r') as f:
               data  = json.load(f)
            title = data['title']
            titlelist.append(title)
    else:
        print('there is no json file')
    print('titles should be list:',titlelist)
    return render_template('index.html',titlelist=titlelist)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@app.route('/files/<filename>')
def file(filename):
    file_name = '/home/shiyanlou/files/'+filename +'.json'
    print('filename:',file_name)
    if os.path.isfile(file_name):
        print("yeeeeeeeee")
        with open(file_name,'r') as f:
            data = json.load(f)
        return render_template('file.html',data=data)
    else:
#        return redirect(url_for('not_found'))
#        abort(404)
        return "errrr"


if __name__ == '__main__':
    app.run()

