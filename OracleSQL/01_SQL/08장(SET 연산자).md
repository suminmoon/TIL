## <8장> SET 연산자(a.k.a 수직 조인)


### 연산자의 종류

    - UNION ALL : 합집합(중복 허용)
    - UNION     : 합집합(중복 제거)
    - INTERSECT : 교집합(중복 제거)
    - MINUS     : 차집합(중복 제거)

   예) A = {1, 1, 1, 2, 2, 3, 3, 3}
       B = {3, 3, 4, 4, 4, 5, 5}

     A union all B = {1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5}
     A union     B = {1, 2, 3, 4, 5}
     A intersect B = {3}
     A minus     B = {1, 2}

문제)근무하는 사원이 있는 부서의 부서번호?

    select deptno from dept
    intersect
    select deptno from emp;

문제)근무하는 사원이 없는 부서의 부서번호?

    select deptno from dept
    minus
    select deptno from emp;

문제)부하직원이 있는 사원의 사번?

    select empno from emp
    intersect
    select mgr from emp;

문제)부하직원이 없는 사원의 사번?

    select empno from emp
    minus
    select mgr from emp;

문제)집계, 소계, 총계를 쿼리하세요

    select deptno, job, sum(sal)
    from emp
    group by deptno, job
    union all
    select deptno, null, sum(sal)
    from emp
    group by deptno
    union all
    select null, null, sum(sal)
    from emp
    order by 1, 2;

문제)빠진 번호 찾기

    drop table t1 purge;

    create table t1
    as
    select level no
    from dual
    connect by level <= 100;

    delete from t1
    where no in (select trunc(dbms_random.value(1, 100)) 
                 from dual
                 connect by level <= 7);

    select level no
    from dual
    connect by level <= 100
    minus
    select no
    from t1;
