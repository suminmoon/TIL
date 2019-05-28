## 1장.PL/SQL 소개


#### 1-13

    - procedure + function = subprogram, subroutine
    - stored procedure, stored function
    - stand-alone subprogram

    cf. MySQL Stored Procedure





    set serveroutput on -- 출력을 활성화 하기 위해 명령 실행
    
    dbms_output.put_line( )  -- oracle이 제공하는 일종의 class. 프로시저. 출력을 표시함
    
    
    --
    
    begin
        (실행문)
    end ; 
    /
    -- 필수!!



## 2장.PL / SQL 변수 선언

    변수 ( Variable )         = 그릇 ( 뚜껑이 열려있는 그릇, 데이터를 넣고 빼는 것이 자유로움)
    상수 ( Constant )        = 그릇 ( 값을 넣고 뚜껑을 덮음, 새로운 값을 넣을 수 없다)
    매개변수 ( Parameter )  = 그릇
    
    
    create or replace function tax(a number)   -- 매개변수
        return number
    is
        v_sal number  := a ;      -- 변수 : 메모리 할당, 메모리에 별명 부여(변수명), 데이터 타입 (초기화는 선택)
        v_tax constant number := 0.013 ;    -- 상수 (초기화 필수)
    begin
        return v_sal * v_tax;       -- 실행문
    end;
    /
    

    select empno, sal, tax(sal) as tax
    from emp
    where job in ('MANAGER' ,'SALESMAN');

-------
유형 6가지
![image](https://user-images.githubusercontent.com/48431771/55444697-97477500-55f2-11e9-877e-f305b32515e3.png)




#### SELECT문 유형에 따른 변수 선언 6가지

    [1]
    
    create or replace procedure p1( k number)
    is
    v_sal emp.sal%type;
    begin
        select sal into v_sal 
        from emp
        where empno = k;
        
        dbms_output.put_line(k|| '사원의 급여는 ' || v_sal || '입니다.');
    end;
    /

    set serveroutput on    
    exec p1(7788);
        
---------------    
    
    [2]
    r이라는 그릇의 칸이 8개 생성 ( emp 테이블 컬럼이 8개라서 ) 한칸한칸을 필드(테이블의 컬럼명)라고 함
    
    create or replace procedure p1 ( k number )
    is
        r emp%rowtype;   -- emp 테이블의 컬럼 구조 그대로 r이라는 그릇을 하나 만든다. ( PL/SQL 레코드)
    begin
        select * into r
        from emp
        where empno = k;
        
        dbms_output.put_line(r.empno);
        dbms_output.put_line(r.ename);
    end;
    /
    
    exec p1(7788)
    
![image](https://user-images.githubusercontent.com/48431771/55386934-7d168400-556b-11e9-84fc-e6ae9e35c976.png)

![image](https://user-images.githubusercontent.com/48431771/55386985-961f3500-556b-11e9-897f-cb6a3e99e5cc.png)

---------------

    [3] 선별적으로 리턴하는 것 ( 새로운 데이터 타입 만들기 )
    
    create or replace procedure p1( k number )
    is
     TYPE rt IS RECORD 
     (ename emp.ename%type, 
      job emp.job%type, 
      sal emp.sal%type ) ; -- 새로운 데이터 타입 생성 / 필드명을 컬럼 명과 같이 만들자(반드시는 아님 a,b,c도 가능)
    -- 생성 되었다가 end를 만나면 사라짐 -> package를 만들어 놓고 사용하자

        
     r rt;  -- r은 rt라는 데이터 타입을 따른다.
    begin
        select ename, job, sal into r
        from emp
        where empno = k ;
        
        dbms_output.put_line(r.ename );
        dbms_output.put_line(r.job );
        dbms_output.put_line(r.sal );              
    end;
    /
    
    exec p1(7788)
    ------------------
    
       ↓↓  데이터 타입 선언 부분을 package로 만들어 놓기! ( 재사용 가능 )
    
    create or replace package pack1
    is
      TYPE rt IS RECORD 
      (ename emp.ename%type, 
       job emp.job%type, 
       sal emp.sal%type ) ;
    end;
    /
    
    
     create or replace procedure p1( k number )
    is
     r pack1.rt;
        
    begin
        select ename, job, sal into r
        from emp
        where empno = k ;
        
        dbms_output.put_line(r.ename );
        dbms_output.put_line(r.job );
        dbms_output.put_line(r.sal );      
    end;
    /
    
    
    exec p1(7788)
    
    
    cf. 뷰를 활용할 경우 이렇게 구현할 수 잇음
    
    create or replace view v1
    as
    select ename, job, sal
    from emp;
    
    create or replace procedure p1(k number)
    is
        r v1%rowtype;
    begin
        select ename, job, sal into r
        from emp
        where empno = k;
        
        dbms_oupput.put_line(r.ename||' ' ||r.job||' '||r.sal);
     end;
     /
     
    
 --------------------
    [4] 한 번에 같은 종류 값 여러 개 리턴할 때 ( 배열로 만들기)
    
    create or replace procedure p1(k number)
    is 
        TYPE t1 IS TABLE OF emp.sal%type   -- 새로운 데이터 타입
        INDEX BY PLS_INTEGER;           -- 정수 값
            
        s t1;    -- t1타입을 따르는 변수 s / 변수를 만들면 매서드가 제공 됨? 
    begin
        select sal BULK COLLECT INTO s
        from emp
        where deptno = k;
        
       dbms_output.put_line(s.first);
       dbms_output.put_line(s.last);
        
        for i in s.first .. s.last loop
            dbms_output.put_line(s(i));
        end loop;                         -- 전형적인 패턴! 암기! 
                                            -- deptno = k 인 사원의 sal을 모두 뽑아내기 위해 반복문 사용                                        end;
    /
    set serveroutput on
    
    exec p1(30)
    
    cf. 다른 방법으로 명시적 커서 활용이 있음
    
    
  
    
-------------------

    [5] 레코드가 여러 개 ( 레코드는 여러 개의 데이터 타입을 갖는 변수들의 집합 )
    
    create or replace procedure p1( k number )
    is
        TYPE emp_table_type is table of emp%rowtype
        INDEX BY PLS_INTEGER;
        
        t emp_table_type;
    begin
        select * BULK COLLECT INTO t
        from emp
        where deptno = k;
        
        for i in t.first .. t.last loop
            dbms_output.put_line(t(i).empno||' ' || t(i).ename);
        end loop;
    end;
    /
    
    exec p1(10)   -- 부서 번호가 10인 모든 사원의 사원번호와 사원이름
    exec p1(30)   -- 부서 번호가 30인 모든 사원의 사원번호와 사원이름
 
------------------

[6] 레코드가 여러 개 ( 레코드 선별적, 배열 )
    
    create or replace procedure p1( k number )
    is
     TYPE rt IS RECORD 
        (ename emp.ename%type, 
         job emp.job%type, 
         sal emp.sal%type ) ;   -- rt의 데이터 타입 선언
         
     TYPE emp_table_type IS TABLE OF rt
        INDEX BY PLS_INTEGER;    -- 데이터 타입 배열로 만들기 위해!! ( 3번과 차이 )
        
    t emp_table_type;  -- t는 위에서 만든 데이터 타입을 
    begin
        select ename, job, sal BULK COLLECT INTO t
        from emp
        where deptno = k;
        
        for i in t.first .. t.last loop
            dbms_output.put_line(t(i).ename||' ' || t(i).job);
        end loop;
    end;
    /
    
    exec p1(10)
    exec p1(30)
    
------------------------------

문제) 부서와 소속 사원을 다음과 같은 형태로 나타내세요
![image](https://user-images.githubusercontent.com/48431771/55446858-6ec47880-55fc-11e9-801d-de2d6683f44f.png)







    
    
    
    
    
    
    
    
    
###################    
##### %rowtype활용 예제

    create or replace procedure 
    p1( a in jobs.job_id%type , b out jobs%rowtype ) -- out을 이렇게 쓰면 레코드가 나가게 만듦
    is
    begin
        select * into b
        from jobs
        where job_id = upper(a);
    end;
    /
    
    create or replace function f1 ( j in jobs.job_id%type )
        return jobs.job_title%type
    is
        r jobs%rowtype;
    begin
         p1( j, r );
        
        return r.job_title;
    end;
    /
    
    exec dbms_output.put_line(f1('ad_pres'));
    exec dbms_output.put_line(f1('st_man'));





##### getter, setter 처럼 만들어봅시다
    
    drop table t1 purge;

    create table t1
    as
    select * from emp;

    create or replace procedure t1_set_ename
    (a t1.empno%type,
     b t1.ename%type)
    is
    begin
      update t1
      set ename = b
      where empno = a;
    end;
    /

    create or replace function t1_get_ename
    (a t1.empno%type)
     return t1.ename%type
    is 
      v_ename t1.ename%type;
    begin
      select ename into v_ename
      from t1
      where empno = a;

      return v_ename;
    end;
    /

    select * from t1;

    exec t1_set_ename(7369, 'QUEEN')

    select * from t1;

    exec dbms_output.put_line(t1_get_ename(7369))
 
 ---

      ↓↓   package로 

    create or replace package t1_pack
      is
      procedure t1_set_ename
      (a t1.empno%type,
       b t1.ename%type);

      function t1_get_ename
        (a t1.empno%type)
       return t1.ename%type;
    end;
    /

    create or replace package body t1_pack
    is
      procedure t1_set_ename
      (a t1.empno%type,
       b t1.ename%type)
      is
      begin
        update t1
        set ename = b
        where empno = a;
      end;  

      function t1_get_ename
      (a t1.empno%type)
       return t1.ename%type
      is 
        v_ename t1.ename%type;
      begin
        select ename into v_ename
        from t1
        where empno = a;

        return v_ename;
      end;
    end;
    /

    exec t1_pack.t1_set_ename(7369, 'PRINCE')

    select * from t1;

    exec dbms_output.put_line(t1_pack.t1_get_ename(7369))


문제.t1_pack에 setter, getter를 일부 더 추가하세요.










