from flask import Flask, render_template, request
import requests
from bean_flavors import prettify_bean_flavor

# Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def jelly_belly_info():
  #errors = []
  response = requests.get("https://jellybellywikiapi.onrender.com/api/Beans")
  #response.raise_for_status()
  response_data = response.json()
  beans_info = response_data["items"]
  sevenup_info = beans_info[0]
  return render_template("jellybeans.html", beans = beans_info, sevenup_info = sevenup_info)
  
      

# Run the flask server
if __name__ == "__main__":
    app.run()