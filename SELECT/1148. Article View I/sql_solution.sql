/* Write your T-SQL query statement below */
SELECT
    distinct author_id as id
FROM Views
WHERE author_id = viewer_id;
