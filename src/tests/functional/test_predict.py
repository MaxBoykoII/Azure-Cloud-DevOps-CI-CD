import json


def test_predict(test_app):
    # Given
    client = test_app.test_client()

    # When
    resp = client.post(
        "/predict",
        data=json.dumps(
            {
                "CHAS": {"0": 0, "1": 0},
                "RM": {"0": 6.575, "1": 5.5},
                "TAX": {"0": 296.0, "1": 295.0},
                "PTRATIO": {"0": 15.3, "1": 243.0},
                "B": {"0": 396.9, "1": 343.2},
                "LSTAT": {"0": 4.98, "1": 5.1},
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


def test_predict_invalid_json_keys(test_app):
    # Given
    client = test_app.test_client()

    # When
    resp = client.post(
        "/predict", data=json.dumps({"CHAS": {"0": 0}}), content_type="application/json"
    )

    # Then
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Input payload validation failed" in data["message"]
