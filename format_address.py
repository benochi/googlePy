def format_address(address_string):
  # Declare variables
  number =""
  address =""
  # Separate the address string into parts
  add = address_string.split()
  # Traverse through the address parts
  for element in add:
    # Determine if the address part is the
    # house number or part of the street name
    if element.isdigit():
      number = element
    else:
      address += element
      address += ' '
  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(number, address)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
