position_example = ("P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DH")
statuses_example = ("yes", "no, injured", "no, retired")
 
 
def validate_name(name: str):
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    name = name.strip()
    if not name:
        raise ValueError("name cannot be empty")
    if len(name) < 2:
        raise ValueError("name must be at least 2 characters long")
    if len(name) > 50:
        raise ValueError("name must not exceed 50 characters")
    return name
 
 
def validate_age(age: int):
    if not isinstance(age, int):
        raise TypeError("age must be an integer")
    if age < 16:
        raise ValueError("age must be at least 16")
    if age > 50:
        raise ValueError("age must not exceed 50")
    return age
 
 
def validate_team(team: str):
    if not isinstance(team, str):
        raise TypeError("team must be a string")
    team = team.strip()
    if not team:
        raise ValueError("team name cannot be empty")
    return team
 
 
def validate_batting_average(avg: float):
    if not isinstance(avg, (int, float)):
        raise TypeError("batting average must be a number")
    avg = float(avg)
    if avg < 0.0 or avg > 1.0:
        raise ValueError("batting average must be between 0.0 and 1.0")
    return avg
 
 
def validate_home_runs(hr: int):
    if not isinstance(hr, int):
        raise TypeError("home runs must be an integer")
    if hr < 0:
        raise ValueError("home runs cannot be negative")
    return hr
 
 
def validate_position(position: str):
    if not isinstance(position, str):
        raise TypeError("position must be a string")
    position = position.strip().upper()
    if position not in position_example:
        raise ValueError(
            f"position '{position}' is invalid. try {", ".join(position_example)}"
        )
    return position
 
 
def validate_status(status: str):
    if status not in statuses_example:
        raise ValueError(
            f"status '{status}' is invalid. try {", ".join(statuses_example)}"
        )
    return status