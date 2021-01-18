import music
from SoundEffects import SoundEffects


class EscapeRoomSoundEffects(SoundEffects):
    """
    Child class to represent an escape room collection of sound effects inheriting
    from the SoundEffects base class
    """

    def __init__(self, volume=None):
        """
        Attrs:
            volume: int
        """
        super().__init__(volume)

    @staticmethod
    def play_success_sound_effect():
        """
        Play a success sound effect as a result of a winning question

        Returns:
            str, str
        """
        return 'c4:4', 'c5:8'

    @staticmethod
    def win_game_sound_effect():
        """
        Play a win game sound effect as a result of a escaping the room

        Returns:
            str
        """
        return music.POWER_UP