"""Module with integration tests of `evaluate()` function."""

from core.tokens.literal import Time
from main import evaluate
from typing import Any
import pytest

@pytest.mark.parametrize('code,output', [
    ('10', 10.0),
    ('-15.5', -15.5),
    ('"μLang is my favourite language."', 'μLang is my favourite language.'),
    ('10:15', Time('10:15')),
])
def test_evaluating_primitives(code: str, output: Any):
    """Test if primitives such as numbers, times, durations and strings as expected."""
    evaluated: Any = evaluate(code)
    assert type(evaluated) is type(output), \
        f"Mismatch between an actual type ({type(evaluated)}) and" \
        f" expected type ({type(output)})."
    assert evaluated == output
