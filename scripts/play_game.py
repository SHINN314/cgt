from src.chomp import Chomp


def play_game() -> None:
    """Chompゲームをプレイする関数。"""
    row: int = int(input("行数を入力してください: "))
    col: int = int(input("列数を入力してください: "))
    game = Chomp(row, col)

    while game.is_game_over() is False:
        game.display()
        r: int = int(input("食べる行のインデックスを入力してください: "))
        c: int = int(input("食べる列のインデックスを入力してください: "))
        game.eat(r, c)
