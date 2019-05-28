## PL/SQL Program Unit
: SQL 만으로는 그 기능을 다 쓸 수 없기 떄문에 PL/SQL을 사용하여 프로그램밍 언어로 표현
(실행문(begin~end)에 SQL + PL/SQL )

개념정리 블로그 : http://www.gurubee.net/lecture/1343


    - Pascal -> Ada -> Pl/SQL
    - SQL(Manipulation power) + 3GL(Processing power) = PL/SQL

    - Block Structured Language -> Anonymous block ( 이름이 없는 block )
                                -> Named block        : procedure, function
    
    
    
#### 전형적인 Anonymous block

    declare                  -- 옵션
        선언부
    begin                   -- 필수
        실행부
    exception              -- 옵션
        예외처리부
    end;                     -- 필수
    


  
     - SQL 엔진 + PL/SQL 엔진

     - 할당 연산자 vs 비교 연산자

                  C, Java    Basic, PowerScript   Pascal, PL/SQL
    할당 연산자   A = B      A = B                A := B
    비교 연산자   A == B     A = B                A = B


    set serveroutput on
    begin
        dbms_output.put_line('Hello world');
    end;
    /
    
    begin
        for i in 1..10 loop
        DBMS_OUTPUT.PUT_LINE(i ||'번째, Hello world!');
        end loop;
    end;
    /
    
    declare
        v_sal number ;
    begin
        select sal into v_sal
        from emp
        where empno = 7788;
        
        dbms_output.put_line(v_sal);
    end;
    /
    

__________________________________________

#### Named block ( 이름을 붙이는 이유는 : 그 일을 반복적으로 시키기 위해 )

    create or replace procedure p1
    is
    begin
        DBMS_OUTPUT.PUT_LINE('Hello world!');
    end;
    /
    
    select object_name, object_type
    from user_object
    order by 2,1;
    
    select name, text
    from user_source;
    
    execute p1;
    
    
    
    create or replace procedure p1(a number)
    is
        v_sal number;
    begin
        select sal into v_sal
        from emp
        where empno = a;
        
        DBMS_OUTPUT.PUT_LINE('Hello world!');
    end;
    /


-------------------

    <예제들> 
    
    set serveroutput on
    create or replace procedure emp_avg_sal(a number)   -- 이름 붙여주기!!
    is
        v_avg_sal number;
    begin
        select avg(sal) into v_avg_sal
        from emp
        where deptno = a;
        DBMS_OUTPUT.PUT_LINE(round(v_avg_sal,2));
    end;
    /
   
    exec emp_avg_sal(30)
    exec emp_avg_sal(10)
        
    ---
    
    
 #### emp_avg_sal 프로시저 사용 ( 리턴 값 없는 )
 
     -- 결과를 바로 화면으로 뿌리지 않고 b로 나오게 하는 경우       
    create or replace procedure emp_avg_sal(a in number, b out number)   -- a 들어오는 b 나가는 매개변수
     is
    begin
        select round(avg(sal),2) into b
        from emp
        where deptno = a;
    end;
    /
    
    show errors
    
---
    
    create or replace procedure emp_sal_compare(a number)
    is
        v_sal emp.sal%type;    -- v_sal은 emp테이블의 sal type을 따라라
        v_deptno emp.deptno%type;  ---- v_deptno는 emp테이블의 deptno type을 따라라
        v_avg_sal number;
    begin
        select sal, deptno into v_sal, v_deptno
        from emp
        where empno = a;
        
        emp_avg_sal(v_deptno, v_avg_sal);  -- 위 실행에서 input a 와 output b 사용
        
        if v_sal > v_avg_sal then
             DBMS_OUTPUT.PUT_LINE('소속 부서 평균 급여보다 큼');
        elsif v_sal < v_avg_sal then
              DBMS_OUTPUT.PUT_LINE('소속 부서 평균 급여보다 적음');
        else
              DBMS_OUTPUT.PUT_LINE('소속 부서 평균 급여와 같음');
        end if;
        
    end;
    /
    
    set serveroutput on
    exec emp_sal_compare(7900);
    
    
    
    ---

![image](https://user-images.githubusercontent.com/48431771/55371194-45daaf80-5538-11e9-95b0-a0cce6019774.png)

    
    
#### emp_avg_sal 프로시저를 함수로 변경할 경우 ( 리턴 값 있는 )


    drop procedure emp_avg_sal;
    
    create or replace function emp_avg_sal (p_deptno emp.deptno%type)   
    
        return number -- return이 있을 경우 여기 표현해야 함
     is
     b number ;
     
    begin  -- 실행문 안에 SQL
        select round(avg(sal),2) into b
        from emp
        where deptno = p_deptno;
        
        return b;   -- function은 return문이 꼭 들어가야 함!!!
    
    end;
    /
    
    select deptno, emp_avg_sal(deptno) avg_sal 
    from dept;
    
---


    create or replace procedure emp_sal_compare(a number)
    is
        v_sal emp.sal%type;    -- v_sal은 emp테이블의 sal type을 따라라
        v_deptno emp.deptno%type;  ---- v_deptno는 emp테이블의 deptno type을 따라라
       
    begin
        select sal, deptno into v_sal, v_deptno
        from emp
        where empno = a;
        
        
        if v_sal > emp_avg_sal(v_deptno) then
             DBMS_OUTPUT.PUT_LINE('소속 부서 평균 급여보다 큼');
        elsif v_sal < emp_avg_sal(v_deptno) then
              DBMS_OUTPUT.PUT_LINE('소속 부서 평균 급여보다 적음');
        else
              DBMS_OUTPUT.PUT_LINE('소속 부서 평균 급여와 같음');
        end if;
        
    end;
    /
    
    exec emp_sal_compare(7900);
    


![image](https://user-images.githubusercontent.com/48431771/55380601-a0d1ce00-555b-11e9-8ea0-666e7711fb82.png)





