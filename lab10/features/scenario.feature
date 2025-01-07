Feature: Extended Scenario outline

Scenario Outline: Test multiple categories
  Given I have "<thing>" and "<detail>"
  When I process them
  Then the result should be "<outcome>"

Examples: User Id - Password
  | thing     | detail      | outcome        |
  | user1     | password1   | success        |
  | user2     | password2   | success        |
  | user3     | password3   | failure        |
  | user4     | password4   | success        |
  | user5     | password5   | failure        |

Examples: Product Name - Price
  | thing      | detail  | outcome    |
  | Laptop     | $1000   | in stock   |
  | Phone      | $700    | out of stock |
  | Headphones | $150    | in stock   |
  | Charger    | $30     | in stock   |
  | Mouse      | $50     | out of stock |

Examples: Course - Pre-Requisite
  | thing           | detail          | outcome      |
  | Mathematics I   | None            | available    |
  | Programming I   | None            | available    |
  | Data Structures | Programming I   | available    |
  | Algorithms      | Data Structures | available    |
  | AI              | Mathematics I   | available    |
