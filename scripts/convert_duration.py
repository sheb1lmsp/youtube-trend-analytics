import re

def duration_to_seconds(duration):
    """
    Convert ISO-8601 YouTube duration strings into total seconds.

    Examples:
        PT5M20S → 320 seconds
        PT1H2M5S → 3725 seconds
        PT30S → 30 seconds

    Parameters:
        duration (str): ISO-8601 duration string

    Returns:
        int: Duration in seconds
    """
    match = re.match(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', duration)
    if not match:
        return 0

    hours = int(match.group(1)) if match.group(1) else 0
    minutes = int(match.group(2)) if match.group(2) else 0
    seconds = int(match.group(3)) if match.group(3) else 0

    return hours * 3600 + minutes * 60 + seconds
