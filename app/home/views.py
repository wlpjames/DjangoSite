from django.shortcuts import render

# Create your views here.

#landing main page
def index(request):

	return render(request, "index.html", {'sliders': sliders})
	

#landing contact page
def contact(request):
	return render(request, "contact.html")

def about(request):
	return render(request, "about.html")

sliders = [

	{
	'id' : 0, 
	'heading' : 'Image One', 
	'desc' : 'A short description of the thing that it is',
	'image' : 'https://www.realgap.co.uk/tpl/lib/img/public/compressed-images/tpl/lib/img/private/media/africa-900x621-cropped-85.jpg',
	},

	{
	'id' : 1, 
	'heading' : 'Image Two', 
	'desc' : 'A short description of the thing that it is',
	'image' : 'https://images.pexels.com/photos/861339/pexels-photo-861339.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
	},
	
	{
	'id' : 2,
	'heading' : 'Image Three', 
	'desc' : 'A short description of the thing that it is',
	'image' : 'https://www.nationalgeographic.com/content/dam/travel/2019-digital/south-africa-hub/royal-natal-national-park-drakensberg-south-africa.adapt.1900.1.jpg',
	},

]