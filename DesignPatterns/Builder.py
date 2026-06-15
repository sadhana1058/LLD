class Email:
    def __init__(self, builder):
        self.to = builder._to
        self.subject = builder._subject
        self.cc = list(builder._cc)
        self.bcc = list(builder._bcc)
        self.body = builder._body
        self.priority = builder._priority
        self.attachments = list(builder._attachments)

    def __str__(self):
        # TODO: Return formatted string showing all fields
        # Expected format:
        cc = ', '.join(self.cc)
        bcc = ', '.join(self.bcc)
        a = ', '.join(self.attachments)
        return (
                f"Email{{to='{self.to}', "
                f"subject='{self.subject}', "
                f"cc=[{cc}], "
                f"bcc=[{bcc}], "
                f"body='{self.body}', "
                f"priority='{self.priority}', "
                f"attachments=[{a}]}}"
        )

    class Builder:
        def __init__(self, to, subject):
            self._to = to
            self._subject = subject
            self._cc = []
            self._bcc = []
            self._body = None
            self._priority = "normal"
            self._attachments = []

        def cc(self, cc):
            # TODO: Append cc to the _cc list
            self._cc.append(cc)
            return self

        def bcc(self, bcc):
            # TODO: Append bcc to the _bcc list
            self._bcc.append(bcc)
            return self

        def body(self, body):
            # TODO: Set the _body field
            self._body = body
            return self

        def priority(self, priority):
            # TODO: Set the _priority field
            self._priority = priority
            return self

        def attachment(self, attachment):
            # TODO: Append attachment to the _attachments list
            self._attachments.append(attachment)
            return self

        def build(self):
            return Email(self)

if __name__ == "__main__":
    email1 = Email.Builder("alice@example.com", "Meeting Tomorrow") \
        .body("Let's meet at 10am in conference room B.") \
        .build()

    email2 = Email.Builder("bob@example.com", "Project Update") \
        .cc("carol@example.com") \
        .cc("dave@example.com") \
        .bcc("manager@example.com") \
        .body("Attached is the Q4 report.") \
        .priority("high") \
        .attachment("q4-report.pdf") \
        .attachment("summary.xlsx") \
        .build()

    print(email1)
    print()
    print(email2)