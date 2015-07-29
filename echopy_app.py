#! /usr/bin/python
#################################################
#       Alexa Skills Kit Hello World            #
#################################################
# Zachary Priddy - 2015                         #
# me@zpriddy.com                                #
#                                               #
# Features:                                     #
#################################################
#################################################
def run(app):

    try:
        app.run(debug=True,
                port=5000,
                threaded=True,
                use_reloader=False,
                use_debugger=True,
                host='0.0.0.0'
                )
    finally:
        print "Disconnecting clients"

    print "Done"