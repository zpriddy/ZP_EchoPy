import json
appVersion = 1.0


def data_init():
	global MyDataStore
	MyDataStore = DataStore()



def data_handler(rawdata):
	global MyDataStore
	#print rawdata['session']
	currentSession = MyDataStore.getSession(rawdata['session'])
	currentRequest = rawdata['request']
	response = request_handler(currentSession, currentRequest)


	#print json.dumps({"version":appVersion,"response":response},sort_keys=True,indent=4)

	return json.dumps({"version":appVersion,"response":response},indent=2,sort_keys=True)


def request_handler(session, request):
	requestType = request['type']
	
	if requestType == "LaunchRequest":
		return launch_request(session, request)
	elif requestType == "IntentRequest":
		return intent_request(session,request)


def launch_request(session, request):
	output_speech = "Welcome to the Alexa Skills Kit, you can say hello"
	output_type = "PlainText"

	card_type = "Simple"
	card_title = "HelloWorld - Title"
	card_content = "HelloWorld - Content"

	response = {"outputSpeech": {"type":output_type,"text":output_speech},"card":{"type":card_type,"title":card_title,"content":card_content},'shouldEndSession':False}

	return response

def intent_request(session,request):
	print "intent_request"
	if request['intent']['name'] == "HelloWorldIntent":
		output_speech = "Hellow World!"
		output_type = "PlainText"

		card_type = "Simple"
		card_title = "HelloWorld - Title"
		card_content = "HelloWorld - Content"

		response = {"outputSpeech": {"type":output_type,"text":output_speech},"card":{"type":card_type,"title":card_title,"content":card_content},'shouldEndSession':True}

		return response
	else:
		return launch_request(session, request) ##Just do the same thing as launch request





class Session:
	def __init__(self,sessionData):
		self.sessionId = sessionData['sessionId']


	def getSessionID(self):
		return self.sessionId

class DataStore:
	def __init__(self):
		self.sessions = {}

	def getSession(self,session):
		if session['new'] is True or session['sessionId'] not in self.sessions:
			self.sessions[session['sessionId']] = Session(session)

		return self.sessions[session['sessionId']]
