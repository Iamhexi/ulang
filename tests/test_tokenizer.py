from core.tokenizer import SimpleTokenizer, Tokenizer
import pytest

@pytest.fixture
def simple_tokenizer() -> Tokenizer:
    return SimpleTokenizer()

@pytest.mark.parametrize('code,tokenized_code', [
    ('+123', ),
    ('-0', '[integer]'),
    ('+400', '[integer]'),
    ('95378', '[integer]'),
    ('2', '[integer]'),
    ('-18', '[integer]'),
])
def test_parsing_integers(code: str, tokenized_code: type, simple_tokenizer):
    assert  simple_tokenizer.tokenize(code)[0] == tokenized_code


@pytest.mark.parametrize('code,tokenized_code', [
    ('"abc"', '[string]'),
    ('"ABC"', '[string]'),
    ('"I\'m happy mom."', '[string]'),
    ('"9 nine 9"', '[string]'),
    ('"`ulang` is the best language known to the human race."', '[string]'),
    ('"-18"', '[string]'),
])
def test_parsing_strings(code: str, tokenized_code: str, simple_tokenizer):
    assert  simple_tokenizer.tokenize(code) == tokenized_code

@pytest.mark.parametrize('code,tokenized_code', [
    ('-1.23 1.', '[float] [integer]'),
    ('"-1.23 1."', '[string]'),
])
def test_parsing_mixed_literals(code: str, tokenized_code: str, simple_tokenizer):
    assert  simple_tokenizer.tokenize(code) == tokenized_code
