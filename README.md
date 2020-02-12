環境構築メモ

1.python3系をインストールする
2.リポジトリをクローンする
3.クローンしたディレクトリに仮想環境を作成する
 python -m venv 仮想環境名
4.パッケージをインストールする
 pip install -r requirements.txt
5.データベースの準備
 python manage.py migrate
 python manage.py createsuperuser

　※データベースはsqliteかpostgresを使う

以上