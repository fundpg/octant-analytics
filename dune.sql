WITH ExtractedDataB AS (

WITH ExtractedDataA AS (

SELECT

    DATE_TRUNC('day', block_time) AS transaction_day,
    SUBSTR(CAST(data AS VARCHAR), 3, 8) AS method,
    SUBSTR(CAST(data AS VARCHAR), 11) AS hex_value,
    bytearray_to_uint256(bytearray_substring(data, 11, 64))/POWER(10,18) AS decimal_value
    
FROM ethereum.transactions 

WHERE to = 0x879133Fd79b7F48CE1c368b0fCA9ea168eaF117C
AND "from" = {{user_address}}
AND block_time >= DATE_TRUNC('day', CURRENT_TIMESTAMP) - INTERVAL '7' day

)

SELECT 
    transaction_day,
    method,
    sum(decimal_value) as total_value

FROM ExtractedDataA
GROUP BY 
    transaction_day, method
ORDER BY
    transaction_day, method

)

SELECT 
    method,
    SUM(
        CASE 
            WHEN method = '6198e339' THEN total_value * (-1)
            ELSE total_value
        END
    ) as adjusted_value

FROM ExtractedDataB
GROUP BY 
    method
ORDER BY
    method