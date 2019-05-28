## <7장> 명시적 커서
오라클에서 CURSOR란 시스템 글로벌 영역의 공유 풀 내에 저장공간을 사용하여 사용자가 SQL 문을 실행시키면 결과값을 저장공간에 가지고 있다가 원하는 시기에 순차적으로 fetch해 처리하여 해당 결과 셋을 프로그래밍적으로 접근할수 있게 도와주는 기능이다.


--------------

명시적 커서는 처음의 맨 상단의 예제와 같이 일반적으로 어떠한 결과값을 글로벌 영역에 저장해놓고 순차적으로 값을 Fetch해 이용하기 위해 사용된다. 명시적 커서라고 불리우는 이유는 묵시적 커서와는 다르게 명시적으로 CURSOR라고 선언하고 사용하기 때문에 누가봐도 커서니깐. 그렇게 불린다. 머. 아님말고.

 명시적 커서는 간단히 아래와 같이 4단계로 나뉜다.

 CURSOR :  커서 선언
 OPEN : 커서 열기
 FETCH ~ INTO : 커서가 가리키는 곳의 결과 값을 엑세스
 CLOSE : 커서 닫기

*** 커서를 사용하지 않고 Begin ~ end; 문장 안에 select 쿼리를 하는데 여러 row가 선택되는 쿼리를 하면 에러가 발생함.
개별 로우에 순차적으로 접근하기 위해 명시적 커서를 사용한다.!!!





### 7-15

    create or replace procedure p1(w number)
    is
      cursor c1
      is
      select empno, ename, sal, deptno
      from emp
      where deptno = w
      order by sal desc;

      r c1%rowtype;
    begin
      open c1;

      loop
        fetch c1 into r;
        exit when c1%notfound or c1%rowcount > 3;
        p.p(r.empno||' '||r.ename);
      end loop;

      close c1;    
    end;
    /

    exec p1(10)
    exec p1(30)

      ↓↓

    create or replace procedure p1(w number)
    is
      cursor c1
      is 
      select empno, ename, sal, deptno
      from emp
      where deptno = w
      order by sal desc;
    begin 
      for r in c1 loop
        p.p(r.empno||' '||r.ename);
      end loop;
    end;
    /

    exec p1(10)
    exec p1(30)

      ↓↓

    create or replace procedure p1(w number)
    is
    begin 
      for r in (select empno, ename, sal, deptno
                from emp
                where deptno = w
                order by sal desc) loop
        p.p(r.empno||' '||r.ename);
      end loop;
    end;
    /

    exec p1(10)
    exec p1(30)

문제)다음과 같은 결과를 만드세요

![image](https://user-images.githubusercontent.com/48431771/55536103-e9bc8a80-56f3-11e9-8915-9a59f22d25df.png)


    create or replace procedure p1(w number)
    is
    begin 
      for d in (select * from dept) loop
      end loop;
    end;
    /

    create or replace procedure p1(w number)
    is
    begin 
      for d in (select * from dept) loop
        for e in (select empno, ename, sal from emp) loop
        end loop;
      end loop;
    end;
    /

    create or replace procedure p1
    is
    begin 
      p.p('------------------------');
      for d in (select * from dept) loop
        p.p(d.deptno||' '||d.dname||' '||d.loc);
        p.p('------------------------');
        for e in (select empno, ename, sal
                  from emp 
                  where deptno = d.deptno) loop
          p.p(e.empno||' '||e.ename||' '||e.sal); 
        end loop;
        p.p('------------------------');
      end loop;
    end;
    /

#### 7-26

    drop table t1 purge;
    drop table t2 purge;

    create table t1 as select * from dept;
    create table t2 as select * from emp;

    create or replace procedure p1(w varchar2)
    is
      cursor c1
      is
      select e.empno, e.ename, e.sal, e.deptno
      from t2 e, t1 d
      where e.deptno = d.deptno
      and d.loc = w
      for update of e.sal wait 5;

      r c1%rowtype;
    begin
      open c1;

      loop
        fetch c1 into r;
        exit when c1%notfound;
        update t2
        set sal = r.sal * 1.1
        where empno = r.empno;
      end loop;

      close c1;
    end;
    /

    select * from t2;

    exec p1('DALLAS')

      ↓↓

    create or replace procedure p1(w varchar2)
    is
      cursor c1
      is
      select e.empno, e.ename, e.sal, e.deptno
      from t2 e, t1 d
      where e.deptno = d.deptno
      and d.loc = w
      for update of e.sal wait 5;
    begin
      for r in c1 loop
        update t2
        set sal = r.sal * 1.1
        where empno = r.empno;
      end loop;
    end;
    /

    select * from t2;

    exec p1('DALLAS')

      ↓↓

    create or replace procedure p1(w varchar2)
    is
      cursor c1
      is
      select e.rowid as rid, e.empno, e.ename, e.sal, e.deptno
      from t2 e, t1 d
      where e.deptno = d.deptno
      and d.loc = w
      for update of e.sal wait 5;
    begin
      for r in c1 loop
        update t2
        set sal = r.sal * 1.1
        where rowid = r.rid
      end loop;
    end;
    /

    select * from t2;

    exec p1('DALLAS')

      ↓↓

    create or replace procedure p1(w varchar2)
    is
      cursor c1
      is
      select e.empno, e.ename, e.sal, e.deptno
      from t2 e, t1 d
      where e.deptno = d.deptno
      and d.loc = w
      for update of e.sal wait 5;
    begin
      for r in c1 loop
        update t2
        set sal = r.sal * 1.1
        where current of c1;
      end loop;
    end;
    /

    select * from t2;

    exec p1('DALLAS')

    select * from t2;


 ## <8장> 예외 처리


### Error

    - Syntax error
    - Logical error
    - Runtime error -> Oracle-defined Exception -> Predefined exception     ->[1] when 이름 then
                                                -> Non-predefined exception ->[2] 선언 -> 이름부여 -> 자동발생 -> 처리
                                                                            ->[3] when others then
     (Exception)   -> User_defined Exception                                ->[4] 선언 -> raise -> 처리
                                                                            ->[5] raise_application_error 프로시저


#### 예제

 - Every Oracle error has a number,
      but exceptions must be handled by name.

#### Exception 처리 예제들

[1] when 이름 then

    (0) Predefined exception의 정체를 확인해 보세요
  
      1.파일을 여세요

        C:\Users\student> notepad c:\oraclexe\app\oracle\product\11.2.0\server\rdbms\admin\stdspec.sql
  
      2.다음으로 시작되는 파트를 찾으세요

        /********** Predefined exceptions **********/
        

    (1) 발생한 Exception을 제대로 처리하지 못하는 경우
  
    drop table t1 purge;
    create table t1 (no number);

    create or replace procedure p1(a number, b number)
    is
    begin
      insert into t1 values(1000);
      p.p(a/b);
    end;
    /

    exec p1(100, 2)

    select * from t1;    -> 입력된 1000이 확인됨

    rollback;

    exec p1(100, 0)

    select * from t1;    -> no rows selected
    
-------

    (2) 발생한 Exception을 제대로 처리하는 경우

    create or replace procedure p1(a number, b number)
    is
    begin
      insert into t1 values(1000);
       p.p(a/b);
    exception
      when zero_divide then
        p.p('0으로 나눌 수 없습니다!');
      when others then
        p.p('에러 발생!');
    end;
    /

    exec p1(100, 0)

    select * from t1;  -> exception 발생 이전의 입력 데이터가 그대로 남아있음

    rollback;

[2] 선언 -> 이름부여 -> 자동 발생 -> 처리

    drop table t1 purge;

    create table t1 (no number not null);

    create or replace procedure p1(a number)
    is
      e_null exception;
      pragma exception_init(e_null, -1400);
    begin
      insert into t1 values(a);
    exception
      when e_null then
        p.p('null값 입력할 수 없습니다!');
    end;
    /

    exec p1(null)

      ↓↓

    create or replace package exception_pack
    is
      e_null exception;
      pragma exception_init(e_null, -1400);
    end;
    /

    create or replace procedure p1(a number)
    is
    begin
      insert into t1 values(a);
    exception
      when exception_pack.e_null then
        p.p('null값 입력할 수 없습니다!');
    end;
    /

    exec p1(null)







[3] when others then

    create or replace procedure p1(a number)
    is
    begin
      p.p('다른 문장이 많음');
      insert into t1 values(a);
    exception
      when others then
        p.p(sqlcode);
        p.p(sqlerrm);
    end;
    /

    exec p1(null)




    create or replace procedure p1(e number)
    is
      v_sal emp.sal%type;
      e_low exception;
    begin
      p.p('중요한 작업들');

    select sal into v_sal
    from emp
    where empno = e;

    if v_sal < 3000 then
      raise e_low;
    end if;

    p.p(v_sal);    
    exception
      when e_low then
        p.p('급여가 너무 적어요!');
    end;
    /

    exec p1(7788)
    exec p1(7900)














