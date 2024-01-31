from flask import Flask, request, session
import pandas

app = Flask(__name__)
app.config["DEBUG"] = True

app.route("/", methods=["GET", "POST"])
def adder_page():
    if request.method == "POST":
        rawpaste= request.form["rawpaste"]


        #All the calculations bit will go here


           return '''
           <!DOCTYPE html>
           <html>
           <head>
           <title>Generate PDF Report</title>
           <style>
             @import url(https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,900);

             body {
               font-family: 'Helvetica Neue', Helvetica;
             }

             header {
               position: absolute;
               top: 50%;
               left: 50%;
               transform: translate(-50%, -50%);
               color: black;
               text-align: center;
             }
             h1 {
               text-transform: uppercase;
               margin: 0;
               font-size: 3rem;
               white-space: nowrap;
             }
             p {
               margin: 0;
               font-size: 1.75rem;
               color: red;
             }

             a:link {
               color: yellow;
               background-color: transparent;
               text-decoration: none;
             }

             a:visited {
               color: yellow;
               background-color: transparent;
               text-decoration: none;
             }

             a:hover {
               color: white;
               background-color: transparent;
               text-decoration: none;
             }

             a:active {
               color: grey;
               background-color: transparent;
               text-decoration: none;
             }

           </style>
           </head>

           <header>
             <h1>Paste Table Data Below</h1>
             <br><br><br>
             <h1><input name="rawpaste"></h1>
              <p><input type="submit" value="Generate" size="20%" /></p>
           </header>

           <footer>
               <p style='color: e1e1e1; 
               font-size: 0.6rem; 
               color: white;
               text-align: center; 
               position: relative;
               bottom: 100%;
               '>
               </p>
           </footer>

           </html> 
        
    '''
