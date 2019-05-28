## <10장> Table

    - 과정 : 현실세계 -> 데이터 모델링                -> 데이터베이스 구현
                       - 선별, 정리                    - Create Database ~
                       - Logicle Modeling               Create USer ~
                         Relational Modeling            Create Table ~     
                         Physical Modeling              ...
    
    - Data Integrity 유지를 끊임없이 고민해야 함
      -> 데이터 무결성의 유일한 판단 기준은 비즈니스 룰임
      -> 테이블 생성시 무결성 제약  설정
      -> PL/SQL을 이용해서 트리거 생성
      -> Application Code
      
___________________________________________
      
### Table Instance Chart
      
      T_EMP                                                    T_DEPT
      
      empno  ename    sal    hp ...   deptno                   deptno dname    loc
      number varchar2 number varchar2 number                   number varchar2 varchar2
      
    
      drop table t_dept purge;
      drop table t_emp purge;
    
      create table t_dept
      (deptno number (2) , 
       dname varchar2(10), 
       loc      varchar2(10));
    
      create table t_emp
      (empno number (4), 
       ename varchar2(10), 
       sal     number(10, 2),
       hp     varchar2(11),
       deptno number(2));
       
       
       
       

    
       
  
--------------------------  
    
### Table Instance Chart 수정
    
                  T_EMP                                             T_DEPT
      
      empno  ename     sal      hp ...     deptno               deptno dname    loc
      number varchar2  number   varchar2   number               number varchar2 varchar2
      중복x    중복o    중복0    중복x                            중복x   중복o
      널x       널x     널O     널x                               널x     널x
                       0이상
                                          정해진 값




    drop table t_dept purge;
    drop table t_emp purge;
    
    create table t_dept
    (deptno number (2) primary key,     --식별자 (primary key) 
     dname varchar2(10) not null, 
     loc      varchar2(10));
    
    create table t_emp
    (empno number (4) primary key, 
     ename varchar2(10) not null, 
     sal     number(10, 2) check (sal >=0),
     hp     varchar2(11) unique not null,
     deptno number(2)   references t_dept(deptno));   --참조무결성 ( 여기 deptno는 t_dept의 deptno 값을 보고 판단해라 )
     


#### 컬럼 레벨 제약조건 설정 문법 (무결성 제약조건 이름 붙이기 )
    
    drop table t_dept purge;
    drop table t_emp purge;
    
    create table t_dept
    (deptno number (2) constraint t_dept_deptno_pk primary key,       
     dname varchar2(10) constraint t_dept_dname_nn not null, 
     loc   varchar2(10));
    
    create table t_emp
    (empno number (4) constraint t_emp_empno_pk primary key, 
     ename varchar2(10) constraint t_emp_ename_nn not null, 
     sal     number(10, 2) constraint t_emp_sal_ck check (sal >=0),
     hp     varchar2(11) constraint t_emp_hp_uk unique 
                         constraint t_emp_hp_nn not null,
     deptno number(2)  constraint t_emp_deptno_fk references t_dept(deptno)  ) ;
                                                          
    insert into t_dept values(10, 'SALES', 'SEOUL');
    insert into t_dept values(10, 'IT', 'SEOUL');     -- 에러
    insert into t_dept values(null, 'SALES', 'SEOUL')  --에러
    
           
       
       
       
      select * from tab
      where tname like 'T!_%' escape '!';
    
      desc t_dept;
      desc t_emp;
    
      insert into t_dept values(10, 'Marketing', 'Seoul');
      select * from t_dept;
      insert into t_dept values(10, 'IT', 'Masan');
    
      alter table t_dept add unique(deptno);   --에러(이미 중복된 값이 들어있음)
    
      update t_dept
        set deptno = 20
      where dname ='IT';    --수정(중복 안되게)
    
      select * from t_dept;
    
      alter table t_dept add unique(deptno);    --실행됨
    
      insert into t_dept values(10, 'RD', 'Suwon');   --에러(unique제약 때문에 중복 ㄴㄴ)
      insert into t_dept values(30, 'RD', 'Suwon');
    
    
      -- deptno를 사용자가 일일히 지정하지 않도록 설정하기!
      create sequence t_dept_deptno_seq
      start with 40           -- 40부터
      increment by 10       -- 10씩 증가하는
      maxvalue 1000;        -- 최대 1000
    
      insert into t_dept values (t_dept_deptno_seq.nextval, 'Account', 'GJ');
    
      select t_dept_deptno_seq.currval
      from dual;    --sequence 번호 어디까지 지정되었는지 확인하기
    
      insert into t_dept values (null, 'Sales', 'GJ');
      insert into t_dept values (null, 'Research', 'GJ');  -- unique 제약은 null 허락! null은 계속 들어감
    
    
      delete from t_dept;
      select * from t_dept;



#### 테이블 레벨 제약조건 설정 문법 
 모든 컬럼 정의 뒤에 붙이기
 
    drop table t_dept purge;
    drop table t_emp purge;
    
    create table t_dept
    (deptno number (2) , 
     dname varchar2(10), 
     loc   varchar2(10),
        constraint t_dept_deptno_pk primary key (deptno),
        constraint t_dept_dname_nn check (dname is not null));
    
    create table t_emp
    (empno number (4), 
     ename varchar2(10), 
     sal     number(10, 2),
     hp     varchar2(11),
     deptno number(2),
       constraint t_emp_empno_pk primary key(empno),
        constraint t_emp_ename_nn check (ename is not null ),
        constraint t_emp_sal_ck check(sal >=0),
        constraint t_emp_hp_uk unique(hp),
        constraint t_emp_hp_nn check (hp is not null),
        constraint t_emp_deptno_fk foreign key(deptno) references t_dept(deptno) );
    
    select * from t_dept;
    

    ### cf. 반드시 테이블 레벨 문법 제약 설정을 해야하는 경우
       : 두 개 이상의 컬럼으로 하나의 제약을 생성할 경우!

    create table t_simin
    (no number primary key,
        ju1 varchar2(6),
        ju2 varchar2(7),
            unique(ju1, ju2));



### PL/SQL을 이용해서 트리거(Trigger) 생성

    drop table t1 purge;
    
    create table t1 (no number, name varchar2(10));
    
    -> name 컬럼에 반드시 대문자 입력이라는 룰을 설정해야 함
    
    create or replace trigger t1_name_tri
    before insert or update of name on t1  -- t1 컬럼에 내용 추가할 때랑 이름을 업데이트 할 때 실행되어라!
    for each row
    begin
        :new.name := upper( :new.name );     -- ':=' : 오른쪽에 있는 걸 왼쪽에 넣어라! -> user가 소문자로 넣은 걸 대문자로 바꿔서 넣어라
    end;
    /
    
    insert into t1 values (1000, 'john');
    insert into t1 values (2000, 'alice');
    select * from t1;
    
    update t1
    set name = ~~
    where no between 1000 and 3000;
    
    


##### 테이블 관련 대표적 Meta data
    
    select table_name, NUM_ROWS, EMPTY_BLOCKS
    from user_tables;
    
    select table_name, 
            constraint_name, 
            constraint_type,
            SEARCH_CONDITION
    from user_constraints;
    
    
    select table_name, index_name
    from user_indexes
    order by 1;
    
    
    
    
    
        
## 부록 AP 연습문제(2-1) 풀어보기


    create table member
    (member_id number(10), 
    last_name varchar2(25), 
    first_name varchar2(25), 
    address varchar2(100), 
    city varchar2(30), 
    phone varchar2(15), 
    join_date date,
        constraint t_member_memberid_pk primary key(member_id),
        constraint t_member_memberid_nn check( member_id is not null),
        constraint t_member_lastname_nn check(last_name is not null),
        constraint t_member_joindate_nn check(join_date is not null)
    );
    
    
    create table title
    (title_id number(10), 
    title varchar2(60), 
    description varchar2(400), 
    rating varchar2(4),
    category varchar2(20), 
    release_date date, 
        constraint t_title_titleid_pk primary key(title_id),
        constraint t_title_titleid_nn check( title_id is not null),
        constraint t_title_title_nn check(title is not null),
        constraint t_tile_description_nn check(description is not null),
        constraint t_title_rating_ck check(rating in ('G', 'PG','R','NC17','NR')),
        constraint t_title_category_ck check(rating in ('DRAME', 'COMEDY','ACTION','CHILD','SCIEL','DOCUMENTARY'))
    );    
    
    create table title_copy
    (copy_id number(10), 
    title_id number(10) constraint title_copy_titleid_fk references title(title_id),
    status varchar2(15) constraint title_copy_status_nn not null
                            constraint title_copy_status_ck check ( status in ( 'AVAILABLE', 'DESTROYED','RENTED','RESERVED')),
                            constrint tile_copy_copyid_titleid_pk primary key(copy_id, title_id)  );
                            
                            
    
    create table rental
    (book_date date default sysdate, 
    member_id number(10) constraint rental_memberid_fk references member(member_id),
    copy_id number(10) 
    act_ret_date date,
    exp_ret_date date default sysdate+2,
    title_id number(10),
    constraint rental_bookdate_copy_title_pk primary key(book_date, member_id, copy_id, title_id),
    constraint rental_copyid_titleid_fk foreign key (copy_id, title_id) references title_copy(title_id));
    

    create table reservation
    (res_date date,
    member_id number(10) constraint reservation_member_id references member(member_id),
    title_id number(10) constraint reservation_title_id references title(title_id),
        constraint reservation_resdate_mem_tit_pk primary key (res_date, member_id, title_id));
