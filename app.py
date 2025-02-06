from flask import Flask, render_template, request
import requests
import json

# Initialize the Flask application
app = Flask(__name__)

@app.route("/", methods=["GET"])
def jelly_belly_info():
  response = requests.get("https://jelly-belly-wiki.netlify.app/api/beans?groupName=Jelly%20Belly%20Official%20Flavors")
  respnonse_data = response.json()
  jelly_beans = json.loads(respnonse_data)
  print(jelly_beans)
  return render_template("/jellybeans.html")

# Run the flask server
if __name__ == "__main__":
    app.run()