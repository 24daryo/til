# Top 65 SQL Interview Questions You Must Prepare In 2021

I have compiled the information on the following sites in my own way.

https://www.edureka.co/blog/interview-questions/sql-interview-questions?utm_source=youtube&utm_medium=description&utm_campaign=sql-int-video-09072019

# 用語一覧

概念理解のために、日本語ではじめは書いておく

<details>
  <summary>インデックス(Index)</summary>
  ある列(カラム)の要素について、ある規則性に沿って並び替えられたもの。
  
  インデックスがないと、線形探索となりo(n)となるが、整列されていることで計算量を削減し
  効果的なパフォーマンス向上が得られる。
  
  ただしデメリットとして、データ追加時にその都度インデックス作成するため、データ追加の処理が重たくなる。
  
  よって無闇にインデックスを使うのでなく、効果的に選択する必要がある。

</details>

<details>
  <summary>ヒープ表(Heap organized Table)</summary>
  インデックスのない通常のテーブルのこと。計算量はo(n)で遅い。
</details>

<details>
  <summary>クラスタ化インデックス(Clustered Index)</summary>
  B-Treeで構成されたインデックス。計算量はo(logn)。一般的にPrimaryKeyの値で作成される。
  
  ただし、テーブル1つに対して1つしかクラスタ化インデックスを作成できない。
</details>


<details>
  <summary>部分関数従属()</summary>
</details>

<details>
  <summary>関数従属()</summary>
  主キーが決まるとその他も一位的に決定できるもの。
  例えば「千代田区」とわかれば「東京都千代田区」なので東京都も一意的に決定できる。
  つまり、東京都は千代田区に関数従属していると言える。
</details>

<details>
  <summary>部分関数従属()</summary>
</details>

<details>
  <summary>部分関数従属()</summary>
</details>

# 違い一覧

<details>
  <summary>DROPコマンドとTRUNCATEコマンドの違いは</summary>
  DROPはロールバックできるDMLであるが、TRUNCATEできないDDLである。ただしTRUNCATEは高速であるメリットあり。
</details>

<details>
  <summary>第一正規化</summary>
  1行の中に複数の繰り返し項目が存在するような表(例えばnameカラムが複数あったり、dateカラムが複数あったり)。
  追加可能性がある要素は横でなく縦につながる構造にする必要がある(つまり正規化するべき)
</details>

<details>
  <summary>第二正規化</summary>
  
  簡単にいうと「キーの結びついていない繰り返しが列にある」状態。これも分離して正規化する必要あり。
</details>
  

