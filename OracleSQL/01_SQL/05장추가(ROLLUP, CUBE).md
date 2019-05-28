## SQL for Aggregation in Date Warehouses

1. AGGREGATE FUNCTION : count , sum , avg , max , min 등 각종 집계 함수

2. GROUP FUNCTION : 결산 개념의 업무, 소계, 중계, 합계, 총 합계등 보고서를 만드는 기능

3. WINDOW FUNCTION : 분석함수나 순위함수 같은 데이터 웨어하우스에서 발전한 기능



공인 교재

    오라클 SQL 교재 2-2 부록 F  

### 소개 
https://docs.oracle.com/cd/E11882_01/server.112/e25554/aggreg.htm#DWHSG020

    - ROLLUP Extension to GROUP BY
    - CUBE Extension to GROUP BY
    - GROUPING Functions
    - GROUPING SETS Expression
    - Composite Columns
    - Concatenated Groupings

#### Test 데이터 준비

    drop table t1 purge;

    create table t1
    as
    select deptno a, job b, 'M' as c, ceil(sal*dbms_random.value(1, 2)) d
    from emp;

    insert into t1
    select deptno a, job b, 'W' as c, ceil(sal*dbms_random.value(1, 2)) d
    from emp;

    select * from t1;


#### ROLLUP Extension to Group by


    - 컬럼의 갯수가 n개면 결과 집합의 종류는 n+1가지임
    - 컬럼의 나열 순서가 중요



    select a, b, sum(d)
    from t1
    group by ROLLUP(a, b);                    

    select a, b, sum(d)
    from t1
    group by GROUPING SETS((a, b), (a), ());

    --

    select a, b, c, sum(d)
    from t1
    group by ROLLUP(a, b, c);  

    select a, b, c, sum(d)
    from t1
    group by GROUPING SETS((a, b, c), (a, b), (a), ());

#### CUBE Extension to GROUP BY

    - 컬럼의 갯수가 n개면 결과 집합의 종류는 2^n가지임
    - 컬럼의 나열 순서가 중요하지 않음

    select a, b, sum(d)
    from t1
    group by CUBE(a, b);                    

    select a, b, sum(d)
    from t1
    group by GROUPING SETS((a, b), (a), (b), ());

    --

    select a, b, c, sum(d)
    from t1
    group by CUBE(a, b, c)
    order by a, b, c;

    select a, b, c, sum(d)
    from t1
    group by GROUPING SETS((a, b, c), (a, b), (b, c), (a, c),
                           (a), (b), (c), ())
    order by a, b, c;
    
#### GROUPING Functions

    drop table t_emp purge;

    create table t_emp
    as
    select * from emp;

    select deptno, job, sum(sal)
    from t_emp
    group by rollup(deptno, job);

    --

    ** Data에 Null이 포함되어 결과를 구분하기 힘듦

    update t_emp
    set job = null
    where rownum = 1;

    select deptno, job, sum(sal) as sum_sal
    from t_emp
    group by rollup(deptno, job);

    select *
    from (select deptno, job, sum(sal) as sum_sal
          from t_emp
          group by rollup(deptno, job))
    where deptno is not null
    and   job    is null;


         ↓↓

    Grouping 함수를 이용해서 문제 해결

    select deptno, job, sum(sal) as sum_sal, grouping(deptno), grouping(job)
    from t_emp
    group by rollup(deptno, job);

    select deptno, job, sum_sal
    from (select deptno, 
                 job, 
                 sum(sal) as sum_sal,
                 grouping(deptno) as g_deptno, 
                 grouping(job) as g_job
          from t_emp
          group by rollup(deptno, job))
    where g_deptno in (0, 1)
    and   g_job    = 1;

#### Composite Columns

    select a, b, c, sum(d)
    from t1
    group by ROLLUP(a, b, c);      -- (a, b, c), (a, b), (a), ()

    select a, b, c, sum(d)
    from t1
    group by ROLLUP(a, (b, c));    -- (a, b, c), (a), ()

    select a, b, c, sum(d)
    from t1
    group by ROLLUP((a, b), c);    -- (a, b, c), (a, b), ()

    select a, b, c, sum(d)
    from t1
    group by ROLLUP((a, b, c));    -- (a, b, c), ()

#### GROUPING SETS Expression

    - Rollup, Cube에 비해 좀 더 세부적인 집합 요청이 가능함

    select a, b, c, sum(d)
    from t1
    group by GROUPING SETS((a, b, c), (a, c), (b), ())
    order by a, b, c;

#### Concatenated Groupings

https://docs.oracle.com/cd/E11882_01/server.112/e25554/aggreg.htm#i1007021

    Concatenated groupings offer a concise way to generate useful combinations of groupings. 

    group by a, rollup(b), cube(c)
  
             a      b         c       a, b, c
                   ()         ()      a, b
                                      a, c
                                      a
             1   *  2   *     2

    group by grouping sets((a, b, c), (a, b), (a, c), (a))

     ----

    GROUP BY ROLLUP(calendar_year, calendar_quarter_desc, calendar_month_desc),
             ROLLUP(country_region, country_subregion, countries.country_iso_code, cust_state_province, cust_city),
             ROLLUP(prod_category_desc, prod_subcategory_desc, prod_name);

    GROUP BY GROUPING SETS((calendar_year, calendar_quarter_desc, calendar_month_desc, country_region, country_subregion,           countries.country_iso_code, cust_state_province, cust_city, prod_category_desc, prod_subcategory_desc, prod_name),
                           (calendar_year, calendar_quarter_desc, calendar_month_desc, country_region, country_subregion,   countries.country_iso_code, cust_state_province, cust_city, prod_category_desc, prod_subcategory_desc),
                           (), ...)



    
 
