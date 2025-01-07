from behave import when, then

@when('I enter my registered email')
def step_impl(context):
    print("Entered registered email")
    context.email_valid = True

@when('I enter an unregistered email')
def step_impl(context):
    print("Entered unregistered email")
    context.email_valid = False

@when('I click reset password button')
def step_impl(context):
    print("Clicked reset password button")
    context.reset_button_clicked = True

@then('I should receive a reset link')
def step_impl(context):
    assert context.email_valid and context.reset_button_clicked
    print("Reset link sent to registered email")

@then('I should see a confirmation message')
def step_impl(context):
    assert context.email_valid and context.reset_button_clicked
    print("Confirmation message displayed")

@then('I should not receive a reset link')
def step_impl(context):
    assert not context.email_valid
    print("No reset link sent")
