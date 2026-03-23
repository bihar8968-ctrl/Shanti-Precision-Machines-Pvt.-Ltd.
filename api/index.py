from flask import Flask, render_template, request, jsonify
import os

# Using explicit template folder path for serverless environments
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

PRODUCTS = {
    "VFD": ["Siemens", "ABB", "Schneider Electric", "Danfoss", "Yaskawa", "Delta", "Fuji Electric", "Mitsubishi"],
    "Relays": ["Omron", "Siemens", "Schneider Electric", "ABB", "TE Connectivity", "Panasonic", "Fuji Electric", "Eaton"],
    "MCB": ["Schneider Electric", "Legrand", "Havells", "ABB", "Anchor Panasonic", "L&T", "Finolex", "BCH Electric"],
    "Relay & Contactors": ["Hella", "Bosch", "Phoenix Molex", "Comat Releco", "Progressive Automotives", "Autonics", "Enalshi"],
    "Connectors": ["TE Connectivity", "Amphenol", "Molex", "Hirose Electric", "JST", "Harting"],
    "Terminals": ["APN", "Kundu", "Hicargo", "Wago/Phoenix"],
    "Wires": ["Polycab", "Finolex", "Havells", "RR Kabel", "V-Guard", "KEI", "Syska Anchor"],
    "Motors": ["ABB", "Siemens", "Crompton Greaves", "Kirloskar", "Hindustan Motors", "Marathon"],
    "SSPS Fuse": ["Eaton", "Littelfuse", "Siemens", "SIBA", "Mersen", "DF Electric", "Lawson", "Keystone"],
    "Proximity Sensors": ["Autonics", "Omron", "SICK", "BCH", "Pepperl+Fuchs"],
    "Reed Switch": ["Gem", "Havells", "Anchor", "Honeywell", "Schneider", "HPL"],
    "Limit Switch": ["Siemens", "Schneider", "Honeywell", "Omron", "Schmersal"],
    "Pneumatic Cylinders": ["SMC", "Festo", "Janatics", "IMI Norgren", "Parker", "Camozzi"],
    "Pneumatic Valves": ["Airtac", "SMC", "Festo", "Koganei", "Janatics", "Pneumax"],
    "CNC Controllers": ["FANUC", "Siemens", "Mitsubishi"],
    "NC Systems": ["FANUC", "Siemens", "Mitsubishi", "Haas", "Delta", "NC Studio"],
    "PLC Controllers": ["Siemens", "Allen-Bradley", "Mitsubishi", "Schneider", "Omron"],
}

COMPANY = {
    "name": "Shanti Precision Machine Pvt. Ltd.",
    "phone": "+91 9825276581",
    "email": "saurabh.as134@gmail.com",
    "whatsapp": "919825276581",
    "address": "616, 07, GIDC Rd, Makarpura GIDC, Makarpura, Vadodara, Gujarat 390010",
    "map_embed_url": "https://www.google.com/maps?q=616,%2007,%20GIDC%20Rd,%20Makarpura%20GIDC,%20Makarpura,%20Vadodara,%20Gujarat%20390010&output=embed",
    "map_link": "https://maps.google.com/?q=616,%2007,%20GIDC%20Rd,%20Makarpura%20GIDC,%20Makarpura,%20Vadodara,%20Gujarat%20390010",
}

@app.route("/")
def index():
    return render_template("index.html", company=COMPANY, products=PRODUCTS)

@app.route("/get-products")
def get_products():
    return jsonify(PRODUCTS)

@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json()
    name = data.get("name", "")
    phone = data.get("phone", "")
    email = data.get("email", "")
    message = data.get("message", "")
    # In production, send email or store in DB
    print(f"Contact from {name} | {phone} | {email}: {message}")
    return jsonify({"success": True, "message": "Thank you! We'll get back to you shortly."})

if __name__ == "__main__":
    app.run(debug=True)
