facts_table_check = '''SELECT COUNT(*) FROM facts_table'''

destination_table_check = '''SELECT COUNT(*) FROM destination_table'''

geography_table_check = '''SELECT COUNT(*) FROM geography_table'''

date_table_check = '''SELECT COUNT(*) FROM date_table'''

immigration_table_check = '''SELECT COUNT(*) FROM immigration_table'''

quality_check_queries = [facts_table_check, destination_table_check, geography_table_check, date_table_check, immigration_table_check]
