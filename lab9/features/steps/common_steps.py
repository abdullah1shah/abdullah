from behave import given, when, then

@given('I am on the {page} page')
def step_impl(context, page):
    print(f"Navigated to {page} page")

@when('I click the {button_name} button')
def step_impl(context, button_name):
    print(f"Clicked {button_name} button")

@then('I should see an error message')
def step_impl(context):
    print("Error message displayed")


    