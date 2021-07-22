person = { "first_name": "Robin", "last_name": "Ochoa", "birth_year": 1979, "country_of_birth": "Canada" }

print ( "Original person dictionary: " , person )

print ( type(person) )

print ( person["first_name"] )

person["marital_status"] = "Married"

print ( "Added property marital_status, to Person dictionary: " , person )

person["children"] = ["Luciano","Charlotte"]

print ( "Added property children, to Person dictionary: " , person )

person["children"].append("Isabella")

print ( "Added another children to list, to Person dictionary: " , person )

print ( person.get("age","invalid property") )

print ( person.get("children","invalid property") )

key = "first_name"

print ( person.get(key,"invalid property") )

person.clear()

print ( "Cleared dictionary", person )
