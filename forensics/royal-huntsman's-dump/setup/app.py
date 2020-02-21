from flask import Flask, request #import main Flask class and request object

app = Flask(__name__)

@app.route('/32c1eb3a605f4006370eb2028f44389552e3507f/Th3W1tchER/Str1Ga')        
def get_flag():
    return '''CCSC{NoB0dy_5m4rT_pL4ys_fA1R}'''

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
