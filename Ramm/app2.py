from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = {
            "Bundle_Number": request.form["bundle_number"], # String
            "Teacher_Name": request.form["teacher"],   # String
            "Academic_year_start": request.form["academic_year_start"],
            "Academic_year_end": request.form["academic_year_end"],
            "Semester": int(request.form["semester"]),
            "Branch": request.form["branch"],               # String
            "Batch": int(request.form["batch"]),
            "Section": request.form["section"],             # String
            "Subject_Code": request.form["subject_code"],   # String
            "Subject_Name": request.form["subject_name"],
            "Number_of_COs": int(request.form["number_of_cos"]),
            "Internal": float(request.form["internal"]),
            "External": float(request.form["external"]),
            "Direct": float(request.form["direct"]),
            "Indirect": float(request.form["indirect"])
        }

        components = []
        num_components = int(request.form["number_of_components"])
        for i in range(num_components):
            component_name = request.form[f"component_{i}_name"]        # String
            num_questions_str = request.form[f"component_{i}_num_questions"]
            num_questions = int(num_questions_str) if num_questions_str else 0  # Integer
            components.append({"name": component_name, "questions": num_questions})


        # Print the data dictionary and components
        print("Data:")
        for key, value in data.items():
            print(f"{key}: {value}")
        
        print("\nComponents:")
        for i, component in enumerate(components, 1):
            print(f"Component {i}: {component['name']} - {component['questions']} questions")

        return "Data submitted and printed in the console. Check the console output."
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
