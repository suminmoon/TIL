## <9장> DML, TCL, 읽기 일관성 및 Lock


### DML : INSERT, UPDATE, DELETE

    drop table t1 purge;
    
    create table t1
    as
    select empno a, ename b, sal c
    from emp
    where 1 = 2;

    select * from t1;
    
    insert into t1 values(1000, 'korea', 27.343);
    insert into t1 values(1001, 'usa');   -- table 컬럼 세 개인데 두 개만 주면 에러 발생!
    insert into t1(a,b) values(1001, 'usa');  -- 성공 ( 암시적 null 입력 )
    insert into t1 values(1002, 'Uk', null);   -- 성공 ( 명시적 null )
    -- oracle insert는 한 번에 한 건씩만 할 수 있다.
    -- 단, db 내부에 있는 데이터를 넣을 때는 한 번에 여러 건 넣을 수 있음
    
    
    
    
    insert into t1 values (&sv_no, 'abc', 300);
    select * from t1;
    
    
#### 9-16. implicit query ( 암시적 쿼리 )

    where 절이 없으면 테이블 모든 값을 바꿈
    where절 주면 조건에 일치하는 행만 바꿈
    
#### 9-25. Delete vs Truncate vs Drop

                                rollback      공간반납
    delete table t1;             o               x         
                                             -- rollback 영역으로 옮겨짐 ( 되돌릴 수 있음)
    truncate table t1;           x         최초 크기만 남기고 반납
    drop table t1;               x           몽땅 반납
    

#### TCL : COMMIT, ROLLBACK, SAVAPOINT

    drop table t1 purge;
    
    create table t1 (no number, name varchar2(10));
    
    insert into t1 (no) values (1000);
    insert into t1 (no) values (2000);
    
    update t1 set name = 'JAVA' where no = 2000;
    
    savepoint s1;
    
    insert into t1 (no) values (3000);
    insert into t1 (no) values (4000);

    savepoint s2;
    
    insert into t1 (no) values (5000);
    insert into t1 (no) values (6000);

    rollback to s2; -- s2 이후 것 모두 취소
    
    commit;
    
    select * from t1;
    
    
#### 9-29. 읽기 일관성,  Lock 그리고 Deadlock

[SESSION 1]

    create table t_books
    ( no number, name varchar2(20));
    
    insert into t_books
    values(1000, 'java');
    
    insert into t_books
    values(2000, 'sql');
    
    select * from t_books;
    
    commit;  -- 커밋까지 해주어야 다른 워크시트에서 t_kooks를 조회했을 때 데이터까지 보임
    
    동시성 vs 일관성
    
    
##### Lock
    update t_books
    set name = 'Python'
    where no = 1000;
    
    select  * from t_books;
    
    rollback -- 오른쪽 유저는 이거 전에 기다리고 있다가 rollback하면 풀림
    

##### Deadlock


### DDL :  CREATE, ALTER, DROP, RENAME, TRUNCATE, COMMENT

    drop table t1 purge;
    create table t1
    (empno number, ename varchar2(10));

    insert into t1
    select empno, ename from emp where rownum <= 3;
    
    alter table t1 add(sal number (10,2), deptno number(2));
    alter table t1 modify(ename varchar2 (6), deptno default 10);
    alter table t1 add constraint t1_empno_pk primary key(empno);
    select * from t1;
    alter table t1 add not null (ename);  -- 에러
    alter table t1 modify ( ename not null);  -- not null 추가는 add가 아닌 modify 사용하기!
    
    rename t1 to tab1;
    truncate table tab1;
    
    comment on table tab1 is '테스트 프로젝트용';
    comment on column tab1.empno is '사번';
    comment on column tab1.ename is '사원이름';
    select * from user_tab_comments;
    select * from user_col_comments;
    
    drop table tab1;



    
