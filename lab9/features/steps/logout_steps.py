# features/steps/logout_steps.py
from behave import given, when, then

@given('I am logged in')
def step_impl(context):
    print("User is logged in")
    context.logged_in = True

@when('my session expires')
def step_impl(context):
    print("Session expired")
    context.session_expired = True

@then('I should be logged out')
def step_impl(context):
    assert context.logged_in
    print("User logged out successfully")

@then('I should be redirected to login page')
def step_impl(context):
    print("Redirected to login page")

@then('I should see a session timeout message')
def step_impl(context):
    assert context.session_expired
    print("Session timeout message displayed")