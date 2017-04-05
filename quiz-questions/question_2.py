import unittest


def number_of_customers_per_state(customers):
    """Return the number of customers per state.

    This function receives a dictionary containing states (as keys) and
    customers for those states (as a list of dictionaries) and should
    return a final dictionary containing the count of customers per state.

    customers = {
        'UT': [{
            'name': 'Mary',
            'age': 28
        }, {
            'name': 'John',  # Eldest
            'age': 31
        }],
        'NY': [{
            'name': 'Linda',  # Eldest
            'age': 71
        }]
    }
    number_of_customers_per_state(customers)
    >>>
    {
        'UT': 2,
        'NY': 1
    }
    """
    dictionary_list = {}
    
    customerList_1 = customers['UT']
    customerCount_1 = 0
    for customer in customerList_1:
        customerCount_1 += 1
            dictionary_list['UT'] = customerCount_1
            
    customerList_2 = customers['NY']
    customerCount_2 = 0
    for customer in customerList_2:
        customerCount_2 += 1
            dictionary_list['NY'] = customerCount_2
            
    customerList_3 = customers['CA']
    customerCount_3= 0
    for customer in customerList_3:
        customerCount_3 += 1
            dictionary_list['CA'] = customerCount_3
                
    return dictionary_list

class NumberOfCustomersPerStateTestCase(unittest.TestCase):
    def test_number_of_customers_per_state(self):
        """Should return the correct number of customers per state."""
        customers = {
            'UT': [{
                'name': 'Mary',
                'age': 28
            }, {
                'name': 'John',
                'age': 31
            }, {
                'name': 'Robert',
                'age': 16
            }],
            'NY': [{
                'name': 'Linda',
                'age': 71
            }],
            'CA': [{
                'name': 'Barbara',
                'age': 15
            }, {
                'name': 'Paul',
                'age': 18
            }]
        }
        expected_result = {
            'UT': 3,
            'NY': 1,
            'CA': 2
        }
        self.assertEqual(
            number_of_customers_per_state(customers), expected_result)

    def test_number_of_customers_per_state_with_blank_state(self):
        """Should return the correct number of customers per state."""
        customers = {
            'UT': [{
                'name': 'Mary',
                'age': 28
            }, {
                'name': 'John',
                'age': 31
            }, {
                'name': 'Robert',
                'age': 16
            }],
            'NY': None,  # Be Careful! NY value is None
            'CA': [{
                'name': 'Barbara',
                'age': 15
            }, {
                'name': 'Paul',
                'age': 18
            }]
        }
        expected_result = {
            'UT': 3,
            'NY': 0,
            'CA': 2
        }
        self.assertEqual(
            number_of_customers_per_state(customers), expected_result)


if __name__ == '__main__':
    unittest.main()
