import pytest

from project import app


@pytest.fixture(scope="module")
def test_app():
    app.config.from_object("project.config.TestingConfig")
    with app.app_context():
        yield app
