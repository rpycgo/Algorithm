class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            name, domain = email.split('@')

            name = name.split('+')[0].replace('.', '')
            email = f'{name}@{domain}'

            unique_emails.add(email)

        return len(unique_emails)
