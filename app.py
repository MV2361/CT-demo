# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:58:23 2022

@author: mayan
"""

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET']) 
def main():
	return render_template("index.html")


@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        pre=1
        Project_title = request.form["Project title"]
        fed_learning = request.form["fed_learning"]
        
    return render_template("index.html", prediction = pre, Project_title = Project_title ,fed_learning= fed_learning)

if __name__ =='__main__':
	#app.debug = True
	app.run(host='0.0.0.0' , port=8080)