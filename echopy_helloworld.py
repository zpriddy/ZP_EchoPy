import json
appVersion = 1.0


def data_init():
	global MyDataStore
	MyDataStore = DataStore()



def data_handler(rawdata):
	global MyDataStore
	#print rawdata['session']
	currentSession = MyDataStore.getSession(rawdata['session'])
	currentUser = MyDataStore.getUser(rawdata['session'])
	currentRequest = rawdata['request']
	response = request_handler(currentSession, currentUser, currentRequest)


	#print json.dumps({"version":appVersion,"response":response},sort_keys=True,indent=4)

	return json.dumps({"version":appVersion,"response":response},indent=2,sort_keys=True)


def request_handler(session, user, request):
	requestType = request['type']
	
	if requestType == "LaunchRequest":
		return launch_request(session, user, request)
	elif requestType == "IntentRequest":
		return intent_request(session, user, request)


def launch_request(session, user, request):
	output_speech = "Welcome to the Alexa Skills Kit, you can say hello"
	output_type = "PlainText"

	card_type = "Simple"
	card_title = "HelloWorld - Title"
	card_content = "HelloWorld - Content"

	response = {"outputSpeech": {"type":output_type,"text":output_speech},"card":{"type":card_type,"title":card_title,"content":card_content},'shouldEndSession':False}

	return response

def intent_request(session, user, request):
	print "intent_request"
	if request['intent']['name'] == "HelloWorldIntent":
		output_speech = "Hellow World!"
		output_type = "PlainText"

		card_type = "Simple"
		card_title = "HelloWorld - Title"
		card_content = "HelloWorld - Content"

		response = {"outputSpeech": {"type":output_type,"text":output_speech},"card":{"type":card_type,"title":card_title,"content":card_content},'shouldEndSession':True}

		return response
	'''
	elif request['intent']['name'] ==  "NestSetIntent":
		nestTempValue = request['intent']['slots']['temp']['value']
		output_speech = "Telling Nest to cool to " + str(nestTempValue) + " degrees fahrenheit"
		output_type = "PlainText"

		card_type = "Simple"
		card_title = "HelloWorld - Setting Nest Temp"
		card_content = "Telling Nest to cool to " + str(nestTempValue) + " degrees fahrenheit."

		response = {"outputSpeech": {"type":output_type,"text":output_speech},"card":{"type":card_type,"title":card_title,"content":card_content},'shouldEndSession':True}

		return response
	
		'''
	else:
		return launch_request(session, user, request) ##Just do the same thing as launch request





class Session:
	def __init__(self,sessionData):
		self.sessionId = sessionData['sessionId']


	def getSessionID(self):
		return self.sessionId

class User:
	def __init__(self,userId):
		self.userId = userId
		self.settings = {}

	def getUserId(self):
		return self.userId

class DataStore:
	def __init__(self):
		self.sessions = {}
		self.users = {}

	def getSession(self,session):
		if session['new'] is True or session['sessionId'] not in self.sessions:
			self.sessions[session['sessionId']] = Session(session)

		return self.sessions[session['sessionId']]

	def getUser(self,session):
		userId = session['user']['userId']
		if userId not in self.users:
			self.users[userId] = User(userId)

		return self.users[userId]

