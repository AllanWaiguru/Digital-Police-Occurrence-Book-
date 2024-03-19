CREATE TABLE suspects (
    suspect_id SERIAL PRIMARY KEY,
    -- suspect details
);

CREATE TABLE fingerprints (
    fingerprint_id SERIAL PRIMARY KEY,
    suspect_id INT REFERENCES suspects(suspect_id),
    fingerprint_data BYTEA -- Binary data or reference
);

CREATE TABLE crimes (
    crime_id SERIAL PRIMARY KEY,
    -- crime details
);

CREATE TABLE cells (
    cell_id SERIAL PRIMARY KEY,
    crime_id INT REFERENCES crimes(crime_id),
    number_of_criminals INT
);

CREATE TABLE registered_crimes (
    registered_crime_id SERIAL PRIMARY KEY,
    crime_id INT REFERENCES crimes(crime_id)
);

CREATE TABLE pending_crimes (
    pending_crime_id SERIAL PRIMARY KEY,
    crime_id INT REFERENCES crimes(crime_id)
);

CREATE TABLE reporters (
    reporter_id SERIAL PRIMARY KEY,
    -- reporter details
);

CREATE TABLE witnesses (
    witness_id SERIAL PRIMARY KEY,
    -- witness details
);

CREATE TABLE reporter_lawyers (
    reporter_lawyer_id SERIAL PRIMARY KEY,
    reporter_id INT REFERENCES reporters(reporter_id),
    -- lawyer details
);

CREATE TABLE exhibits (
    exhibit_id SERIAL PRIMARY KEY,
    crime_id INT REFERENCES crimes(crime_id),
    -- exhibit details
);

CREATE TABLE penalties (
    penalty_id SERIAL PRIMARY KEY,
    crime_id INT REFERENCES crimes(crime_id),
    -- penalty details
);

CREATE TABLE bails (
    bail_id SERIAL PRIMARY KEY,
    suspect_id INT REFERENCES suspects(suspect_id),
    amount NUMERIC(10, 2)
);

CREATE TABLE officers (
    officer_id SERIAL PRIMARY KEY,
    -- officer details
);

CREATE TABLE courts (
    court_id SERIAL PRIMARY KEY,
    -- court details
);

CREATE TABLE judges (
    judge_id SERIAL PRIMARY KEY,
    -- judge details
);

CREATE TABLE police_stations (
    station_id SERIAL PRIMARY KEY,
    -- station details
);

CREATE TABLE armories (
    armory_id SERIAL PRIMARY KEY,
    station_id INT REFERENCES police_stations(station_id),
    -- armory details
);

CREATE TABLE incidents (
    incident_id SERIAL PRIMARY KEY,
    -- incident details
);
