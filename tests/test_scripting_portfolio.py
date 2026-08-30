from src.scripting_portfolio import sort_tv_shows, word_frequencies


def test_sort_tv_shows_orders_by_count_then_title():
    assert sort_tv_shows(["20 Gunsmoke", "10 Dallas", "20 Law & Order"]) == [
        (10, "Dallas"), (20, "Gunsmoke"), (20, "Law & Order")
    ]


def test_word_frequencies_are_case_insensitive():
    assert word_frequencies(["Hello", "hello", "cat", "cat"]) == {"cat": 2, "hello": 2}
