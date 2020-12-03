import json


def test_predict(test_app):
    # Given
    client = test_app.test_client()

    # When
    resp = client.post(
        "/predict",
        data=json.dumps(
            {
                "CHAS": {"0": 0},
                "RM": {"0": 6.575},
                "TAX": {"0": 296.0},
                "PTRATIO": {"0": 15.3},
                "B": {"0": 396.9},
                "LSTAT": {"0": 4.98},
            }
        ),
        content_type="application/json",
    )

    # Then
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert "prediction" in data
    assert isinstance(data["prediction"][0], float)


def test_predict_invalid_json(test_app):
    # Given
    client = test_app.test_client()

    # When
    resp = client.post("/predict", data=json.dumps({}), content_type="application/json")

    # Then
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Input payload validation failed" in data["message"]
