from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def index():
    random_number: int = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route('/guess/<name>')
def guess(name: str):
    gender = None
    res_gender = requests.get(url=f"https://api.genderize.io?name={name}")
    if res_gender.status_code == 200:
        res_data_gender = res_gender.json()
        gender = res_data_gender["gender"]
    else:
        print("Error fetching data from API (genderize)")

    age = None
    res_age = requests.get(url=f"https://api.agify.io?name={name}")
    if res_age.status_code == 200:
        res_data_age = res_age.json()
        age = res_data_age["age"]
    else:
        print("Error fetching data from API (agify)")

    return render_template("guess.html", person_name=name, person_gender=gender, person_age=age)


@app.route('/blog/<num>')
def get_blog(num: str):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
