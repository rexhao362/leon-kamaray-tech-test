import csv
from collections import Counter


def read_csv_file(file_path):
    """
    Read a CSV file and return its content as a list of dictionaries.

    Args:
        filepath (str): The filepath of the CSV data.

    Returns:
        list of dictionaries: A list of dictionaries containing data
        from the CSV mapped to their corresponding headers.
    """

    with open(file_path, newline='')as f:
        reader = csv.DictReader(f)

        return [row for row in reader]


def get_unique_teams(data):
    """
    Return a set of unique team names from the provided data.

    Args:
        data (list of dictionaries): Dataset that has been
        extracted from a CSV file.

    Returns:
        set: Returns a set of all unique team names in the
        dataset.
    """
    return set(row['team_name'] for row in data)


def get_most_common_event_type(data):
    """
    Return the most common event type name from the provided data.

    Args:
        data (list of dictionaries): Dataset that has been
        extracted from a CSV file.

    Returns:
        str: Returns the most common event type name
    """

    event_types = [row.get('event_type_name') for row in data]

    return Counter(event_types).most_common(1)[0][0]


def filter_by_team(data, team_name):
    """
    Filter the data by the provided team name and return the filtered data.

    Args:
        data (list of dictionaries): Dataset that has been
        extracted from a CSV file.
        team_name (str): The name of the team for which the data should
        be filtered.

    Returns:
        list of dictionaries: Returns a dataset containing only the data
        that corresponds to the selected team.
    """
    return list(filter(lambda x: x['team_name'] == team_name, data))


def count_event_type_by_team(data, team_name, event_type_name):
    """
    Count the number of events of a specific type for a given team.
    """
    return


def average_pass_length_by_team(data, team_name):
    """
    Calculate the average pass length for the provided team to 1 decimal place
    """
    return


def filter_players_by_position(data, position_name):
    """
    Return a list of player names who play at the provided position.
    """
    return


def count_successful_passes(data):
    """
    Count the number of successful passes (not considering pass outcome).
    """
    return


def filter_by_period(data, period):
    """
    Return a list of events that occurred in the provided period (e.g., 1 or 2).
    """
    return


def count_shots_by_player(data, player_name):
    """
    Count the number of shots taken by the provided player.
    """
    return
