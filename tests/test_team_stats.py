import unittest
import pandas as pd
from src.team_stats import TeamStats

class TestTeamStats(unittest.TestCase):
    def setUp(self):
        data = {
            'match_id': [1, 2, 3],
            'result': ['win', 'loss', 'win'],
            'team_members': [['Player1', 'Player2'], ['Player1', 'Player3'], ['Player2', 'Player3']],
            'hero_picks': [['HeroA', 'HeroB'], ['HeroB', 'HeroC'], ['HeroA', 'HeroC']]
        }
        self.team_data = pd.DataFrame(data)
        self.team_stats = TeamStats(self.team_data)

    def test_get_team_results(self):
        results = self.team_stats.get_team_results()
        expected_results = {'wins': 2, 'losses': 1}
        self.assertEqual(results, expected_results)

    def test_get_team_composition(self):
        composition = self.team_stats.get_team_composition()
        expected_composition = ['Player2', 'Player3']
        self.assertEqual(composition, expected_composition)

    def test_get_hero_picks(self):
        hero_picks = self.team_stats.get_hero_picks()
        expected_hero_picks = {'HeroA': 2, 'HeroB': 2, 'HeroC': 2}
        self.assertEqual(hero_picks, expected_hero_picks)

if __name__ == '__main__':
    unittest.main()