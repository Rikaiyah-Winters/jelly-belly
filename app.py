from flask import Flask, render_template, request
import requests
import json

# Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def jelly_belly_info():
  response = requests.get("https://jellybellywikiapi.onrender.com/api/Beans")
  response.raise_for_status()  # Check if the request was successful
  response_data = response.json() #jsonifies the data
  beans_info = response_data["items"] 
  return render_template("jellybeans.html", beans = beans_info)
  

# Run the flask server
if __name__ == "__main__":
    app.run()