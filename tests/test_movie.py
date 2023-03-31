import pytest
from viewing_party.movie import Movie

def test_create_movie():
    # Arrange
    elf = Movie("Elf", "Christmas Movie", 4)
    # Act

    # Assert
    assert isinstance(elf, Movie)
    assert elf.title == "Elf"
    assert elf.genre == "Christmas Movie"
    assert elf.rating == 4