## <5장>제어구조

### 제어구조
    
    - Selection : if, case
    - Iteration : basic loop, while loop, for loop
    - Sequence : goto, null


#### 5-28


    begin
      for i in 1..3 loop
        -- i := 100;   -- 에러 : PLS-00363: expression 'I' cannot be used as an assignment target
        p.p(i);
      end loop;
    end;
    /

문제)구구단 만들기

    begin
      for i in 2..9 loop
        for j in 1..9 loop
          p.p(i||' * '||j||' = '||i*j);
        end loop;
      end loop;
    end;
    / 

-----------------------------

## <6>장 Composite Data Type

#### 분류

    - PL/SQL Record
    - PL/SQL Collection -> Associative array (or index-by table) : PL/SQL Table
                        -> VARRAY (variable-size array)
                        -> Nested table

    -> https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/composites.htm#LNPLS005



#### 6-10 %rowtype 활용 예제

    create or replace procedure p1
     (a in  jobs.job_id%type, 
      b out jobs%rowtype)
    is
    begin
      select * into b
      from jobs
      where job_id = upper(a);
    end;
    /

    create or replace function f1(j in jobs.job_id%type)
      return jobs.job_title%type
    is
      r jobs%rowtype;
    begin
      p1(j, r);

      return r.job_title;
    end;
    /

    exec dbms_output.put_line(f1('ad_pres'))
    exec dbms_output.put_line(f1('st_man'))

#### 6-21 Collection Methods

    https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/composites.htm#LNPLS00508





















