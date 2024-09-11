from datetime import datetime

def get_formatted_date(date, format="%A, %d %b\n%Y"):
    if date is not None:
        # Ensure the date is parsed correctly
        if isinstance(date, str):
            # Parse the string with the given format (includes milliseconds and 'Z')
            date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
        
        # If you need to localize the time, ensure to add timezone handling here
        return date.strftime(format)

    return date