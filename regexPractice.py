import re

phoneNumRegex = re.compile(r'\d{2}-\d{4}-\d{4}')
examplePhoneNum = 'My number is 02-4721-4242.'
result = phoneNumRegex.search(examplePhoneNum)
if result:
    print("Phone number found:", result.group())
    print("Area code : ", result.group()[0:2])
    print("Phone number : ", result.group()[3:7], result.group()[8:12])
else:
    print("No phone number found.")

# messageID = IHUBMDP-MSG-202502040930
messageId = re.compile(r'[A-Z]{7}-[A-Z]{3}-\d{12}')
exampleMessageId = 'Message id is IHUBMDP-MSG-202502040930'
result = messageId.search(exampleMessageId)
if result:
    print("Message ID found:", result.group())
    print("MDP : ", result.group()[0:7])
else:
    print("No message ID found.")