@app.route("/predict-digit",methods=["POST"])
def predict_data():
    image = request.files.get("alphabet")
    prediction = get_prediction(image)

    return jsonify({

        'prediction':prediction
    }),200

    