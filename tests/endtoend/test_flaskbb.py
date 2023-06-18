import pytest
from playwright.sync_api import Page

###################################################################
# CoRise TODO: add a new fixture `translations` that calls the
# `compile_translations` function from flaskbb.utils.translations

# ADD CODE HERE

@pytest.fixture
def app():
    """application with context."""
    app = create_app(Config)
    
    with app.app_context():
        db.create_all()
        create_default_groups()
        create_default_settings()
        compile_translations()

    return app

def test_create_new_account(live_server, page: Page):    
    url=url_for('forum.index', _external=True)

    page.goto(url)
    expect(page).to_have_title("FlaskBB - A lightweight forum software in Flask")
    

###################################################################