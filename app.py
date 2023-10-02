import os
from flask import Flask, render_template, render_template_string, make_response, url_for, request
from jinja2 import Template

app = Flask(__name__)
app.static_folder='static'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/firstClassOrdinary')
def firstClassOrdinary():
    return render_template('firstClassOrdinary.html')

@app.route('/generate_letter', methods=['POST'])
def generate_letter():
    # User Inputs from Form
    selected_template = request.form['template']
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    fullName = request.form['fullName']
    gender = request.form['gender']
    rank = request.form['rank']
    years = request.form['years']
    gradYear = request.form['gradYear']
    progStudied = request.form['progStudied']
    progApplying = request.form['progApplying']
    schoolApplying = request.form['schoolApplying']
    comments = request.form['comments']
    receiversAddress = request.form['receiversAddress']

    # Load selected template
    template_filename = f"{selected_template}.html"
    with open(os.path.join("templates", template_filename), 'r') as template_file:
        letter_content = template_file.read()
    # Render the selected template with user data
    rendered_template = render_template_string(letter_content, fullName=fullName, firstName=firstName, lastName=lastName, gender= gender, rank=rank, years=years, gradYear=gradYear, progStudied=progStudied, progApplying=progApplying, schoolApplying=schoolApplying, comments=comments, receiversAddress=receiversAddress)

    # Generate PDF using WeasyPrint library
    from weasyprint import HTML
    pdf = HTML(string=rendered_template).write_pdf(presentational_hints=True);

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=pdf.pdf'

    return response

if __name__ == '__main__':
    app.run(debug=True)