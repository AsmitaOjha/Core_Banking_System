CREATE TABLE IF NOT EXISTS transactions (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    sender_account_id BIGINT NOT NULL,
    receiver_account_id BIGINT,
    amount BIGINT NOT NULL,
    transaction_type ENUM('deposit', 'withdraw', 'transfer') NOT NULL,
    date_time TIMESTAMP NOT NULL,
    remark VARCHAR(255) NOT NULL,
    status ENUM('Completed', 'Failed', 'Pending'),
    FOREIGN KEY (sender_account_id) REFERENCES accounts(account_number) ON DELETE CASCADE,
    FOREIGN KEY (receiver_account_id) REFERENCES accounts(account_number) ON DELETE CASCADE
);