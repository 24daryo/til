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
  <summary>推移的関数従属()</summary>
  AがわかるとBがわかり、BがわかるとCがわかるときのAとCの関係。
  このときCはAに推移的関数従属しているという。
  例えば社員Aの住所Bがわかればそれにより郵便番号Cもわかる例が当てはまる。
</details>

<details>
  <summary>ACID特性(ACID property)</summary>
  Atomicity（原子性）、Consistency（一貫性）、Isolation（独立性）、Durability（永続性）を頭字語で表したもの。
  
  トランザクション処理において必要とされる4つの要素である。
  
</details>

<details>
  <summary>原子性(Atomicity)</summary>
</details>
<details>
  <summary>一貫性(Consistency)</summary>
</details>
<details>
  <summary>独立性(Isolation)</summary>
</details>
<details>
  <summary>永続性(Durability)</summary>
</details>

# 違い一覧

<details>
  <summary>DROPコマンドとTRUNCATEコマンドの違いは</summary>
  DROPはロールバックできるDMLであるが、TRUNCATEできないDDLである。ただしTRUNCATEは高速であるメリットあり。
</details>

<details>
  <summary>第一正規化</summary>
  1行の中に複数の繰り返し項目が存在するような表(例えばnameカラムが複数あったり、dateカラムが複数あったり)を重複なしにすること。
  追加可能性がある要素は横でなく縦につながる構造にする必要があり、これを修正することを指す。
  
  列内の重複(縦の重複)は許して良いので、とにかく重複列(横の重複)がなく全てが単一セルで表現できているテーブルにするイメージ。
</details>

<details>
  <summary>第二正規化</summary>
  主キーに部分従属している属性を分離すること。
  
  簡単にいうと「キーの結びついていない繰り返し要素が列にある」状態を、主キーで分離して正規化して修正することを指す。
  イメージとしては、列内の繰り返しはキーのみになっている状態にすること。
</details>

<details>
  <summary>第三正規化</summary>
  テーブル内にある推移従属関係を分離して、どのテーブルであってもすべての属性が主キーに対して完全従属であるテーブルにすること。
  
  イメージとしては、テーブル内の列の冗長性が完全に排除され、関数従属以外の要素はキーのみで管理されている状態にすること。
  
</details>
  

