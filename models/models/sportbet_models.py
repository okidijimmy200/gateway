from typing import Any

class SportBet:
    id: int
    league: str
    home_team: str
    away_team: str
    home_team_win_odds: float
    away_team_win_odds: float
    draw_odds: float
    game_date: str

    def __init__(self, id: int, league:str, home_team: str, away_team: str, home_team_win_odds: float, away_team_win_odds: float, draw_odds: float, game_date: str) -> None:
        self.id = id
        self.league = league
        self.home_team = home_team
        self.away_team = away_team
        self.home_team_win_odds= home_team_win_odds
        self.away_team_win_odds = away_team_win_odds
        self.draw_odds = draw_odds
        self.game_date = game_date

class CreateBetRequest:
    league: str
    home_team : str
    away_team: str
    home_team_win_odds : float
    away_team_win_odds: float
    draw_odds: float
    game_date:str

    def __init__(self, league: str, home_team: str, away_team: str, home_team_win_odds: float, away_team_win_odds: float, draw_odds: float, game_date: str) -> None:
        self.league = league
        self.home_team = home_team
        self.away_team = away_team
        self.home_team_win_odds= home_team_win_odds
        self.away_team_win_odds = away_team_win_odds
        self.draw_odds = draw_odds
        self.game_date = game_date

class CreateBetResponse:
    code: int
    reason : str

    def __init__(self, code: int, reason: str) -> None:
        self.code = code
        self.reason = reason

class ReadBetRequest:
    league: str
    start_date: str
    end_date: str

    def __init__(self, league: str, start_date: str, end_date: str) -> None:
        self.league = league
        self.start_date= start_date
        self.end_date = end_date

class ReadBetResponse:
    code: int
    response: Any
    reason: str

    def __init__(self, code: str, response: Any, reason: str) -> None:
        self.code =code
        self.response = response
        self.reason = reason

class UpdateBetRequest:
    id: int
    league: str
    home_team : str
    away_team: str
    home_team_win_odds : float
    away_team_win_odds: float
    draw_odds: float
    game_date: str

    def __init__(self, id: int, league: str, home_team: str, away_team: str, home_team_win_odds: float, away_team_win_odds: float, draw_odds: float, game_date: str) -> None:
        self.id = id
        self.league = league
        self.home_team = home_team
        self.away_team = away_team
        self.home_team_win_odds= home_team_win_odds
        self.away_team_win_odds = away_team_win_odds
        self.draw_odds = draw_odds
        self.game_date = game_date

class UpdateBetResponse:
    code: int
    reason : str

    def __init__(self, code: int, reason: str) -> None:
        self.code = code
        self.reason = reason

class DeleteBetRequest:
    league: str
    home_team: str
    away_team: str
    game_date: str

    def __init__(self, league: str, home_team: str, away_team: str, game_date: str) -> None:
        self.league = league
        self.home_team = home_team
        self.away_team = away_team
        self.game_date = game_date

class DeleteBetResponse:
    code: int
    reason: str

    def __init__(self, code: int, reason: str) -> None:
        self.code = code
        self.reason = reason