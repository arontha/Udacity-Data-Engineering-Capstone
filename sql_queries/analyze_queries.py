#/*Top 10 Immigration Origin Report*/
imm_dest_report = '''SELECT COUNT(imm_id) as Num_People, dest_id as State
FROM facts_table
GROUP BY State
ORDER BY Num_People DESC
LIMIT 10;'''

imm_origin_report = '''SELECT COUNT(imm_id) as Num_People, origin_id as Country
FROM facts_table
GROUP BY Country
ORDER BY Num_People DESC
LIMIT 10;'''

#/*Origin of immigration to New York*/
imm_newyork_report = '''SELECT COUNT(imm_id) as Num_People, origin_id as Country
FROM facts_table
WHERE dest_id = 'NY'
GROUP BY Country
ORDER BY Num_People DESC
LIMIT 10;'''

#/*Immigration to States with High Latino Population*/
imm_origin_report = '''SELECT COUNT(imm_id) as Num_People, origin_id as Country, DT.dest_id as State
FROM facts_table FT JOIN Destination_Table DT ON FT.dest_id = DT.dest_id
WHERE DT.latino > 20
GROUP BY Country, DT.dest_id
ORDER BY Num_People DESC
LIMIT 10;'''

#/*Immigration by Gender Report*/
imm_gender_report = '''SELECT COUNT(imm_id) as Num_People, country_of_origin, gender
FROM immigration_table
GROUP BY gender, country_of_origin
ORDER BY Num_People DESC
LIMIT 10;'''

#/*Immigration by Age Report*/



#/*Immigration by Climate Change Report - amount of immigration vs. amount of temperature change in country of origin*/



#/*Immigration by Month Report*/



#/*Top Immigration destination by visatype*/



#/*Warm weather vacationing report - amount of immigration from colder countries to warmer states*/



#/*Seasonality of Immigration Report - visatype by month*/


analyze_queries = [imm_dest_report, imm_origin_report, imm_newyork_report, imm_gender_report, imm_origin_report]
