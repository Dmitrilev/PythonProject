import json
from flask import Flask, Response

app = Flask(__name__)

@app.route("/alkuluku/<luku>")
def luku_tarkistus(luku):
    try:
        luku = int(luku)
        alkuluku = True
        if luku == 1:
            alkuluku = False
        elif luku == 2:
            alkuluku = True
        else:
            for i in range(2, luku):
                if luku % i == 0:
                    alkuluku = False
                    break

        respons = { "Number": luku,}
        if alkuluku:
            respons["isPrime"] = True
        else:
            respons["isPrime"] = False

        jsonvast = json.dumps(respons)
        return Response(response=jsonvast, status=200, mimetype="application/json")


    except ValueError:
        virhevastaus = {
            "status": 400,
            "teksti": "Virhe. Anna kokonaisluku."
        }
        return Response(response=json.dumps(virhevastaus), status=400, mimetype="application/json")


if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)




