INSERT INTO emp (empno, ename, deptno, job, sal)
VALUES
    (1001, 'KIM', 10, 'MANAGER', 5000),
    (1002, 'LEE', 20, 'ANALYST', 4200),
    (1003, 'PARK', 30, 'CLERK', 2800)
ON CONFLICT (empno) DO NOTHING;