from codewatch.core import diff

def test_diff():
    assert diff("a\nb", "a\nc\nd") == {"before": 2, "after": 3, "changed": 2}
