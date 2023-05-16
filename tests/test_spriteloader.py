from pytest import fixture


# Classes not prefixed with Test won't be ran
class TestCase:
    @fixture
    def generate_sprite_fake(self) -> int:
        return 1

    def test_pytest(self, generate_sprite_fake: int):
        assert generate_sprite_fake == 1
