from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body>Hello!</body></html>"
            self.wfile.write(message)
            print message
            return
	
	if self.path.endswith("/hola"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body> &#161 Hola ! </body></html>"
            self.wfile.write(message)
            print message
            return

        else:
            self.send_error(404, 'File Not Found: %s' % self.path)
    def do_post(self):
	 try:
	   self.send_response(301)
	   self.send_header('Content-type', 'text/html')
           self.end_headers()
           ctype, pdict =cgi.parse_header(
                  self.headers.getheader('content-type'))
           if ctype=='multipart/form-data':
	       fields= cgi.parse_multipart(self.rfile, pdict)
               messagecontent=fields.get('message')
           output=""
           output++"<html><body>"
           output+= "h<h2> okey, how about this: </h2>"
           output+="<h2> %s </h1>" % messagecontent[0]
           output+= '''<form method='POST' enctype='multipart/form-data' action='/hello'> what would you like to say? </h2><input name="message" type="text"> <input type="submit" value="Submit"> </form>'''
           output+="</body></html>"
           self.wfile.write(output)
           print(output)

         except:
            pass 


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()
