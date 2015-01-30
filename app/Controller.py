import os
import webapp2
from google.appengine.ext.webapp import template     
from datetime import date
    
def renderTemplate(response, templatename, templatevalues) :
    basepath = os.path.split(os.path.dirname(__file__)) #extract the base path, since we are in the "app" folder instead of the root folder
    path = os.path.join(basepath[0], 'templates/' + templatename)
    html = template.render(path, templatevalues)
    response.out.write(html)
 
# Handler classes
class HomepageHandler(webapp2.RequestHandler) :
    def get(self):
        template_values = {
            'page_title' : "Swahili Cheat Sheet",
            'current_year' : date.today().year,
        }
            
        renderTemplate(self.response, 'home.html', template_values)
        
            
# list of URI/Handler routing tuples
# the URI is a regular expression beginning with root '/' char
routeHandlers = [
    (r'/', HomepageHandler),
]

# application object
application = webapp2.WSGIApplication(routeHandlers, debug=True)