def sort_games(*args, **kwargs):
    console_games = {}
    pc_games = {}

    platforms = {title: platform for platform, title in args}

    for release_id, title in kwargs.items():
        if platforms[title] == "console":
            console_games[release_id] = title
        else:
            pc_games[release_id] = title

    result = []

    if console_games:
        result.append("Console Games:")
        for release_id in sorted(console_games):
            date = "_".join(release_id.split("_")[:-1])
            result.append(f">>>{date}: {console_games[release_id]}")

    if pc_games:
        result.append("PC Games:")
        for release_id in sorted(pc_games, reverse=True):
            date = "_".join(release_id.split("_")[:-1])
            result.append(f"<<<{date}: {pc_games[release_id]}")

    return "\n".join(result)
