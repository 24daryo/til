/* 

sqlファイルを実行する場合は
\i /Users/username/.. .. .. /test1.sql
のようにする。パスは調べておくと良い
*/

/*
    テーブルを作成する
*/
CREATE temp TABLE table1 (id integer, nameA text);
select * from table1;