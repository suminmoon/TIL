 ## <3장> PL/SQL Statement in Blocks

### Lexical unit(어휘 단위)

  A line of PL/SQL text contains groups of characters
  known as lexical units:

  - 구분자(Delimiter)  : simple and compound symbols
  - 식별자(Identifier) : which include reserved words
  - 리터럴(Literal)
  - 주석(Comment)

#### 3-16
 
  - Scope(범위)
  - Visibility(가시성)

#### 3-18

  - qualifier(수식자)

#### 3-19

    create or replace package p
    is
    procedure p(a number);
    procedure p(a date);
    procedure p(a varchar2);
    end;
    /

    create or replace package body p
    is
      procedure p(a number)
      is
      begin
        dbms_output.put_line(a);
      end;

      procedure p(a date)
      is
      begin
        dbms_output.put_line(a);
      end;

      procedure p(a varchar2)
      is
      begin
        dbms_output.put_line(a);
      end;
    end;
    /  

    exec p.p(100)
    exec p.p('100')
    exec p.p(sysdate)

   ---

    <<outer>>
    DECLARE
      v_sal     NUMBER(7,2) := 60000;
      v_comm    NUMBER(7,2) := v_sal * 0.20;
      v_message VARCHAR2(255) := ' eligible for commission';
    BEGIN 

      DECLARE
        v_sal        NUMBER(7,2) := 50000;
        v_comm       NUMBER(7,2) := 0;
        v_total_comp NUMBER(7,2) := v_sal + v_comm;
      BEGIN 
        v_message := 'CLERK not'||v_message;

        p.p(v_message);         -- 1 CLERK not eligible for commission
        p.p(v_comm);            -- 2 0
        p.p(outer.v_comm);      -- 3 12000

        outer.v_comm := v_sal * 0.30; 
      END;

      v_message := 'SALESMAN, '||v_message;

      -- p.p(v_total_comp);     -- 4 에러
      p.p(v_comm);              -- 5 15000 
      p.p(v_message);           -- 6 SALESMAN, CLERK not eligible for commission
 
    END;
    /


## <4장> SQL Statement in Blocks

#### 4-4 

    BEGIN
      - DDL : CREATE, ALTER, DROP, RENAME, TRUNCATE, COMMENT   : 사용 불가
      - DML : INSERT, UPDATE, DELETE, MERGE, SELECT            : 사용 가능
      - TCL : COMMIT, ROLLBACK, SAVEPOINT                      : 사용 가능
      - DCL : GRANT, REVOKE                                    : 사용 불가
    END;

  => 이유 : https://docs.oracle.com/cd/A57673_01/DOC/server/doc/PLS23/ch5.htm#toc043


