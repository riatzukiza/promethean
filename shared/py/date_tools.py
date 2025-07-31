from datetime import datetime, timezone, timedelta


def time_ago(past: datetime, now: datetime = None) -> str:
    if now is None:
        now = datetime.now(timezone.utc)
    delta = now - past

    seconds = int(delta.total_seconds())
    minutes = seconds // 60
    hours = minutes // 60
    days = delta.days

    if seconds < 60:
        return f"{seconds} second{'s' if seconds != 1 else ''} ago"
    elif minutes < 60:
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    elif hours < 24:
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    else:
        return f"{days} day{'s' if days != 1 else ''} ago"


def days_until(future: datetime, now: datetime | None = None) -> int:
    """Return number of whole days from *now* until ``future``.

    A negative value is returned if ``future`` is in the past relative to ``now``.
    """
    if now is None:
        now = datetime.now(timezone.utc)
    delta = future - now
    return delta.days
