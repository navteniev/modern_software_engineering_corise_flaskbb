# CoRise TODO: add unit tests for topic manager

import pytest

from flaskbb.forum.topic_manager import TopicManager
from flaskbb.forum.models import Topic


def test_set_lock_state():
    manager = TopicManager('forum_id', 'user', ['topic'])
    manager._TopicManager__set_field_state = Mock()
    
    manager.set_lock_state(True)
    
    manager._TopicManager__set_field_state.assert_called_once_with('locked', True)

def test_set_important_state():
    manager = TopicManager('forum_id', 'user', ['topic'])
    manager._TopicManager__set_field_state = Mock()

    manager.set_important_state(True)

    manager._TopicManager__set_field_state.assert_called_once_with('important', True)

def test_delete_topics():
    topic_mock = Mock()
    manager = TopicManager('forum_id', 'user', [topic_mock])

    assert manager.delete_topics() == 1

    topic_mock.delete.assert_called_once()

def test___set_field_state():
    topic_mock = Mock()
    topic_mock.important = False
    manager = TopicManager('forum_id', 'user', [topic_mock])

    assert manager._TopicManager__set_field_state('important', True) == 1

    assert topic_mock.important == True
    topic_mock.save.assert_called_once()
