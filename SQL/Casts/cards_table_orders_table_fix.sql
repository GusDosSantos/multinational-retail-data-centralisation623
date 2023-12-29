UPDATE orders_table
SET card_number = NULL
WHERE card_number IS NOT NULL
  AND card_number NOT IN (SELECT card_number FROM dim_cards);
