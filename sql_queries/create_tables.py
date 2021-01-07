facts_table_create = '''CREATE TABLE IF NOT EXISTS facts_table(
    imm_id int,
    date_id date,
    dest_id varchar,
    origin_id varchar,
    airport_id varchar,
    PRIMARY KEY (imm_id));'''
    
destination_table_create = '''CREATE TABLE IF NOT EXISTS destination_table(
    dest_id varchar,
    state varchar,
    median_age float,
    population float,
    white float,
    black float,
    asian float,
    latino float,
    native_american float,
    foreign_born float,
    PRIMARY KEY (dest_id));'''
    
geography_table_create = '''CREATE TABLE IF NOT EXISTS geography_table(
    airport_id varchar,
    state varchar,
    country varchar,
    city varchar,
    airport_name varchar,
    elevation int,
    continent varchar,
    avg_yrly_temp float,
    mnthly_high_temp float,
    mnthly_low_temp float,
    temp_delta_10_yrs float,
    temp_delta_20_yrs float,
    PRIMARY KEY (airport_id));'''
    
date_table_create = '''CREATE TABLE IF NOT EXISTS date_table(
    date_id date,
    day int,
    week int, 
    month int,
    year int,
    PRIMARY KEY (date_id));'''

immigration_table_create = '''CREATE TABLE IF NOT EXISTS immigration_table(
    imm_id int,
    country_of_origin varchar,
    mode_transport varchar,
    age int,
    visa_reason varchar,
    dos_issuing_office varchar,
    occupation varchar,
    arrival_flag varchar, 
    departure_flag varchar,
    update_flag varchar,
    matching_flag varchar,
    birth_year int,
    gender varchar,
    airline varchar, 
    visatype varchar,
    PRIMARY KEY (imm_id));'''

create_table_queries = [facts_table_create, destination_table_create, geography_table_create, date_table_create, immigration_table_create]
