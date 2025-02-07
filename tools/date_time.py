from datetime import datetime

async def get_time():
    """Returns the current time in a structured format."""
    return {
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": "UTC"  # You can modify this based on system timezone
    }