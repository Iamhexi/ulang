"""Module with integration tests of `evaluate()` function."""

from typing import Any

import pytest

from main import evaluate
from core.tokens.literal import Duration, Time

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

@pytest.mark.parametrize('code,output', [
    ('9:30 - 8:00', '1h30m'),
    ('10:00 - 9:00', '1h'),
    ('12:15 - 8:30', '3h45m'),
    ('12:00 - 12:00', '0m'),
])
def test_time_arthmetics(code: str, output: str):
    """Test if time arthmetics works properly."""
    evaluated = evaluate(code)
    assert evaluated == Duration(output)

@pytest.mark.parametrize('code', [
    '8:00 - 9:00',
    '00:00 - 23:59',
])
def test_time_arthmetics_emitting_warning(code: str):
    """Test if subtracting a later hour from an earlier hours emits a warning."""
    with pytest.raises(UserWarning):
        evaluate(code)
