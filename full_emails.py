def full_emails(people):
  result = []
  for email, name in people:
    result.append("{} <{}>".format(name, email))
  
  return result

print(full_emails([( "Bob@bob.com","Bob"), ( "Bob2@bob.com","Bob2")
]))
