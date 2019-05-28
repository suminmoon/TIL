
### 환경 설정

 1.Oracle DBMS가 설치되어 있을 경우

  C:\Users\student> notepad ace.bat

    sqlplus ace번호/me@70.12.114.184:1521/xe

  C:\Users\student> ace

  SQL> show user

 2.Oracle DBMS가 설치되어 있지 않을 경우 : Instance Client 다운로드 받아서 사용

  C:\Users\student> notepad ic.bat

    set path=C:\Instructor\Software\instantclient_12_1;%path%

    sqlplus ace번호/me@70.12.114.184:1521/xe

  C:\Users\student> ic

  SQL> show user

### SQL*Plus 명령어

  - 환경설정 : show, set 
  - 결과포맷 : column, ttitle, btitle, break, ...
  - 명령편집 : list, input, append, delete, ...
  - 스크립트 파일관리 : save, get, start, ...
  - 치환변수 : &, &&, define, accept...
  - 기타     : run, clear, describe, connect, ...
  


#### 환경설정
    
    
    SQL> show all

    SQL> show sqlprompt

    SQL> set sqlprompt "Eddy> "

    Eddy> set timing on

    Eddy> set linesize 200

    Eddy> set pagesize 40

    Eddy> select * from emp;

    Eddy> show colsep

    Eddy> set colsep "|"

    Eddy> list  또는 l

    Eddy> run   또는 r, /

    Eddy> exit

    C:\Users\student> notepad login.sql

    alter session set nls_language = 'american';
    alter session set nls_territory = 'america';

    set lines 400
    set pages 100

    set serveroutput on

    C:\Users\student> ic

    SQL> select * from emp;
    
    
    
    
결과포맷 : column, break, ttitle, btitle, ...

    SQL> select department_id, employee_id, last_name, salary
       from employees
       order by department_id;

    SQL> ? column
    SQL> help column

    SQL> col last_name for a15
    SQL> r

    SQL> col salary for 999,999.99
    SQL> r

    SQL> break on department_id
    SQL> /

    SQL> break on department_id skip 1
    SQL> /

    SQL> set linesize 60
    SQL> tti 'Salary|Report'
    SQL> r

    SQL> set feedback off

    SQL> set pages 40
    SQL> bti 'Confidential'
    SQL> r

    SQL> tti off
    SQL> bti off
    SQL> clear break

    SQL> col
    SQL> col salary
    SQL> col salary clear
    SQL> clear col
    SQL> col

#### 명령편집 : list, input, append, delete, ...

    SQL> select empno
      2  from emp;

    SQL> list

    SQL> 1

    SQL> append , ename, sal    

    SQL> l
    SQL> /

    SQL> input
      3  where deptno = 30;

    SQL> l 2 3


#### 스크립트 파일 관리 : save, get, start, ....

    save  파일이름 : 버퍼 -> 파일
    get   파일이름 : 파일 -> 버퍼
    start 파일이름 : 파일 -> 버퍼 -> 실행
    @     파일이름 : 파일 -> 버퍼 -> 실행
    edit  파일이름 : 파일 생성 or 파일 편집
    edit          : 버퍼 편집
    
    
    
    
    
     spool 파일이름 ....  spool off  : 화면 캡쳐

    SQL> select empno, ename from emp;

    SQL> save s001   <- 같은 이름의 파일을 덮어쓰려면 replace 옵션 추가

    SQL> select * from dept;

    SQL> list

    SQL> get s001

    SQL> start s001

    SQL> edit s002

    select *
    from tab;

    SQL> @s002

    SQL> host dir *.sql
    SQL> host dir *.bat

    
    
바인드 변수 : var, pri ...
    
    - session이 끊어지기 전까지 존재
    - PLSQL 외부에 존재하는 변수
    - 호스트 환경에서 생성되어 데이터를 저장하기 때문에 호스트 변수라고도 한다.
    - 키워드 VARIABLE을 이용하며, SQL문이나 PL/SQL블록에서도 사용 가능하다.
    - PL/SQL블록이 실행된 후에도 액세스가 가능하다.
    - print명령을 이용하여 출력이 가능하다.
    - :(콜론) 을 붙여 사용한다.
    


    var b_sal number

    begin
      select sal into :b_sal
      from emp
    where empno = 7788;
    end;
    /

    print b_sal

    var

    select empno, ename, sal
    from emp
    where sal < :b_sal;
    

치환변수 : &, &&, define, accept, ...
생겼다 사라짐    ( &이름 )
    
    select empno, ename, sal
    from emp
    where sal < &sv_sal;

    set verify off

    r



PL/SQL 변수 : PL/SQL문 안에 존재







##### 예제 1

    variable b_annual_salary number

    declare
      v_empno emp.empno%type := &sv_empno;
    begin
      select sal*12 + nvl(comm, 0) into :b_annual_salary
        from emp
       where empno = v_empno;
    end;
    /

    Enter value for sv_empno: 7788

    print b_annual_salary


##### 예제 2

    SQL> exit

    C:\Users\student> ic

    SQL> ed sal_rep.sql

    accept sv_deptno prompt '부서 번호를 입력해 주세요 : '

    set linesize 60
    set pagesize 40
    set feedback off
    set verify off

    tti 'Salary|Report'
    bti 'Confidential'
    break on deptno skip 1
  
    spool sal_rep.txt

    select deptno, empno, ename, job, sal
    from emp
    where deptno in (&sv_deptno)
    order by deptno, empno; 

    spool off

    clear break 
    tti off
    bti off

    set linesize 400
    set pagesize 100
    set feedback on
    set verify on

    SQL> @ sal_rep.sql
    부서 번호를 입력해 주세요 : 10, 30

    SQL> @ sal_rep.sql
    부서 번호를 입력해 주세요 : 20, 30

    SQL> edit sal_rep.txt










