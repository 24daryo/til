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
