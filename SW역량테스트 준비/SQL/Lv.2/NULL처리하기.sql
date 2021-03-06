SELECT ANIMAL_TYPE, IFNULL(NAME,'No name') AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
SELECT ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE like '%Neutered%' or SEX_UPON_INTAKE like '%Spayed%',"O","X") as "중성화"
FROM ANIMAL_INS
#IFNULL NULL인지 아닌지 판단하는 값으로 NULL이 아니면 A값으로, 맞으면 B값으로 반환한다.