# テストコレクション作成実践

## 環境構築


### Anaconda
Anacondaは，コンパイル済Pythonパッケージの管理用ソフトウェアです． Anacondaを通して，様々なPythonパッケージ（ライブラリのようなもの）をWindowsでもMacでも簡単にインストールすることができます．
Python 3.xとPython 2.xがありますが，Python 3.x推奨です．
- Windows
	- https://docs.anaconda.com/anaconda/install/windows
- Mac
	- https://docs.anaconda.com/anaconda/install/mac-os
	

### Java

1. https://java.com/ja/ へアクセスし「無料Javaのダウンロード」→「同意して無料ダウンロードを開始」をクリック
2. ダウンロードしたファイルを実行し「インストール」
3. ターミナルを起動し「java -version」と入力，「java version “1.8.0_211” …」などと表示されれば成功

### Elasticsearch

1. https://www.elastic.co/jp/downloads/elasticsearch から 自分のOS用のElasticsearchをダウンロード
2. ダウンロードしたzipファイル (for Windows)／tar.gzファイル (for Mac)を展開し好きな場所に移動させる3. ターミナルを開き，「cd」を駆使して2で展開したフォルダ中のbinフォルダに移動
4. 「elasticsearch.bat」 (for Windows)／「elasticsearch」 (for Mac) を実行

### Elasticsearchの設定

1. Elasticsearchフォルダ中の「config/elasticsearch.yml」ファイルの末尾に下記の4行を追加
```
http.max_content_length: 350mb
cluster.routing.allocation.disk.threshold_enabled: false
http.cors.allow-origin: '*'
http.cors.enabled: true
```

2. ターミナル上でElasticsearchフォルダ中のbinフォルダに移動し
```bash
$ elasticsearch-plugin install analysis-kuromoji
```
を実行（日本語形態素解析器プラグイン）
	- Windowsの場合，elasticsearch-plugin.bat

3. 上記実施後にElasticsearchを再起動しておく
	- Ctrl+C (for Windows)／Command+C (for Mac)で一度止めて再実行

### Dockerを利用する場合

- Windows
	- 要件
		- Windows 10 64bit: Pro, Enterprise or Education， 4GB以上のメモリ，
		- 仮想化の有効化: https://docs.docker.com/docker-for-windows/troubleshoot/#virtualization-must-be-enabled 
	- ダウンロード
		- https://hub.docker.com/editions/community/docker-ce-desktop-windows
- Mac 
	- 要件
		- 2010年以降のMac，macOS Sierra 10.12以降のmacOS，4GB以上のメモリ，VirtualBox 4.3.30以前がインストールされていないこと
	- ダウンロード
		- https://hub.docker.com/editions/community/docker-ce-desktop-mac
		
インストール後に本レポジトリのディレクトリから以下のコマンドを実行
```bash
$ cd elasticsearch_docker
$ docker-compose up
```

## 青空文庫データ

- 青空文庫データ
	- https://bit.ly/2xAOAtJ (`aozorabunko_json_data.zip`)

上記データを展開し，`aozorabunko_json_data`を本レポジトリのディレクトリ中に移動させる．
ディレクトリは下記のようになる：
```
test_collection_lecture
- aozorabunko_json_data
- insert_aozorabunko.py
- mapping.json
- ranking.json
- test_collection_lecture.ipynb
- update_ranking.py
- ...
```

下記のコマンドによってElasticsearchに青空文庫のデータを投入できる：
```bash
$ python insert_aozorabunko.py
```

## 検索インタフェース

簡易的な検索インタフェースとして`webui/index.html`が利用可能．

## 評価
`Rankings.csv`と`Pooling.csv`を用意した上で，`test_collection_lecture.ipynb`を利用すればよい．
Precision@5とnDCG@5を計算することができる．