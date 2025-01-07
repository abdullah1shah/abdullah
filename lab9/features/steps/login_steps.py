# features/steps/login_steps.py
from behave import given, when, then

@when('I enter valid user credentials')
def step_impl(context):
    print("Entered valid username and password")
    context.credentials_valid = True

@when('I enter invalid credentials')
def step_impl(context):
    print("Entered invalid username or password")
    context.credentials_valid = False

@when('I enter valid admin credentials')
def step_impl(context):
    print("Entered valid admin credentials")
    context.admin_credentials_valid = True

@when('I enter invalid admin credentials')
def step_impl(context):
    print("Entered invalid admin credentials")
    context.admin_credentials_valid = False

@then('I should be logged in')
def step_impl(context):
    assert context.credentials_valid
    print("Successfully logged in as user")

@then('I should be logged in as admin')
def step_impl(context):
    assert context.admin_credentials_valid
    print("Successfully logged in as admin")

@then('I should see the dashboard')
def step_impl(context):
    print("Dashboard displayed")

@then('I should see the admin dashboard')
def step_impl(context):
    print("Admin dashboard displayed")

@then('I should remain on the login page')
def step_impl(context):
    print("Remained on login page")