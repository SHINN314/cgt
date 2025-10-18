# 組み合わせゲーム理論 Chomp の確率的解析

## 環境構築

`uv`を用いてプロジェクトを管理している。
`uv`を pc にインストールしていない場合は[ドキュメント](https://docs.astral.sh/uv/getting-started/installation/)を参考にインストールしてから以下のコマンドを一考する。

```bash
uv sync
```

## コミットルール

コミット時の構文は以下の通り。

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

また、コミット時に許されている type と詳細は以下の通り。

| type     | 説明             |
| :------- | ---------------- |
| add      | 新規機能の追加   |
| update   | 実装の更新       |
| fix      | 実装の修正       |
| refactor | リファクタ       |
| chore    | その他のコミット |

## Linter と Formatter

Linter と Formatter は`Ruff`を用いて管理している。
vscode の拡張機能から`Python`と`Ruff`の拡張機能をインストールすることで使えるようにしている。
