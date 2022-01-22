SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL

#중복을 제거해주는 DISTINCT를 사용, null인지 확인하는거는 != null이 아닌 is not NULL을 사용해야
하며, 동등연산자는 ==이 아닌 =을 사용한다는 특징이 있다.