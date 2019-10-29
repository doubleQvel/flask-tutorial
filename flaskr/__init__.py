import os
from flask import Flask


def create_app(test_config=None):
    """
    1.Flaskインスタンスの作成
    2.設定変数の決定
    3.読み込み時にtest設定であれば変数読み込み
    4.インスタンスフォルダの確認
    5.ページの作成
    6.作成したappを渡す
    """
    # create and configure the app
    # __name__ : pythonのモジュール名
    # instance_relating_config: 設定ファイルとインスタンスフォルダとの関係性
    # インスタンスフォルダはflaskrの外にあり、ローカルデータを保持できる
    # app.config.from_mapping
    # デフォルトのアプリで使う変数の設定
    # SECRET_KEY:隠し変数名ををdev内に格納していることを示す。ここで使うのは開発中の変数
    # DATABASE:データベースのパス。ここではsqliteを使う
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev", DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )
    if test_config is None:
        # load the instance config, if it exists, whem not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    # makedirs():flaskはインスタンスフォルダは自動的に生成されないので存在を確保する
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that sasy hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    from . import db

    db.init_app(app)

    from . import auth

    app.register_blueprint(auth.bp)

    return app
