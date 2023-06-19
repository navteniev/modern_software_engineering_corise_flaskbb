import pytest
from flaskbb.forum import forms
from werkzeug.datastructures import MultiDict


pytestmark = pytest.mark.usefixtures("post_request_context", "default_settings")

###################################################################
# CoRise TODO: add unit tests below that test the functionality of
# the `SpecialTopicForm`

class TestSpecialTopicForm(object):
    # ADD CODE HERE

    def test_add_title_speical_topic_prefix(self):        
        test_data = MultiDict({"title" : "Test Title",  "content" : "Test Content", "track_topic" : False})
        form = forms.SpecialTopicForm(formdata = test_data)
        assert form.data.get("title") == "Special Topic : Test Title"

    def test_add_content_speical_topic_prefix(self):        
        test_data = MultiDict({"title" : "Test Title",  "content" : "Test Content", "track_topic" : False})
        form = forms.SpecialTopicForm(formdata = test_data)
        assert form.data.get("content") == "Special Topic : Test Content"
    

###################################################################