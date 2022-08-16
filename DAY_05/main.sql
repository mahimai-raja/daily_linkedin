# Author : Mahimai Raja J
# Linkedin : https://www.linkedin.com/in/mahimai-raja-j/

SELECT DISTINCT(CITY)
FROM STATION
WHERE CITY REGEXP '^[aeiou]';          
	
''' Output : 
    All element with starting alphabet
    as vowel. '''