from flask import Flask, render_template, request, jsonify
import json
import subprocess
from subprocess import Popen, PIPE

app = Flask(__name__)

# disable caching this may hinder working with css
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0




@app.route('/', methods = ['POST','GET'])
def index():
    return render_template('index.html')


def get_shell_script_output_using_communicate(fl):
    cmd = 'python3 ' + fl
    # print(cmd)
    session = Popen(cmd,shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = session.communicate()
    # if stderr:
        # raise Exception("Error "+str(stderr))
    # if stderr:
    #     return stderr.decode('utf-8') + stdout.decode('utf-8')
    # return stdout.decode('utf-8')
    return {
        "error" : stderr.decode('utf-8'),
        "output" : stdout.decode('utf-8')
    }


@app.route('/run', methods=['POST'])
def run():
    data = json.loads(request.data)
    print(data["code"])
    with open('A.py','w') as f:
        f.write(data["code"])
    res = get_shell_script_output_using_communicate('A.py')
    return jsonify(res)


@app.route('/runinput', methods=['POST'])
def runinput():
    data = json.loads(request.data)
    # print(data['str'])
    # print(data['mod'])
    fl = 'multpython.py'
    if data['mod'] == 'lstm':
        fl = 'lstmpython.py'
    with open('inpstring.txt','w') as f:
        f.write(data['str'])
    res = get_shell_script_output_using_communicate(fl)
    print(jsonify(res))
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True)
