from flask import Flask, render_template, request
import requests
import json
from bean_flavors import prettify_bean_flavor

# Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def jelly_belly_info():
  errors = []
  if request.method == "POST":
    bean_flavor = request.form.get("bean-flavor")
    if not bean_flavor:
      errors.append("Oops! Please choose a jelly bean flavor!")
    if bean_flavor:
      response = requests.get("https://jellybellywikiapi.onrender.com/api/Beans")
      #response.raise_for_status() # Check if the request was successful
      response_data = response.json() #jsonifies the data
      beans_info = response_data["items"] 
      return render_template("jellybeans.html", bean_nom=prettify_bean_flavor(bean_flavor), errors=[])
  return render_template("jellybeans.html", beans = [], bean_nom="", errors=errors)
  

# Run the flask server
if __name__ == "__main__":
    app.run()