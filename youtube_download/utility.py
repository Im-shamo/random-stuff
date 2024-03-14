def seconds_to_min(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes}:{remaining_seconds:02d}"


def check_num_range(n, start, end):
    return True if start <= n and end >= n else False
