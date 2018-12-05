#!/usr/bin/python3

import request
from flask import Flask
app = Flask(__name__)

# @app.route('/user/<username>')
# def show_user_profile():
#     return 'User %s' % username

# @app.route('/post/<int:post_id>')
# def show_post():
#     return 'Post_id is %d' % post_id

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "PSOT":
        return "Post"
    else:
        return "Get"    

if __name__ == '__main__':
    app.run(debug= True)
