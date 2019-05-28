
 ## Data Modeling and Database Design


### 용어

    - Data Modeling?
  
      ~ Logical Modeling         -> Relational Modeling -> Physical Modeling 
      ~ 개념모델링 -> 논리모델링 -> 물리모델링
      ~ Data Modeling            -> Database Design

    - Data Modeling   : http://en.wikipedia.org/wiki/Data_modeling
    - Database Design : http://en.wikipedia.org/wiki/Database_Design

#### 실습

    - http://me2.do/xMvTWFRe : Modeling for a Small Database
    - http://me2.do/xeidjI0a : Re-engineering Your Database Using Oracle SQL Developer Data Modeler 4.0 
    - http://me2.do/xpctClDk : Sample Models and Scripts
    - http://me2.do/FDTFsJOh : Online Demonstrations - Data Modeler
    - http://me2.do/GGRz4LjY : Searching Models in Oracle SQL Developer Data Modeler 4.0

SQL 활용 능력이 Database Design에 큰 영향을 줍니다.

    - http://me2.do/FWF1jH60 : 오라클 실습
    - http://me2.do/GkFy9CQD : DW 매뉴얼 21장 이후 


-------------------
 관련 교재 및 툴
-------------------

  - 아는 만큼 보이는 데이터베이스 설계와 구축(이춘식) 
  - 데이터베이스 설계와 구축(이춘식) 
  - 관계형 데이터 모델링 프리미엄 가이드
  - 오용철의 데이터베이스 모델링
  - 이화식님의 모델링 강의

  - Oracle SQL Developer Data Modeler : http://me2.do/xawupCez (오라클)
  - Data Ware                         : http://www.encore.co.kr/academy/course_info/103976
  - ERWin 등 권장 무료교육            : http://cyber.dbguide.net/user/apply/Apply.jsp

  - 국가공인 DAP 자격증 : http://www.dbguide.net/da.db?cmd=snb2_1


----------------------------------
 System Development Cycle           
----------------------------------

    Business Information Requirements 
     
       ↓ 
  
    Data Modeling (Conceptual) : Basic, Advanced 

       ↓

    (CRUD Matrix 및 여러 가지 질문으로 Data Model 검토)
 
       ↓

    Database Design

       ↓

    (Performance를 고려한 Database Design 수정 : PK 컬럼 조정, Denomalization 등)

       ↓
  
    Database Build



### Entity (개체)
----------------------

  - Is something that exists separately from other things
    and has a clear identity of its own. (by 네이버 영영 사전)

  - Is a thing of significance.
    
  - Must have attributes.
  - Must have multiple instances.
  - Must have a Unique Identifier(UID).

  ----------
  Entity를 찾는 순서

      0.무엇을 이용해서 엔티티를 찾을 것인가? 장표(보고서), 업무기술서, 인터뷰, 예전 시스템, 현장조사, DFD 등

       1.명사를 찾으세요. 업무에 중요한 것인가요?

       2.Entity 이름을 지으세요.

       3.Attribute를 찾으세요.

       4.Instance를 찾으세요.
  
       5.UID를 찾으세요.

       6.그림으로 그리세요.


  - 엔티티 검증의 대표적인 기법 : CRUD Matrix 등
  - 엔티티 검토용 질문 



### Relationship (관계)
----------------------

Relationship을 찾는 순서

    1.Existence : Relationship Matrix
 
    2.Name      : Relationship Matrix 

    3.Optionality

    4.Degree

    5.Validate : 관련자들 앞에서 큰 소리로 떠들기

 Relationship Syntax

    Each entity1   must be     relationship name    one or more      entity2.
    Each entity1   may be      relationship name    one or more      entity2.
    Each entity1   must be     relationship name    one and only one entity2.
    Each entity1   may be      relationship name    one and only one entity2.
 
                [optionality]        [name]           [Degree]

    cf.A degree of 0 is addressed by may be.

  
  Relationship Types : 1:1 or 1:M or M:M
  Relationship을 맺으면 UID가 컬럼화 되어 컬럼 개수가 늘어남


### Attribute (속성)
----------------------

  - Is a quality or feature that someone or something has. (by 네이버 영영사전)

 Attribute 찾는 순서

    1.Attribute 후보를 찾아서 Entity에 표현하세요.

    2.더 작은 단위의 Attribute로 나눌 수 있나요?

    3.Single valued Attribute인가요?                 -> A repeated attribute indicates a missing entity!!!

    4.Derived Attribute는 아니겠지요?

    5.정말 Attribute인가요? 혹시 Entity가 아닌가요?  -> If an attribute has their own attributes, then it is an entity!!!

    6.필수 속성인가 판단하세요. 



### Unique Identifier (식별자)
-----------------------------

  - UID : A, A++, A+R, R++

 UID 찾는 순서

    1.Attribute를 이용해서 UID 결정하세요.

    2.필요할 경우 Attribute + Relationship으로 UID를 결정하세요.

    3.필요할 경우 Artificial Attribute를 이용해서 UID를 결정하세요.

    cf.1:M 관계에서 1쪽의 UID가 복잡할 경우 Database Design시에 M쪽에 컬럼이 많이 생긴다.

    - [식별자 관계(UID의 일부가 되는 Relationship)]와 [비식별자 관계(UID의 일부가 되지 않는 Relationship)]를 결정

      ~ 식별자 관계   -> PK 구조가 복잡해진다. 중복이 많아진다. 

	A : REGIONS 

	a1 (pk)
	a2

	B : COUNTRY

	b1 (pk)
	b2
	a1 (pk), (fk)

	C : DEPT

	c1 (pk)
	c2
	b1 (pk), (fk)
	a1 (pk), (fk)

	D : EMP

	d1 (pk)
	d2
	c1 (pk), (fk)
	b1 (pk), (fk)
	a1 (pk), (fk)

      ~ 비식별자 관계 -> 정보가 단절되어 과다한 조인이 필요해진다.

	A : REGIONS 

	a1 (pk)
	a2

	B : COUNTRY

	b1 (pk)
	b2
	a1 (fk)

	C : DEPT

	c1 (pk)
	c2
	b1 (fk)

	D : EMP

	d1 (pk)
	d2
	c1 (fk)


    [1] 식별자 관계 : C, D 조인
  
    select e.*
    from dept d, emp e
    where d.deptid = e.deptno
    and d.country_id = e.country_id
    and d.region_id = e.region_id
    and d.name = 'SALES';

    [2] 식별자 관계 : A, D 조인

    select e.*
    from region r, emp e
    where r.region_id = e.region_id
    and r.name = 'ASIA';

    [3] 비식별자 관계 : C, D 조인
 
    select e.*
    from dept d, emp e
    where and d.deptid = e.deptno
    and d.name = 'SALES';

    [4] 비식별자 관계 : A, D 조인

    select e.*
    from region r, country c, dept d, emp e
    where r.region_id = c.region_id
    and c.country_id = d.country_id
    and d.deptid = e.deptno
    and r.name = 'ASIA';



  ### 4-7

    drop table orders purge;
    drop table customers purge;

    create table customers
    (family_name varchar2(10),
     initials    varchar2(10),
     address     varchar2(30),
     telephone   varchar2(11),
       constraint customers_pk primary key(family_name, address));

    create table orders
    (order_date  date,
     family_name varchar2(10),
     address     varchar2(30),
       constraint orders_pk primary key(order_date, family_name, address),
       constraint orders_fk foreign key(family_name, address) references customers(family_name, address));

    >> 복합PK 컬럼 순서는 주의해서 결정해야 합니다.

       ~ 오라클의 Index는 Rowid를 전문적으로 보관하는 객체(물론 Key 컬럼의 값도 보관함)
       ~ 복합 인덱스 설계시 컬럼 순서를 결정하는 방법 
 
            항상 사용되는 컬럼

                   ↓ 
 
            항상 =로 사용되는 컬럼

                   ↓ 
  
            유일값이 많은 컬럼

                   ↓ 
  
            기타 여러 기준

            <예제>

            where a = 
            and   b = 
            and   c =

            where a = 
            and   c =

            where b like 
            and   c =

            where c =

            도출된 인덱스 : c + a + b

### 4-8

    drop table rooms purge;
    drop table floors purge;
    drop table hotels purge;

    create table hotels
    (name varchar2(10),
       primary key(name));

    create table floors
    (no         number(2),
     hotel_name varchar2(10),
       primary key(no, hotel_name),
       foreign key(hotel_name) references hotels(name));

    create table rooms
    (no         number(2),
     floor_no   number(2),
     hotel_name varchar2(10),
       primary key(no, floor_no, hotel_name),
       foreign key(floor_no, hotel_name) references floors(no, hotel_name));

 #### Oracle 8i Nosegment Index vs Oracle 11g Invisible Index

    http://ukja.tistory.com/90
 


 ### Advanced Modeling
----------------------

    - Normalize the Data Model

	~ Normailize the Data Model : normalize / 표준화하다 / 표준적으로 하다
	
	  -> 정규화 또는 정상화(normalization)는 어떤 대상을 일정한 규칙이나 기준에 따르는 '정규적인' 상태로 
             바꾸거나, 비정상적인 대상을 정상적으로 되돌리는 과정을 뜻한다. 
	  -> 데이터를 일정한 규칙에 따라 변형하여 이용하기 쉽게 만드는 일. 
  
	~ History of Normalization 
	
	  Normalization is a technique established by the originator of the relational model, E.F. Codd. The complete 
	  set of normalization techniques, include "twelve rules" that databases need to follow in order to be described
	  as truly normalized. 

	  It is a technique that was created in support of relational theory, years before entity relationship modeling
	  was developed. The entity relationship modeling process has incorporated many of the normalization techniques
	  to produce a normalized entity relationship diagram.

	  Two terms that have their origins in the normalization technique are still widely in use. One is normalized data,
	  the other is denormalization.

          출처 : RDM9i 교재


#### 정규화 방법

    정규화되지 않은 상태

       ↓ 제1정규화(1 Normalization) : repeating group 제거

    제1정규형(1 Normal Form) : repeating group이 제거된 상태

       ↓ 제2정규화(2 Normalization) : 복합UID에 대한 부분 종속 제거(두개 이상 pk로 종속되는(복합 UID) 컬럼과 아닌 컬럼 쪼개기)

    제2정규형(2 Normal Form) : 제2정규화가 된 상태

       ↓ 제3정규화(3 Normalization) : Non-UID에 대한 종속 제거 ( UID가 아닌 것들끼리 종속관계가 있는지 확인 )

    제3정규형(3 Normal Form)

  - Resolve M:M Relationships

  - Model Subtypes

  - Model Exclusive Relationships

  - Model Hierachical Data

  - Model Recursive Relationships

  - Model Role Relationships

  - Model Data over Time  >> cf.Flashback Data Archive + Flashback Query

  - Model Complex relationships



### Model Hierachical Data
---------------------------

    5  select
    1  from
    4  where
    2  start with
    3  connect by

    col emp_no format a20
    col empno noprint

    select /* Top-Down */
      level, lpad(empno, 4*level, ' ') as emp_no,  e.*
    from emp e
    start with empno = 7839
    connect by PRIOR empno = mgr;

    select /* Top-Down */
      level, lpad(empno, 4*level, ' ') as emp_no,  e.*
    from emp e
    where empno <> 7698            -- Node 자르기
    start with empno = 7839
    connect by PRIOR empno = mgr;

    select /* Top-Down */
      level, lpad(empno, 4*level, ' ') as emp_no,  e.*
    from emp e
    start with empno = 7839
    connect by PRIOR empno = mgr and empno <> 7698   -- Branch 자르기
    ;

    select level, lpad(empno, 4*level, ' ') as emp_no,  e.*
    from emp e
    where level in (1, 2)
    start with empno = 7839
    connect by PRIOR empno = mgr;

    select level, lpad(empno, 4*level, ' ') as emp_no,  e.*
    from emp e
    start with empno = 7839
    connect by PRIOR empno = mgr
    order SIBLINGS by sal desc;

    col path format a40

    select level, lpad(empno, 4*level, ' ') as emp_no,  ename, sys_connect_by_path(ename, '/') as path
    from emp e
    start with empno = 7839
    connect by PRIOR empno = mgr;

     ---

    select /* Bottom-Up */
      level, lpad(empno, 4*level, ' ') as emp_no,  e.*
    from emp e
    start with empno = 7369
    connect by empno = PRIOR mgr;



### Data Model 검토
----------------------

  - [데이터베이스 설계와 구축] 5장, 6장에서...

  - 상관 모델링

  - 다양한 질문



### Database Design : Relational Design
----------------------------------------

    - Eyes Are Usually Red After Swimming(Studying)!

    - Initial database design
  
      1.Simple Entity     -> Table

      2.Attribtue         -> Column, Not null 설정, Sample data 입력

      3.UID(Relationship) -> Primary key

      4.Relationship      -> Foreign key -> 1 : M    -> Many측에 컬럼 추가 
                                         -> 1 : 1    -> Mandatory 1(+ unique 제약) or Wished 1(+ unique 제약)
                                         -> 61페이지 -> PERS_ID 컬럼 및 SPOUSE_ID 컬럼에 각각 unique 제약이 추가된다.

      5.Arc               -> Explicit Arc Design
                          -> Generic Arc Design 

      6.Subtype           -> Single Table Design     -> View로 단점 극복 가능
                          -> Separate Tables Design  -> View로 단점 극복 가능
                          -> Arc Implementation 

    - Table Normalization

    - Complete database design
  
      1.Referential integrity : on delete cacade, on delete set null
      2.Index
      3.View
      4.Denormalization
      5.Physical storage usage



### Denormalization
----------------------

    Storing Derivable Values

    Pre-Joining Tables

    Hard-Coded Values

    Keeping Details with Master

    Repeating Current Detail with Master

    Short-Circuit Keys
  
    End Date Column

    Current Indicator Column
  
    Hierarchy Level Indicator

  ...



### Performance를 고려한 Database Design 수정 
--------------------------------------------

  - [데이터베이스 설계와 구축] 8장에서...
  - 정규화를 통한 성능 향상
  - 반정규화를 통한 성능 향상
  - PK 순서 조정을 통한 성능 향상
  - FK 인덱스 생성을 통한 성능 향상
  - 이력모델의 구분과 기능성 컬럼을 통한 성능 향상
  - 슈퍼타입/서브타입 구분을 통한 성능 향상
  - 효율적인 채번 방법 사용을 통한 성능 향상
  - 컬럼 수가 많은 테이블의 1:1 분리를 통한 성능 향상
  - 대용량 테이블의 파티셔닝 적용을 통한 성능 향상
  - CHAR 형식에서 개발 오류 제거를 통한 성능 향상
  - 복잡한 데이터 모델 단순화를 통한 성능 향상
  - 일관성있는 데이터타입과 길이를 통한 성능 향상
  - 분산 환경 구성을 통한 성능 향상



### Table과 Segment의 관계
--------------------------------------------

                        table   segment

    - Heap-organized      1       1  
    - Partitioned         1       N  -> http://me2.do/FwuEFNqU, http://me2.do/GcUzbjjr
    - Clustered           N       1  -> http://me2.do/5MfRssu5, http://me2.do/5oCnOOHZ, http://me2.do/5oCnQdjn(실습)        
    - Index-organized     1       2  -> http://me2.do/5ROboyz1, http://me2.do/xlJAs890(실습)
 
    - MView -> http://me2.do/GkFy9CQD
 
    >> CLUSTER 예제

     set autot off

     drop cluster bank_cluster including tables cascade constraints;

     create cluster bank_cluster
     (bank_number varchar2(30))
     size 1k
     tablespace users;

     create index bank_cluster_idx
     on cluster bank_cluster;   

     create table bank
     (bank_number varchar2(30),
      bank_name   varchar2(30))
     cluster bank_cluster(bank_number);

     create index bank_pk_idx 
     on bank(bank_number);

     alter table bank
     add constraint bank_pk primary key(bank_number);

     create table account
     (account_number varchar2(30),
      bank_number    varchar2(30),
      account_owner varchar2(30))
     cluster bank_cluster(bank_number);

     create index account_pk_idx
     on account(account_number, bank_number);

     alter table account
     add constraint account_pk primary key(account_number, bank_number);

     set autot on

     select /*+ rule */ * 
     from account a, bank b
     where a.bank_number = b.bank_number;

     -----------------------------------------
     | Id  | Operation             | Name    |
     -----------------------------------------
     |   0 | SELECT STATEMENT      |         |
     |   1 |  NESTED LOOPS         |         |
     |   2 |   TABLE ACCESS FULL   | BANK    |
     |   3 |   TABLE ACCESS CLUSTER| ACCOUNT |
     -----------------------------------------

    >> IOT 예제

     create table iot
     (c1 number,
      c2 number,
      c3 number,  
        primary key(c1, c2))
      organization index;
   
     set autot on

     select * from iot
     where c1 > 0;

     create index iot_c3_idx 
     on iot(c3);

     select c3 from iot
     where c3 > 0;

     select * from iot
     where c3 > 0;

     --> http://www.orafaq.com/wiki/Index-organized_table


### With Check Option
--------------------------------------------

#### View?

- Named Select!
- View에 대한 질의는 Base Table에 대한 질의로 transformation 됩니다. (예외 많음)
  
  
      drop table t1 purge;
  
       create table t1 
      as
      select empno, 
           ename, 
           case when rownum < 10  then sal           end as month_sal,
           case when rownum >= 10 then trunc(sal/4)  end as week_sal, 
           case when rownum < 10  then 'R' else 'IR' end as gubun,
           deptno 
      from emp;

      create or replace view sawon_r
      as
      select empno, ename, month_sal, gubun, deptno from t1
      where gubun = 'R';

      create or replace view sawon_ir
      as
      select empno, ename, week_sal, gubun, deptno from t1
      where gubun = 'IR';

      select * from sawon_r;
      select * from sawon_ir;

      insert into sawon_r values (9999, 'JAMES', 400, 'IR', 20);

      select * from t1;  --> 9999 사원은 IR인데 month_sal에 value가 입력되어 문제이다.
  
      delete from t1 where empno = 9999;

        ↓↓

      create or replace view sawon_r
      as
      select empno, ename, month_sal, gubun, deptno from t1
      where gubun = 'R'
      with check option constraint sawon_r_gubun_ck;

      create or replace view sawon_ir
      as
      select empno, ename, week_sal, gubun, deptno from t1
      where gubun = 'IR'
      with check option constraint sawon_ir_gubun_ck;
  
      insert into sawon_r  values (9999, 'JAMES', 400, 'IR', 20);    --> 에러 : ORA-01402: view WITH CHECK OPTION where-clause violation
      insert into sawon_ir values (9999, 'JAMES', 400, 'IR', 20);    --> 성공

      select * from t1;  --> 9999 사원이 제대로 입력되었음을 확인할 수 있다.

      select constraint_name, table_name, constraint_type
      from user_constraints
      where table_name like 'SAWON%'
      or    table_name like 'TV%'   
      or    table_name like 'EMPL%'   ;




#### 참고 자료
--------------------------------------------

Partitioned Outer Join : http://me2.do/5Fc6guTF 

    select ...
    from days d LEFT OUTER JOIN sales s PARTITION BY (prod_id) ON (조인조건)
  
Between 이해

    drop table t1 purge;

    create table t1 
    (name varchar2(10),
     price number,
     start_date varchar2(8),
     end_date varchar2(8));

    insert into t1 values ('ABC', 1000, '19980101', '20020331');
    insert into t1 values ('ABC', 2000, '20020401', '20091210');
    insert into t1 values ('ABC', 3000, '20091211', '');
    insert into t1 values ('MOP', 2000, '20120101', '20131231');
    insert into t1 values ('MOP', 2500, '20140101', '');
  
    select * from t1;

    select * from t1
    where '20120630' between start_date and nvl(end_date, '99991231');


##### Flashback Data Archive + Flashback Query


##### 객체이름 정하기

  http://orapybubu.blog.me/40045704831
  http://me2.do/xV90URJ3 : Oracle SQL Reserved Words

  create table "2015 sales" (no number);

  drop table tab1 purge;

  create table tab1 (no number);
  create view  tab1 as select no from tab1;  -- 에러
  create index tab1 on tab1(no);
  alter table tab1 add constraint tab1 primary key(no);

  create table substr (substr varchar2(30));
  select substr, substr(substr, 1, 2)
  from substr;

##### MView 

  http://docs.oracle.com/cd/E11882_01/server.112/e25554/toc.htm

##### 물리모델링시 Width가 없는 Number형을 쓰지 말아야 할 이유 
  
  http://gseducation.blog.me/20095938837





