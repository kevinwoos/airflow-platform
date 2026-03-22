CREATE TABLE IF NOT EXISTS emp (
    empno       INTEGER PRIMARY KEY,
    ename       VARCHAR(100) NOT NULL,
    deptno      INTEGER NOT NULL,
    job         VARCHAR(100),
    sal         NUMERIC(12,2),
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);