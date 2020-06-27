# A transaction is possibly invalid if:

# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
# Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

# Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.
# Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# Output: ["alice,20,800,mtv","alice,50,100,beijing"]
# Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# Output: ["bob,50,1200,mtv"]

### An O(n) solution assuming the inputs are sorted in ascending order of name and then ascending order of time for a given name ###

def check_transaction_validity(transactions):
	if not transactions:
		return None 

	invalid_transactions_list = []
	invalid_transaction_set = set()

	for idx,transaction in enumerate(transactions):
		curr_name,trans_time,trans_amount,curr_city = transaction.split(",")
		curr_time = int(trans_time)
		curr_amount = int(trans_amount)

		if curr_amount >= 1000 and transaction not in invalid_transaction_set:
			invalid_transactions_list.append(transaction)
			invalid_transaction_set.add(transaction)

		if idx != 0 :
			if curr_name == prev_name and curr_time - prev_time <= 60 and curr_city != prev_city:
				if prev_transaction not in invalid_transaction_set:
					invalid_transactions_list.append(prev_transaction)  
				invalid_transactions_list.append(transaction)

		prev_transaction = transaction
		prev_name = curr_name 
		prev_time = curr_time
		prev_amount = curr_amount
		prev_city = curr_city

	return invalid_transactions_list 

print(check_transaction_validity(["alice,20,800,mtv","alice,50,100,beijing"]))
# Output: ["alice,20,800,mtv","alice,50,100,beijing"]
print(check_transaction_validity(["alice,20,800,mtv","bob,50,1200,mtv"]))
# Output: ["bob,50,1200,mtv"]
