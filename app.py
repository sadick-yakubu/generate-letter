import os
from flask import Flask, render_template, render_template_string, make_response, url_for, request
from jinja2 import Template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/firstClassOrdinary')
def firstClassOrdinary():
    return render_template('firstClassOrdinary.html')


@app.route('/firstClassExcellent')
def firstClassExcellent():
    return render_template('firstClassExcellent.html')


@app.route('/upperExcellent')
def upperExcellent():
    return render_template('upperExcellent.html')

@app.route('/upperOrdinary')
def upperOrdinary():
    return render_template('upperOrdinary.html')


@app.route('/generate_letter', methods=['POST'])
def generate_letter():
    # User Inputs from Form
    selected_template = request.form['template']
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    fullName = request.form['fullName']
    gender = request.form['gender']
    rank = request.form['rank']
    position = request.form['position']
    projectTitle = request.form['projectTitle']
    cwa = request.form['cwa']
    years = request.form['years']
    gradYear = request.form['gradYear']
    progStudied = request.form['progStudied']
    progApplying = request.form['progApplying']
    schoolApplying = request.form['schoolApplying']
    comments = request.form['comments']
    receiversAddress = request.form['receiversAddress']
    receiversAddress = receiversAddress.replace('\n', ' <br> ')
    acaYear = int (gradYear) + 1

    # Get the current date
    letter_date = datetime.now().strftime('%B %d, %Y')
    letter_year = datetime.now().strftime('%Y')    
    # Load selected template
    template_filename = f"{selected_template}.html"
    with open(os.path.join("templates", template_filename), 'r') as template_file:
        letter_content = template_file.read()
    # Render the selected template with user data
    rendered_template = render_template_string(letter_content, fullName=fullName, firstName=firstName, lastName=lastName, gender= gender, rank=rank, years=years, position=position, gradYear=gradYear, progStudied=progStudied, progApplying=progApplying, schoolApplying=schoolApplying, comments=comments, receiversAddress=receiversAddress, letter_date=letter_date, letter_year=letter_year, projectTitle=projectTitle, cwa=cwa, acaYear=acaYear)
    # Generate PDF using WeasyPrint library
    from weasyprint import HTML
    from flask_weasyprint import HTML
    pdf = HTML(string=rendered_template).write_pdf(presentational_hints=True);

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=Recommendation_Letter.pdf'

    return response

if __name__ == '__main__':
    app.run(debug=True)

