from flask import Flask, render_template, request
import requests
import json

# Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def jelly_belly_info():
  try:
    response = requests.get("https://jellybellywikiapi.onrender.com/api/beans/1")
    response.raise_for_status()  # Check if the request was successful
    response_data = response.json()
    jelly_beans = json.dumps(response_data, indent=2)  # Pretty print the JSON response
  except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
  #except requests.exceptions.RequestException as err:
    #print(f"Other error occurred: {err}")
  #except json.JSONDecodeError as json_err:
    #print(f"JSON decode error: {json_err}")
  return render_template("jellybeans.html", data = jelly_beans)
  

# Run the flask server
if __name__ == "__main__":
    app.run()