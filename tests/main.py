from pytest import  fixture
from game.spriteloader import MySprite

class SimpleTest:

    @fixture
    def generate_sprite_fake(self) -> int:
        return 1
    
    def test_pytest(self, generate_sprite_fake: int):
        assert generate_sprite_fake == 1
