■環境構築メモ

1.python3系をインストールする
2.リポジトリをクローンする
3.クローンしたディレクトリに仮想環境を作成する
  > python -m venv 仮想環境名
4.パッケージをインストールする
  > pip install -r requirements.txt
5.データベースの準備
 1.postgresをインストールする
 2.ユーザ&データベースを作成する
  > psql -U postgres
  # CREATE USER kakeibo WITH password 'パスワード';
  # CREATE DATABASE kakeibo OWNER kakeibo;
 3.作成したデータベースにマイグレーションの適用
  > python manage.py migrate
 4.アプリケーション操作用のユーザ追加
  > python manage.py createsuperuser

6.ローカルで起動する
  > python manage.py runserver


■うまくいかないとき
pip install -r requirements.txt時にエラーが出た場合、
requirements.txt内でセットしているバージョンが最新かどうかを確認する

updateが必要なパッケージのリスト表示
$ pip list -o


■dbバックアップ→リストア（Djangoのやり方）
python manage.py dumpdata > filename.json
python manage.py loaddata filename.json
