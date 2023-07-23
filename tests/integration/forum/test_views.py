
from flask import url_for
from flask_login import login_user
from flaskbb.forum.models import Topic

# CoRise TODO: implement a integration test to validate the functionality of post method
"""
Hint: All actions require an logged in user autorized to manage topics the super_moderator_user
matches that criteria. Additionally, you will need access to a forum and topic both exist as a fixture.

Additionally, you will need a topic and a forum both are available as fixtures. Finally, you will need to
turn of cross site scripting checks since you are not using a real browser.

Your can use this template for each integration test you write.

def test_<action>(application, forum, topic, super_moderator_user):
    application.config['WTF_CSRF_ENABLED'] = False

    with application.test_client() as test_client:
        manage_forum_url = url_for("forum.manage_forum", forum_id=forum.id)

        login_response = test_client.post(url_for('auth.login'), data={'login': super_moderator_user.username,
                                        'password': 'test'},
                        follow_redirects=True)

        response = test_client.post(manage_forum_url, data = {
            "rowid": topic.id,
            ...
        }, follow_redirects=True)

        assert response.status_code == 200

    fresh_topic = Topic.query.filter_by(id=topic.id).first()
    # validate topic state change here.

"""