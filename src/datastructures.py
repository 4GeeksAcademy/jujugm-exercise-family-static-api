
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

# class Jackson_family = FamilyStructure('Jackson') 


class FamilyStructure:
            def __init__(self, last_name):
                self.last_name = last_name
                self._next_id = 1
                # example list of members
                self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
            def _generateId(self):
                generated_id = self._next_id
                self._next_id += 1
                return generated_id
# Este método genera un 'id' único al agregar miembros a la lista (no debes modificar esta función)
            def add_member(self, member):
               member["last_name"] = self.last_name
               member ["id"] = self._generateId()
               member["lucky_numbers"] = list(member.get("lucky_numbers", []))
               self._members.append(member)

               return member 

            def delete_member(self, id):
                
                for member in self._members:
                    if id == member["id"]:
                        self._members.remove(member)
                        return True
                return False

            def get_member(self, id):
                for member in self._members:
                  if id == member["id"]:
                     return member

            # this method is done, it returns a list with all the family members
            def get_all_members(self):
                return self._members
