import main

def test_main():
    assert main.index() == 'Hello, world!'
    assert main.cow() == 'MOoooOo!'
    assert main.chicken() == 'Pok! Pok! Pok!'
    assert main.pig() == 'Oink! Oink!'
    assert main.sheep() == 'Baaaaah!'