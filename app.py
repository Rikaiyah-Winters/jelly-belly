from flask import Flask, render_template, request
import requests
from bean_flavors import prettify_bean_flavor

# Initialize the Flask application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def jelly_belly_info():
  if request.method == "POST":
    chosen_bean = request.form.get("bean-flavor")
    if chosen_bean:
      response = requests.get("https://jellybellywikiapi.onrender.com/api/Beans")
      #response.raise_for_status()
      response_data = response.json()
      beans_info = response_data["items"]
      chosen_bean_info = next((bean for bean in beans_info if bean['beanId'] == str(chosen_bean)), None)
      return render_template("jellybeans.html", bean=chosen_bean_info)
  return render_template("jellybeans.html", bean=[])
  
      

# Run the flask server
if __name__ == "__main__":
    app.run()