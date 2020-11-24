

def test_development_config(test_app):
    test_app.config.from_object("project.config.DevelopmentConfig")
    assert test_app.config["SECRET_KEY"] == "SECRET"
    assert not test_app.config["TESTING"]


def test_testing_config(test_app):
    test_app.config.from_object("project.config.TestingConfig")
    assert test_app.config["SECRET_KEY"] == "SECRET"
    assert test_app.config["TESTING"]


def test_production_config(test_app):
    test_app.config.from_object("project.config.ProductionConfig")
    assert test_app.config["SECRET_KEY"] == "SECRET"
    assert not test_app.config["TESTING"]
