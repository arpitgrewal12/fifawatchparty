# Services keep it separate from routes because routes should only handle HTTP in/out. The actual work of fetching and processing football data belongs in a service.
import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()


def get_matches():

    api_key = os.getenv('FOOTBALL_API_KEY')
    uri = 'https://api.football-data.org/v4/competitions/WC/matches'
    headers = {'X-Auth-Token': api_key}

    try:
        response = requests.get(uri, headers=headers)
        # print(response.status_code)
        # print(response.json())
        matches = response.json()['matches']
        matches_list = []

        for match in matches:
            matches_list.append({
                'id': match['id'],
                'home_team': match['homeTeam']['name'],
                'away_team': match['awayTeam']['name'],
                'home_score': match['score']['fullTime']['home'],
                'away_score': match['score']['fullTime']['away'],
                'status': match['status'],
                'date': match['utcDate'],
                'stage': match['stage']
            })

        return matches_list

    except Exception as e:
        print(f'Error fetching matches: {e}')
        return []
