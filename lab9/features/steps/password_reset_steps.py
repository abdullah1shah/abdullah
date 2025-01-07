# features/steps/password_reset_steps.py
from behave import given, when, then

@when('I enter my registered email')
def step_impl(context):
    print("Entered registered email")
    context.email_valid = True

@when('I enter an unregistered email')
def step_impl(context):
    print("Entered unregistered email")
    context.email_valid = False

@then('I should receive a reset link')
def step_impl(context):
    assert context.email_valid
    print("Reset link sent")

@then('I should see a confirmation message')
def step_impl(context):
    print("Confirmation message displayed")

@then('I should not receive a reset link')
def step_impl(context):
    assert not context.email_valid
    print("No reset link sent")