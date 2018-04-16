from flask import Flask, request
import subprocess

# Ejemplo llamada
# http://127.0.0.1:5000/talk?msg=hola%20que%20tal%20estas&lang=spanish

app = Flask(__name__)


@app.route('/talk', methods = ['GET', 'POST'])
def index():
    msg = request.args['msg']
    lang = request.args['lang']
 
    subprocess.call('echo "'+msg+'" | festival --language '+lang+' --tts', shell=True)
    #process = subprocess.Popen( 'echo "'+msg+'" | festival --language '+lang+' --tts', shell=True, stdout=subprocess.PIPE)
    #process.wait()

    #return 'echo "'+msg+'" | festival --language '+lang+' --tts'
    return '<br>'


if __name__ == '__main__':
    app.run(host = '192.168.2.57')
