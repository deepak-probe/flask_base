from main import app

def test_home_route():
    """Make sure we get an expected response from home route"""
    response = app.test_client().get('/')
    assert response.status_code == 200
