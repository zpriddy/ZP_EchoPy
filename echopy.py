#! /usr/bin/python
#################################################
#		Alexa Skills Kit Hello World			#
#################################################
# Zachary Priddy - 2015 						#
# me@zpriddy.com 								#
#												#
# Features: 									#
#################################################
#################################################

import os
import echopy_app
import echopy_doc
import echopy_helloworld as myApp
from flask import Flask, render_template, Response, send_from_directory, request, current_app, redirect, jsonify, json


app = Flask(__name__)


@app.route("/")
def main():
	return echopy_doc.main_page


@app.route("/EchoPyAPI",methods = ['GET','POST'])
def apicalls():
	if request.method == 'POST':
		data = request.get_json()
		print "POST"
		sessionId = myApp.data_handler(data)
		return sessionId + "\n"




def run_echopy_app():
	import SocketServer
	SocketServer.ThreadingTCPServer.allow_reuse_address = True
	echopy_app.run(app)


if __name__ == "__main__":
	myApp.data_init()
	run_echopy_app()
