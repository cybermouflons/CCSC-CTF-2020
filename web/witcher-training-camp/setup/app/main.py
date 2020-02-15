from flask import Flask, render_template, request, send_file
from flask_assets import Bundle, Environment

import tempfile
from pychromepdf import ChromePDF

bundles = {
    'application_css': Bundle(
        'application.css',
        output='gen/application.css'
    )
}


app = Flask(__name__, static_folder='static')
assets = Environment(app)
assets.register(bundles)

# change to your chrome executable path
PATH_TO_CHROME_EXE = '/usr/bin/google-chrome-stable'
cpdf = ChromePDF(PATH_TO_CHROME_EXE)
cpdf._chrome_args = list(cpdf._chrome_args)
cpdf._chrome_args.append("--no-sandbox")

@app.route("/", methods=["GET"])
def application():
    return render_template('application.html')

@app.route("/enroll", methods=["POST"])
def enroll():
    params = ["full_name", "specialty", "picture", "origin"]
    validation_errors = [request.form.get(p, None) is None or request.form[p]  == "" for p in params]
    if any(validation_errors):
        return {"error": "All parameters are required!"}, 400

     # get the rendered html as string using the template
    rendered_html = render_template(
        'pdf_template.html',
        full_name=request.form["full_name"],
        origin=request.form["origin"],
        specialty=request.form["specialty"],
        picture=request.form["picture"]
    )

    # create a temporary output file which will be deleted when closed
    with tempfile.NamedTemporaryFile(suffix='.pdf') as output_file:

        # create a pdf from the rendered html and write it to output_file
        if cpdf.html_to_pdf(rendered_html,output_file):
            print("PDF generated successfully: {0}".format(output_file.name))

            try:
                # send the file to user
                return send_file(output_file.name,attachment_filename='awesome.pdf')
            except Exception as e:
                return str(e)
        else:
            print("Error creating PDF")

    return "Error"

    # return request.form

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8080)