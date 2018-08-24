import json
class GameStats():
    """跟踪游戏统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        filename='high_score.json'
        with open(filename)as f_obj:
            self.high_score = json.load(f_obj)

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
