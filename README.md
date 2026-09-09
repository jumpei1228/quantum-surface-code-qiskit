# 表面符号(サーフェスコード)をQiskitで実装｜XとZを同時に見張る2次元誤り訂正

Googleの量子プロセッサ「Willow」で話題になった表面符号(サーフェスコード)の最小単位をQiskitで実装。X・Zどちらのエラーも検出できるしくみと、格子を大きくするほど論理エラー率が指数関数的に下がる理由をコードで確かめます。

> 📖 このコードの詳しい解説（理論・図解つき）は元記事をどうぞ:
> **[表面符号(サーフェスコード)をQiskitで実装｜XとZを同時に見張る2次元誤り訂正](https://quantum.yurufuwa.work/learn/surface-code-qiskit)** — ゆるふわ量子コンピュータ

## セットアップ

```bash
pip install -r requirements.txt
```

## 実行方法

```bash
python surface-code-qiskit.py
```

## これは何？

[ゆるふわ量子コンピュータ](https://quantum.yurufuwa.work) はやさしい技術解説サイト「ゆるふわ」シリーズの一つです。このリポジトリは記事内で解説しているコードをそのまま動かせる形にまとめた、記事の副教材（コンパニオンリポジトリ）です。

## License

MIT
