from src.chomp import Chomp


def play_game() -> None:
    """Chompゲームをプレイする関数。"""
    row: int = int(input("行数を入力してください: "))
    col: int = int(input("列数を入力してください: "))
    game = Chomp(row, col)
    is_first_player: int = 1

    while game.is_game_over() is False:
        if is_first_player:
            print("第一プレイヤーの番です。")
        else:
            print("第二プレイヤーの番です。")
        game.display()
        r: int = int(input("食べる行のインデックスを入力してください: "))
        c: int = int(input("食べる列のインデックスを入力してください: "))
        game.eat(r, c)
        is_first_player ^= 1

    if is_first_player:
        print("第二プレイヤーの勝ちです!")
    else:
        print("第一プレイヤーの勝ちです!")


if __name__ == "__main__":
    play_game()
