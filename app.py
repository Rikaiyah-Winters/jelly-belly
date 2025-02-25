from flask import Flask, render_template, request
import requests
from bean_flavors import prettify_bean_flavor

# Initialize the Flask application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def jelly_belly_info():
  errors=[]
  if request.method == "POST":
    chosen_bean = request.form.get("bean-flavor")
    if not chosen_bean:
      errors.append("Please choose a Jelly Bean Flavor")
      return render_template("jellybeans.html", bean=[], errors=errors)
    chosen_bean = int(chosen_bean)
    if chosen_bean < 11:
      response = requests.get("https://jellybellywikiapi.onrender.com/api/Beans?pageIndex=1")
      #response.raise_for_status()
      response_data = response.json()
      beans_info = response_data["items"]
      chosen_bean_info = next((bean for bean in beans_info if bean['beanId'] == int(chosen_bean)), None)
      return render_template("jellybeans.html", bean=chosen_bean_info)
    #if chosen_bean < 21:
      #response = requests.get("https://jellybellywikiapi.onrender.com/api/Beans?pageIndex=2")
      #response.raise_for_status()
      #response_data = response.json()
      #beans_info = response_data["items"]
      #chosen_bean_info = next((bean for bean in beans_info if bean['beanId'] == int(chosen_bean)), None)
      #return render_template("jellybeans.html", bean=chosen_bean_info, errors=[])
  return render_template("jellybeans.html", bean=[], errors=errors)
      

# Run the flask server
if __name__ == "__main__":
    app.run()