from counter import word_count


def test_word_count_empty_string():
    assert word_count("") == 0


def test_word_count_single_word():
    assert word_count("hello") == 1


def test_word_count_multiple_words():
    assert word_count("hello world foo bar") == 4
