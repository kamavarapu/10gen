import bottle

@bottle.route('/')
def home_page():
	mythings = ['car', 'pin', 'needle']
	return bottle.template('home_page', {'username': "Manoj", 'things': mythings, 'title': "Home Page"})
	
@bottle.route('/secondpage')
def second_page():
	myotherthings = ['TV', 'Fridge', 'Receiver']
	return bottle.template('home_page', {'username': "Archana", 'things': myotherthings, 'title': "Second Page"})
	
bottle.debug(True)
bottle.run(host='localhost', port=8082)