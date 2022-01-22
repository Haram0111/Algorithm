SELECT ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE like '%Neutered%' or SEX_UPON_INTAKE like '%Spayed%',"O","X") as "중성화"
FROM ANIMAL_INS

#if문안에 where을 써서 좀 오래걸렸음 like만쓰면 참 거짓 가능