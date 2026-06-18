from pathlib import Path

from config import LOG_DIR


def log_basic_values(values: dict[str, float], file_name: str = "log_file.txt") -> None:
    """基本統計量をログファイルに書き込む関数。

    Parameters
    ----------
    file_name : str, optional
        ログファイルの名前。デフォルトは "log_file.txt"。
    values : dict[str, float]
        ログに書き込む基本統計量の辞書。

    Returns
    -------
    None

    """
    log_file_path = LOG_DIR / file_name
    with Path.open(log_file_path, "a") as log_file:
        log_file.write("基本統計量:\n")
        for key, value in values.items():
            log_file.write(f"{key}: {value}\n")
            log_file.write("\n")
