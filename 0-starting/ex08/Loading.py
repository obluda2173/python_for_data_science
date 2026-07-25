import os


MAGIC_NUMBER = 42


def ft_tqdm(lst: range) -> None:
    """Replica of tqdm progress bar"""
    total = len(lst)

    for i, item in enumerate(lst):
        percent = (i / total) * 100
        terminal_size = os.get_terminal_size()
        loading_space = terminal_size.columns - MAGIC_NUMBER
        arrow_length = int((i / total) * loading_space)
        arrow = "=" * arrow_length
        spaces = ">" + " " * (loading_space - 1 - arrow_length)

        print(f"\r{int(percent)}%|[{arrow}{spaces}]| {i}/{total}", end="",
              flush=True)

        yield item

    print(f"\r100%|[{'=' * (loading_space - 1)}>]| {total}/{total}")
