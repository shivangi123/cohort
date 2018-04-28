query = {}
query['cohort'] = """
SELECT
  a.customerId AS customerId,
  DATE(a.orderProcessingTime) AS purchaseDate,
  ROW_NUMBER() OVER(PARTITION BY a.customerId ORDER BY a.orderProcessingTime ASC ) AS purchaseRate,
  b.cohortDate AS cohortDate,
  b.chw AS chw,
  DATEDIFF(DATE(a.orderProcessingTime), b.cohortDate)/7 AS AgeByDuration
FROM
  [{project}:{dataset}.{table}] a
LEFT JOIN (
  SELECT
    *
  FROM (
    SELECT
      customerId,
      DATE(orderProcessingTime) AS cohortDate,
      DATE(UTC_USEC_TO_WEEK(DATE(orderProcessingTime),0)) AS chw,
      ROW_NUMBER() OVER(PARTITION BY customerId ORDER BY orderProcessingTime ASC ) AS purchaseRate
    FROM
      [{project}:{dataset}.{table}])
  WHERE
    purchaseRate = 1) b
ON
  a.customerId = b.customerId
"""