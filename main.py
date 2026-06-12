from Flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def index():
    return "bhaad me ja bsdk"



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)



#https://fuzzy-waddle-6p67vjvv65xf59gv-40763.app.github.dev/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/#/ingressclass?namespace=default
