import pandas as pd
import random
from src.team_stats import TeamStats
from src.player_stats import PlayerStats
from src.hero_trends import HeroTrends
import matplotlib.pyplot as plt

heroes = ["Antimage", "Axe", "Bane", "Bloodseeker", "Crystal Maiden", "Drow Ranger", "Earthshaker", "Juggernaut", "Mirana", "Morphling"]

teams_data = {
    "Team Liquid": {"place": 1, "players": ["miCKe", "Nisha", "33", "Boxi", "Insania"]},
    "Gaimin Gladiators": {"place": 2, "players": ["dyrachyo", "Quinn", "Ace", "tOfu", "Seleri"]},
    "Team Spirit": {"place": 3, "players": ["Yatoro", "Larl", "Collapse", "Mira", "Miposhka"]},
    "Team Falcons": {"place": 4, "players": ["skiter", "Malr1ne", "ATF", "Cr1t-", "Sneyking"]},
    "BetBoom Team": {"place": 5, "players": ["Nightfall", "gpk", "MieRo`", "Save-", "TORONTOTOKYO"]}
}

def generate_match_data(team1, team2):
    data = []
    for match_id in range(1, 11):
        kills_team1 = random.randint(20, 60)
        kills_team2 = random.randint(20, 60)
        winner = team1 if kills_team1 > kills_team2 else team2

        match_data = {
            "match_id": match_id,
            "team1": team1,
            "team2": team2,
            "kills_team1": kills_team1,
            "kills_team2": kills_team2,
            "winner": winner,
            "hero_picks_team1": random.sample(heroes, 5),
            "hero_picks_team2": random.sample(heroes, 5)
        }
        data.append(match_data)
    return pd.DataFrame(data)

def generate_player_data():
    player_data = []
    for hero in random.sample(heroes, 5):
        player_data.append({
            "hero": hero,
            "kills": random.randint(5, 20),
            "deaths": random.randint(0, 10),
            "assists": random.randint(5, 15),
            "gpm": random.randint(300, 700),
            "xpm": random.randint(400, 800)
        })
    return pd.DataFrame(player_data)

def main():
    teams = {}
    for team_name, team_info in teams_data.items():
        team_data = {
            "match_id": list(range(1, 11)),
            "result": ["win" if i % 2 == 0 else "loss" for i in range(10)],
            "team_members": [team_info["players"]] * 10,
            "hero_picks": [random.sample(heroes, 5) for _ in range(10)]
        }
        team_df = pd.DataFrame(team_data)
        teams[team_name] = TeamStats(team_df, team_info["place"])

    for team_name, team_stats in teams.items():
        print(f"\n{team_name} Report:")
        print(team_stats.generate_report())
        team_stats.plot_results()
        team_stats.plot_hero_picks()

    players = []
    for player_name in teams_data["Team Spirit"]["players"]:
        player_df = generate_player_data()
        player_stats = PlayerStats(player_df)
        players.append(player_stats)
        
        print(f"\n{player_name}'s Report:")
        print(player_stats.generate_report())
        player_stats.plot_kda()
        player_stats.plot_hero_performance()

    match_data = []
    for team1_name, team2_name in [("Team Liquid", "Gaimin Gladiators"), ("Team Spirit", "Team Falcons")]:
        match_df = generate_match_data(team1_name, team2_name)
        
        heroes_team1 = pd.DataFrame({
            "match_id": match_df["match_id"],
            "hero": match_df["hero_picks_team1"].explode()
        })
        heroes_team2 = pd.DataFrame({
            "match_id": match_df["match_id"],
            "hero": match_df["hero_picks_team2"].explode()
        })
        
        match_data.append(heroes_team1)
        match_data.append(heroes_team2)

    hero_data = pd.concat(match_data, ignore_index=True)
    hero_trends = HeroTrends(hero_data)

    print("\nHero Trends Report:")
    print(hero_trends.generate_report())
    hero_trends.plot_hero_popularity()
    hero_trends.plot_hero_combinations()

if __name__ == "__main__":
    main()
