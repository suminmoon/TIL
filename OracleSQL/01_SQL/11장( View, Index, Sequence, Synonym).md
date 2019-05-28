## <11장> View, Index, Sequence, Synonym

### View

- Named Select 
- 뷰에 대한 질의는 Base Table에 대한 질의로 Query Transformation ( 예외 많음 )
 -> View merging ( view에 대한 쿼리가 table에 대한 쿼리로 바뀌어서 실행? )
- 집합의 무한 확장
- 긴 쿼리를 짧게 줄여서 사용할 수 있다.


#### Simple View ( 테이블에 있는 내용 그대로 보여줌 ) vs Complex View  

-----------------------
>simple view
-----------------------

    select empno, ename, sal
    from emp
    where deptno = 30;
    
    ed s001.sql
   
    create or replace view v1
    as 
    select empno, ename, sal
    from emp
    where deptno = 30; --- view : v1이라는 이름을 붙여 서버에 저장하는 것
    
    select view_name, text
    from user_views;
    
    select *
    from v1;  --v1을 질의 -v1은 view, view가 의미하는 select문을 찾아 쿼리 수행
 
    select empno, ename, sal
    from v1
    where sal >= 2500; --view가 의미하는 쿼리 and sal >=2500
   
   -----
   
    create or replace view vu_emp1
    as
    select empno, ename, job, sal
    from emp;
   
    select *
    from ace30.emp; -- 에러
   
    select *
    from ace30.vu_emp1;  -- 성공   (vu.emp1 view에 대한 권한만 있음)
   
   
      ---
   
    create or replace view vu_numbers
    as
    select level as no, level a, level b, level c, level d
    from dual
    connect by level <= 10;
   
    select *
    from vu_numbers;
   
   
   

-----------------------
>complex view
----------------------- 
    
    create or replace view v2
    select d.deptno 부서번호, 
            d.dname 부서이름, 
            count(*) 사원수, 
            max(e.sal) 최고급여, 
            min(e.sal) 최소급여
    from emp e, dept d
    where e.deptno = d.deptno
    group by d.deptno, d.dname;
   



    
### Index
: 데이터 저장소의 데이처가 순서없이 저장되어 있어서 이를 극복하기 위해 만든 객체로서 rowid를 전문적으로 보관함

  이익                 |         손해
------------           |    ----------------
-검색속도 향상          |    -검색속도 저하
-PK, UK 제약 강화       |    -DML 속도 저하
-FK 관련 일부 Lock 해결  |    -스토리지 소비



    
    rowid - psedocolumn 가운데 하나 
            - 64 진법
            - 6 (Object) 3 (file)  6 (block) 3(row)
    
    
    ** 오라클에서 데이터를 찾는 가장 빠른 방법은 rowid를 찾는 것임!
    
    
    
    create index emp_job_idx
    on emp(job);
    
    select job, rowid
    from emp
    order by 1,2;
    
    --
    
    아래 쿼리를 수행할 경우 오라클의 Optimizer가 인덱스 사용 여부를 판단하며
    인덱스를 사용할 경우 MANAGER라는 값으로 인덱스를 이용해서 적절한 rowid를 획득함
    
    select *
    from emp
    where job= 'MANAGER';
     
    => Index를 지정하면 테이블을 full scan 하지 않음
    => 필요한 곳으로 바로 찾아 들어감 ( 반복 실행)
    
    
### Sequence

- 11-30.Sequence를 사용할 경우 값의 Gap이 발생할 수 있음 
 -> 발생한 번호를 포함한 DML문 롤백
 -> 히나의 시퀀스를 여러 테이블에서 사용할 경우
 -> Cache 설정으로 추출한 번호를 서버 종료로 읽어버리는 경우
 
 
 
 
 ### Synonym

    create synonym sawon for employees;
    select * from sawon;
    select * from employees;
 
 
 
 
 
 
