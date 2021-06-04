class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        results = []
        addresses = {}
        for email in emails:
            # split by '@' first
            split_by_at = email.split('@')
            # local name will be split by '+' as well
            split_by_plus = split_by_at[0].split('+')
            # split by '.' and join without spaces
            join_local_name = ''.join(split_by_plus[0].split('.'))
            final_email = join_local_name + '@' + split_by_at[1]
            if final_email not in addresses:
                addresses[final_email] = 1
        # return a set of email addresses
        return len(addresses)
