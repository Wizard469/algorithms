from challenges.challenge_encrypt_message import encrypt_message
from pytest import raises


def test_encrypt_message():
    with raises(TypeError, match="tipo inválido para key"):
        encrypt_message("challenge", "7")
    with raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 2)

    assert encrypt_message("challenge", 3) == "ahc_egnell"
    assert encrypt_message("challenge", 5) == "llahc_egne"
    assert encrypt_message("challenge", 4) == "egnel_lahc"
    assert encrypt_message("challenge", 6) == "egn_ellahc"
    assert encrypt_message("challenge", 10) == "egnellahc"
    assert encrypt_message("challenge", 20) == "egnellahc"
