from crypt import methods
from flask import Flask, render_template, redirect, request
# import the class from friend.py
from user import User


app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    return render_template("new.html")
            
@app.route("/users", methods=["POST"])
def users():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        # "created_at" : request.form["created_at"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    return redirect("/user")

@app.route('/user', methods=["GET"])
def user():
    users = User.get_all()
    return render_template('users.html', users = users)
if __name__ == "__main__":
    app.run(debug=True)




