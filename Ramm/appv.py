# from flask import Flask, request
# # import flask 
# import flask
# from flask import Flask, render_template, request, send_file
# app = Flask(__name__)

# @app.route('/submit', methods=['POST'])
# def submit():
#     data = {
#         "Bundle_Number": request.form.get('bundleNumber'),
#         "Teacher": request.form.get('teacher'),
#         "Academic_year_start": request.form.get('academicYearStart'),
#         "Academic_year_end": request.form.get('academicYearEnd'),
#         "Semester": int(request.form.get('semester')),
#         "Branch": request.form.get('branch'),
#         "Batch": int(request.form.get('batch')),
#         "Section": request.form.get('section'),
#         "Subject_Code": request.form.get('subjectCode'),
#         "Subject_Name": request.form.get('subjectName'),
#         "Number_of_Students": int(request.form.get('numberOfStudents')),
#         "Number_of_COs": int(request.form.get('numberOfCOs')),
#         "Internal": float(request.form.get('internal')),
#         "External": float(request.form.get('external')),
#         "Direct": float(request.form.get('direct')),
#         "Indirect": float(request.form.get('indirect')),
#         "defaulThreshold": float(request.form.get('defaultThreshold'))
#         # Continue this for all your fields...
#     }

#     num_components = int(request.form.get('numberOfComponents'))
#     Component_Details = {}
#     for i in range(1, num_components+1):
#         Component_Details[request.form.get('componentName'+str(i))] = {"Number_of_questions": request.form.get('componentValue'+str(i))}

#     print("Data:", data)
#     print("Component Details:", Component_Details)

#     return "Data received"

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indexv8_7_2_1.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "Bundle_Number": str(request.form.get('bundleNumber')),
        # similarly for teacher]
        "Teacher": str(request.form.get('teacher')),
        "Academic_year": str(request.form.get('academicYearStart')) + "-" + str(request.form.get('academicYearEnd')),
        "Semester": int(request.form.get('semester')),
        "Branch": str(request.form.get('branch')),
        "Batch": int(request.form.get('batch')),
        "Section": str(request.form.get('section')),
        "Subject_Code": str(request.form.get('subjectCode')),
        "Subject_Name": str(request.form.get('subjectName')),
        "Number_of_Students": int(request.form.get('numberOfStudents')),
        "Number_of_COs": int(request.form.get('numberOfCOs')),
        "Internal": float(request.form.get('internal')),
        "External": float(request.form.get('external')),
        "Direct": float(request.form.get('direct')),
        "Indirect": float(request.form.get('indirect')),
        "Default threshold %": float(request.form.get('defaultThreshold'))
        # Continue this for all your fields...
    }

    num_components = int(request.form.get('numberOfComponents'))
    Component_Details = {}
    for i in range(1, num_components+1):
        Component_Details[request.form.get('componentName'+str(i))] = {"Number_of_questions": int(request.form.get('componentValue'+str(i)))}

    print("Data=", data)
    print("ComponentDetails=", Component_Details)

    return "Data received"

if __name__ == '__main__':
    app.run(debug=True)
