import json
from flask import Flask, request #import main Flask class and request object

app = Flask(__name__)

data = {}
data['str'] = []

@app.route('/test_valid')
def test_valid():
    valid = request.args.get('string') #if key doesn't exist, returns None

    # Open the changed JSON file
    try:
        with open("../data.json") as f:
            data_new = json.load(f, strict=False)
    except:
        pass
    # Generating the emails based on the JSON templates
    # print (len(data_new))
    i = 0
    final = 0
    try:
        while data_new["str"][i]["name"] is not None:
            # print ("i="+str(i))
            # print(data_new["str"][i]["name"])

            if (data_new["str"][i]["name"] == valid):
                print ("YESS")
                final = 1
                i = i + 1
            else:
                print("NOOO")
                i = i + 1
    except:
        pass

    if (final==1):
        return '''CCSC{2e2d1e1d0_But_th15_0n3_1t_w027h5_1t!_67aa06aa1b}'''
    else:
        return '''NO FLAG'''
    # return '''<h1>The flag value is: {}</h1>'''.format(valid)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')