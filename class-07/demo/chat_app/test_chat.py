from chat import AudioMessage
import pytest

# def test_trim():
#     expected = "trim method will be added later"
#     audio_msg = AudioMessage(2)
#     actual = audio_msg.trim()
#     assert actual == expected

# def test_get_size():
#     expected = "size is big"
#     audio_msg = AudioMessage(3)
#     actual = audio_msg.get_size()
#     assert actual == expected
    
# python fixture
@pytest.fixture
def new_msg():
    audio_msg = AudioMessage(5)
    return audio_msg


def test_trim(new_msg):
    expected = "trim method will be added later"
    actual = new_msg.trim()
    assert  actual == expected

def test_get_size(new_msg):
    expected = "size is big"
    actual = new_msg.get_size()
    assert  actual == expected