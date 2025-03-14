-- ranks the country of origins for different bands
SELECT origin, SUM(fans) AS nb_fans
       FROM metal_bands
       GROUP BY origin
       ORDER BY nb_fans DESC;