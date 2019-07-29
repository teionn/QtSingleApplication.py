# QtSingleApplication.py

QtSingleApplicationクラスは、アプリケーションの実行中のインスタンスを検出して通信するためのAPIを提供します。

このクラスを使用すると、同じユーザーに対して同じマシン上で複数のインスタンスを実行できないアプリケーションを作成できます。

QtSingleApplicationクラスを使用するには、アプリケーションを実行しているシステム上で一意のID文字列を指定する必要があります。一般的なIDは、アプリケーションとアプリケーションベンダーの名前、またはUUIDの文字列表現です。

アプリケーションは、起動フェーズの早い段階でQtSingleApplicationオブジェクトを作成し、メッセージを送信するか、isRunning（）を呼び出してこのアプリケーションのインスタンスが既に実行されているかどうかを確認します。

- 引用
  - https://doc.qt.io/archives/qtextended4.4/qtopiadesktop/qtsingleapplication.html#details

- 参考
  - https://stackoverflow.com/a/12712362
  - https://stackoverflow.com/a/25970104

##### 以下のパケージを試用できる状態にしてください。
- [**Qt.py**](https://github.com/mottosso/Qt.py)
  - https://github.com/mottosso/Qt.py

- [**pywin32**](https://github.com/mottosso/Qt.py)
  - https://github.com/mhammond/pywin32
