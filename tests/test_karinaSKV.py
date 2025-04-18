import pytest
from .settings_KarinaSKV import autorizathion, get_method


def test_autorizathion():
    autorizathion()

def test_assert_status_code_get():
    get_method()