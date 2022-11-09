Feature: search flipkart
  Scenario Outline: search data
    Given We are on flipkart website
    When click login
    Then Enter your "<username>" in the feild
    And Enter your "<password>" in the box
    And click login
    Then type "<searchTEXT>" in search bar
    And Click on search button
    Then Click on Product
    Then Click on add to cart


    Examples:
      | username | password | searchTEXT |
      | 9538167879 | Dog@99 | realme |
      | 9538167879 | aswewd | tv     |
      | 8877996655 | Dog@99 | books  |
      | 7896535372 | gehsge | mobile |

