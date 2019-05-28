## 조인(Join)이란?

  from절에 테이블이 두 개 이상!

### 조인 용어
    
    select *
    from emp, dept     -- 조인, Cartesian product, row 복제
    order by 1;

    select e.empno, e.ename, d.*
    from emp e, dept d             -- Join statment
    where e.deptno = d.deptno       -- Join predicate
    and e.sal >= 1000             -- Non-Join predicate
    and e.job like 'A%'           -- Non-Join predicate
    and d.deptno = 20             -- Non-Join predicate (Sigle row predicate)
    order by 1;


### JOIN (for 루프)
**-> sql문에서 from 절 테이블이 2개 이상이면 join!**

    select * 
    from emp, dept　　--조인, Cartesian product, row 복제
    order by 1;

join할 때 
1. 정확하게 from에 어떤 테이블을 쓰는지 정해야한다.
2. 

    select emp.empno, emp.ename, dept.*
    from emp, dept
    where emp.deptno = dept.DEPTNO
    order by 1;
-> 사원쪽 deptno 와 부서의 deptno가 같은 것 True인 것 남기기
-> select 출력은 사원의.사원번호, 사원의.이름, 부서의.모두  


### 조인 분류

    - Oracle Syntax
     - Equi join, Inner join  (등가   조인, 내부 조인)
     - Nonequi join           (비등가 조인)
     - Outer join             (외부   조인)
     - Self join              (자체   조인)

    - SQL:1999 표준 Syntax
     - Cross join
     - Natural join
       : 이름이 같은 두 테이블의 모든 행을 기반으로 한다.
         두 테이블에서 대응되는 모든 열의 값이 동일한 행을 선택한다.
         동일한 이름을 가진 열이 서로 다른 데이터 유형을 가지면 오류 반환된다.
     - Join Using
       : 여러 열이 이름은 같지만 데이터 유형은 다를 경우 USING절을 사용하여 Equijoin에 대한 열을 지정할 수 있다.
         using 절을 사용하면 두 개 이상의 열이 일치하는 경우 하나의 열만 일치하도록 할 수 있다.
     - Join On
     - Outer join
____________________________________________________________________

Equi Join
    
    - 가장 일반적으로 사용하는 Equality Condition (=)에 의한 조인
    - Equi join의 성능을 높이기 위해서는 Index 기능을 사용하는 것이 좋다.
    
      select e.empno, e.ename, d.dname
        from emp e, dept d
       where d.deptno = e.deptno;
       
       
    콤마(,) 대신 INNER JOIN을 사용할 수 있으며 INNER는 생략 가능하다. JOIN 조건은 ON 절에 온다.
      
      select e.empno, e.ename, d.dname
        from dept d
       INNER JOIN emp e
          on d.deptno = e.deptno;
          
    NATURAL JOIN을 사용하면 동일한 컬럼을 내부적으로 모두 조인하므로 ON절이 생략 가능하다.      
        
        select e.empno, e.ename, d.dname
          from dept d
         NATURAL JOIN emp e;
         
    NATURAL JOIN의 단점은 동일한 이름을 가지는 컬럼은 모두 조인이 되는데 USING문을 사용하면 컬럼을 선택해서 조인할 수 있다.
        
        select e.empno, e.ename, d.dname
          from emp e
          JOIN dept d
         USING (deptno) ;
         
Non-Equi Join
    
    - 테이블의 어떤 column도 join할 테이블의 column에 일치하지 않을 때 사용하고, 조인조건은 동등 (=)이외의 연산자를 갖는다.
    - BETWEEN AND, IS NULL IS NOT NULL, IN, NOT IN
    - 거의 사용하지 않는다.
    
      select e.ename, e.sal. s.grade
        from emp e, salgrade s
        where e.sal
       BETWEEN s.losal
          AND  s.hisal;
          
          
          
          
          
 Self Join
     
     - Equi Join과 같으나 하나의 테이블에서 조인이 일어나는 것이 다르다.
     - 같은 테이블에 대해 두 개의 alias를 사용하여 FROM절에 두 개의 테이블을 사용하는 것처럼 조인한다.
     
      select e.ename, a.ename "MANAGER"
        from emp e, emp a
       where e.empno = a.mgr;
       -- 사원의 매니저명을 조회하는 self join 예제
    
    

 -------------------------
 Outer Join
     
     - Equi Join은 조인을 생성하려는 두 개의 테이블을 한 쪽 컬럼에서 값이 없다면 테이터를 반환하지 못한다.
     - 동일 조건에서 조인 조건을 만족하는 값이 없는 행들을 조회하기 위해 Outer Join을 사용한다.
     - Outer Join 연산자는 (+)이다.
     - 조인시 값이 없는 조인측에 (+)를 위치시킨다.
     - Outer Join 연산자는 표현식의 한 편에만 올 수 있다.
     
     
     
     
![image](https://user-images.githubusercontent.com/48431771/55401764-adbae580-558c-11e9-9db0-fecc70271b74.png)
![image](https://user-images.githubusercontent.com/48431771/55401782-bdd2c500-558c-11e9-9bb8-d87ef1fe8197.png)


-------------
LEFT, RIGHT, FULL Outer Join

![image](https://user-images.githubusercontent.com/48431771/55401834-dba02a00-558c-11e9-9efe-58734c497b71.png)










----------------------------------

### JOIN함수    

    select * 
    from EMPLOYEES, DEPARTMENTS
    where department_id = department_id
    order by 1;    
=> 에러 발생

    select * 
    from EMPLOYEES e, DEPARTMENTS d
    where e.department_id = d.department_id
    order by 1;    
 => 조인할 때, where에 테이블 명 붙여주기 (alias로 하는 것이 좋음 , 테이블 명 너무 김)

    select * 
    from EMPLOYEES e, DEPARTMENTS d
    where e.department_id = d.department_id and e.salary >= 3000
    order by 1;    

**- 조인할 때 테이블 중 개수가 많은 것부터 적어주기!!**
**- 조인할 때 테이블 명 적어주는 이유는 두 테이블 간 겹치는 컬럼 명이 있을 수도 있기 때문이다. 겹치는 컬럼 명이 없더라도 습관적으로 테이블 명을 적어주도로 하자!**



    select s.grade , e.empno, e.job, e.sal
    from emp e, salgrade s
    where e.sal >= s.losal and e.sal <= s.hisal
    order by s.grade, e.sal desc;
__________________________________
    
    select s.grade, count(*) as 인원수, round(avg(e.sal)) as 평균급여, 
               round(stddev(e.sal)) as 급여표준편차
    from emp e, salgrade s
    where e.sal >= s.losal and e.sal <= s.hisal
    group by s.grade
    order by s.grade;
________________________________________

    select a.grade, a.empno, a.job, a.sal, b.인원수, b.평균급여, b.급여표준편차
    from (select s.grade , e.empno, e.job, e.sal
            from emp e, salgrade s
            where e.sal >= s.losal and e.sal <= s.hisal
            order by s.grade, e.sal desc) a,
        (select s.grade, count(*) as 인원수, round(avg(e.sal)) as 평균급여, 
            round(stddev(e.sal)) as 급여표준편차
            from emp e, salgrade s
            where e.sal >= s.losal and e.sal <= s.hisal
            group by s.grade
            order by s.grade) b
    where a.grade = b.grade
    order by a.grade, a.sal desc;
    
    
    ______________________________________________________________

### 냉장고를 살펴라 ≒ 데이터의 상황을 확인하라

  https://docs.oracle.com/cd/E18283_01/server.112/e10831/diagrams.htm#CIHGFFHI

    select 'select * from '||tname||';' as 질의문
    from tab;
  
  ### ORACLE SYNTAX 기준 
 
  문제)부서와 부서에 속한 사원들의 ...를 쿼리하세요

    select * from departments;   -  8 rows
    select * from employees;     - 20 rows

    select *
    from employees, departments
    order by 1;

    select /* equi join */
         *
    from employees e, departments d 
    where e.department_id = d.department_id
    order by 1;

    cf. Outer Join

        select /* outer join */
               e.employee_id, e.department_id, d.department_id
        from employees e, departments d 
        where e.department_id = d.department_id (+)
        order by 1;
 
        select /* outer join */
               e.employee_id, e.department_id, d.department_id
        from employees e, departments d 
        where e.department_id (+) = d.department_id
        order by 1;

    cf. 추가 가공

        select *
        from employees e, departments d 
        where e.department_id = d.department_id 
         and e.salary >= 3000
        order by 1;

        select d.department_id, 
               d.department_name, 
               e.employee_id,
               e.job_id,
               e.salary
          from employees e, departments d 
         where e.department_id = d.department_id
           and e.salary >= 3000
        order by 1;

        select d.department_name, 
               e.job_id,
               count(*) 인원수,
               sum(salary) 급여합,
               round(stddev(salary)) 급여표준편차
          from employees e, departments d 
         where e.department_id = d.department_id
           and e.salary >= 3000
         group by d.department_name,
                  e.job_id
         order by 1;

  문제)사원과 사원들의 급여 등급을 쿼리하세요
 
    select * from salgrade;    -  5 rows
    select * from emp;         - 14 rows

    select *
    from emp e, salgrade s
    order by 1;

    select *
    from emp e, salgrade s
    where e.sal >= s.losal and e.sal <= s.hisal
    order by 1;

    select /* nonequi join */
           s.grade, e.empno, e.job, e.sal
    from emp e, salgrade s
    where e.sal >= s.losal and e.sal <= s.hisal
    order by s.grade, e.sal desc;

    cf. 추가 가공

        select s.grade,
               count(*) 인원수,
               round(avg(e.sal)) 평균급여,
               round(stddev(e.sal)) 급여표준편차
          from emp e, salgrade s
         where e.sal >= s.losal 
           and e.sal <= s.hisal
         group by s.grade
         order by s.grade;

        select a.grade, a.empno, a.job, a.sal, b.인원수, b.평균급여, b.급여표준편차
        from (select s.grade, e.empno, e.job, e.sal
                from emp e, salgrade s
               where e.sal >= s.losal and e.sal <= s.hisal
               order by s.grade, e.sal desc) a,
             (select s.grade,
                     count(*) 인원수,
                     round(avg(e.sal)) 평균급여,
                     round(stddev(e.sal)) 급여표준편차
                from emp e, salgrade s
               where e.sal >= s.losal 
                 and e.sal <= s.hisal
               group by s.grade
               order by s.grade) b
         where a.grade = b.grade
         order by a.grade, a.sal desc;

  문제)7844 사원보다 많은 급여를 받는 사원?

    select *
      from emp e, emp t
     where t.empno = 7844;

    select /* self join + nonequi join */
           e.empno, e.sal, t.empno, t.sal
      from emp e, emp t
     where t.empno = 7844
       and e.sal > t.sal;

  문제)누적합 구하기 

           A          B   누적합
    -------- ---------- --------
        7369        800      800
        7499       1600     2400
        7521       1250     3650

    drop table t1 purge;
 
    create table t1
    as
    select empno a, sal b 
    from emp 
    where rownum <= 3;

    select * 
    from t1;

    select *
    from t1 a, t1 b;

    select *
    from t1 a, t1 b
    where a.a >= b.a
    order by a.a;

    select /* self join + nonequi join */
      a.a, a.b, sum(b.b) 누적합
    from t1 a, t1 b
    where a.a >= b.a
    group by a.a, a.b
    order by a.a;










