ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_card_number
FOREIGN KEY (card_number)
REFERENCES dim_cards(card_number)
ON DELETE NO ACTION;
